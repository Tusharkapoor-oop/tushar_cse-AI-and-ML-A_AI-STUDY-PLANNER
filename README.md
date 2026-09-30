# AI Study Planner

**Syllabus → topics → week-by-week study plan + curated videos.** A Flask app built by a 4-person team; I owned the backend.

> Team: **Tushar** (backend) · **Manipal** (backend) · **Poras** (frontend) · **Swayam** (frontend)

---

## What it does

1. **Upload** a syllabus (PDF or TXT).
2. **Extract** topics (`syllabus_processor.py` — heading/regex parsing).
3. **Schedule** topics across weeks (`scheduler.py` — deadline-aware spreading).
4. **Recommend** YouTube videos per topic (`video_recommender.py`).
5. **Render** dashboard + result pages.

```
upload → pdfplumber (fallback: PyPDF2) → extract_topics() → session
      → dashboard.html (topics + video links)
      → result.html (generated schedule)
```

---

## Actual repository layout

```
app.py                    # Flask app (all routes)
syllabus_processor.py     # topic extraction
scheduler.py              # schedule generation
video_recommender.py      # video suggestions
index.html upload.HTML    # ┐
dashboard.html result.html│ ├ must live in templates/ (see step 1)
style.css                 # ┘ must live in static/
README.md
extras: project video (mp4), report (pdf), slides (pptx)
```

## How to run

> **Important:** Flask only serves templates from `templates/`. The HTML files currently sit at
> the repo root — reorganize once after cloning (nothing is deleted, just moved into place):

```bash
git clone https://github.com/Tusharkapoor-oop/tushar_cse-AI-and-ML-A_AI-STUDY-PLANNER.git
cd tushar_cse-AI-and-ML-A_AI-STUDY-PLANNER

# one-time: put templates/static where Flask expects them
mkdir -p templates static
mv index.html dashboard.html result.html templates/
mv upload.HTML templates/upload.html     # note: lowercase .html for Linux
mv style.css static/

# dependencies
pip install flask pdfplumber PyPDF2 werkzeug flask_sqlalchemy flask_login

# run
python app.py
# → http://127.0.0.1:5000
```

Test with any text/PDF syllabus — the app deletes your upload immediately after parsing.

---

## Design notes (backend)

- **Encoding-agnostic text reads:** TXT uploads are tried as UTF-8 → Latin-1 → UTF-16.
- **PDF fallback chain:** `pdfplumber` first (tables + layout), `PyPDF2` if that yields nothing.
- **Session-scoped state:** topics live in the Flask session — no database required for the core flow.
- **Upload hygiene:** `secure_filename` + extension allow-list + immediate `os.remove` after parse.
- **Limit:** 16 MB upload cap (`MAX_CONTENT_LENGTH`).

## Known limitations

- Topic extraction is rule-based (regex/heading heuristics), not an LLM — precision varies with syllabus formatting.
- `app.run(debug=True)` is the documented dev mode; put a real WSGI server in front for anything shared.
- No automated tests yet — planned: pytest fixtures around `extract_topics()` with 3 sample syllabi.
- The walkthrough video (16.7 MB `project video final (2) (1) (1).mp4`) will move to a GitHub Release to keep the clone small.

## Video walkthrough

[Project walkthrough (Google Drive)](https://drive.google.com/file/d/1JtjUFm0z1JoPtQdX6HzAEomDywbVcx3T/view?usp=drivesdk)

## License

No license file yet — MIT intended (to be added by the repository owner).
