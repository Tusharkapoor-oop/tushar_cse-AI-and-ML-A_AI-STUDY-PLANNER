#  tushar_cse-AI-and-ML-A_AI-STUDY-PLANNER

This project is an AI-based Study Planner designed to help students **automatically generate study plans** and **find relevant educational videos**. It combines both frontend and backend components to deliver a smart planning experience. Users interact with the system by uploading a syllabus file, which is then processed to extract key topics. Based on these topics, a personalized study plan is created along with YouTube video suggestions to support the learning process.

---

#  AI-Based Study Planner

##  Team Members
- **Tushar** – Frontend Developer  
- **Manipal** – Frontend & Backend Developer  
- **Poras** – Backend Developer  
- **Swayam** – Backend Developer

##  Project Description
The AI-Based Study Planner is a personalized productivity tool built to help students plan, organize, and track their studies effectively. Using AI-powered logic and a user-friendly interface, the planner suggests daily schedules based on syllabus content, deadlines, and individual study goals.

Our mission is to remove the stress of manual planning and help students build consistent study habits — especially useful during tight exam preparation timelines.

---

##  Video Explanation
👉 [Click here to watch the project walkthrough video](https://your-video-link-here.com)

---

##  Technologies Used
- **Python 3.12.9** *(mandatory version – fixes compatibility issues)*  
- **Flask** – Web framework for backend  
- **MySQL** – Relational database for storing user/session data  
- **HTML + CSS** – Frontend UI  
- **pdfplumber** – PDF processing  
- **Flask-Login** – User session management  
- **Flask-SQLAlchemy** – Database ORM  
- **AI Logic** – Custom scheduler and video recommendation logic

---

##  How to Run the Project

###  1. Install Python (Version 3.12.9 required)
Make sure you are using Python 3.12.9 to avoid unknown errors.

###  2. Install Required Libraries
```bash
pip install flask
pip install pdfplumber
pip install werkzeug
pip install flask_sqlalchemy
pip install flask_login
```

###  3. Project Folder Structure

```
AI_Study_Planner/
│
├── app.py                        # Main Flask app — connects frontend & backend
│
├── syllabus_processor.py         # Handles topic extraction from uploaded syllabus
├── scheduler.py                  # Creates personalized study plan (schedule)
├── video_recommender.py          # Recommends YouTube videos for topics
│
├── uploads/                      # Temp folder to store uploaded files
│   └── (Uploaded PDFs/TXT files — deleted after processing)
│
├── templates/                    # HTML templates (Frontend)
│   ├── index.html                # Landing page
│   ├── upload.html               # File upload page
│   ├── dashboard.html            # Topics + Video Recommendations
│   └── result.html               # Final Study Plan
│
├── static/                       # CSS and other frontend assets
│   └── styles.css                # Stylesheet for all HTML pages
```

###  4. Run the Flask App
```bash
python app.py
```

###  5. Open the App in Your Browser
Go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the planner.

---

## 💬 Final Note

This tool was developed with students in mind. If you have any ideas to improve the user experience or extend the AI capabilities, feel free to contribute or reach out!


