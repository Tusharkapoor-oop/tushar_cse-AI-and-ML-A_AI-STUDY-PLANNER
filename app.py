import os
import secrets
import pdfplumber
from PyPDF2 import PdfReader
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename

from syllabus_processor import extract_topics
from scheduler import generate_schedule
from video_recommender import recommend_videos

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') or secrets.token_hex(16)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def pull_text_from_pdf(filepath):
    """
    Try pdfplumber first; if that yields no text, fall back to PyPDF2.
    """
    text_chunks = []
    # First pass: pdfplumber
    try:
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                txt = page.extract_text()
                if txt:
                    text_chunks.append(txt)
    except Exception as e:
        app.logger.debug(f"pdfplumber error: {e}")

    full_text = "\n".join(text_chunks).strip()
    if full_text:
        app.logger.debug(f"PDF text length via pdfplumber: {len(full_text)}")
        return full_text

    # Fallback to PyPDF2
    try:
        reader = PdfReader(filepath)
        fallback = []
        for page in reader.pages:
            t = page.extract_text()
            if t:
                fallback.append(t)
        result = "\n".join(fallback).strip()
        app.logger.debug(f"PDF text length via PyPDF2: {len(result) if result else 0}")
        return result if result else None
    except Exception as err:
        flash(f"PDF parse error: {err}", 'danger')
        return None

def pull_text_from_txt(filepath):
    """
    Try reading the TXT file with multiple encodings and log a snippet.
    """
    for enc in ('utf-8', 'latin-1', 'utf-16'):
        try:
            with open(filepath, 'r', encoding=enc) as f:
                data = f.read()
                if data:
                    snippet = data[:200].replace('\n', ' ').replace('\r', '')
                    app.logger.debug(f"[TXT-{enc}] snippet: {snippet!r}")
                    return data.strip()
        except Exception as e:
            app.logger.debug(f"[TXT-{enc}] read error: {e}")
            continue

    flash("Unable to read text file (tried UTF-8, Latin-1, UTF-16).", 'danger')
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or not allowed_file(file.filename):
            flash("Only PDF or TXT files are allowed.", 'danger')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)

        # Extract text based on extension
        if filename.lower().endswith('.pdf'):
            text = pull_text_from_pdf(path)
        else:
            text = pull_text_from_txt(path)

        # Clean up the upload immediately
        os.remove(path)

        # Log and handle missing text
        if not text:
            app.logger.debug("No text extracted from file.")
            return redirect(request.url)
        app.logger.debug(f"Total text length: {len(text)}")

        # Extract topics
        topics = extract_topics(text)
        app.logger.debug(f"Topics extracted: {topics}")

        if not topics:
            flash("No topics found in that file.", 'warning')
            return redirect(request.url)

        session['topics'] = topics
        return redirect(url_for('dashboard'))

    return render_template('upload.html')

@app.route('/dashboard')
def dashboard():
    topics = session.get('topics', [])
    if not topics:
        flash("Please upload a syllabus first.", 'info')
        return redirect(url_for('upload'))

    video_links = recommend_videos(topics)
    return render_template('dashboard.html', topics=topics, video_links=video_links)

@app.route('/analyze_and_plan', methods=['POST'])
def analyze_and_plan():
    topics = session.get('topics', [])
    schedule = generate_schedule(topics) if topics else None
    return render_template('result.html', schedule=schedule)

if __name__ == '__main__':
    # Enable debug logging
    app.run(debug=True)


    









