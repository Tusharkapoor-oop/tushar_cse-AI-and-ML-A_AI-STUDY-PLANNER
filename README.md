# tushar_cse-AI-and-ML-A_AI-STUDY-PLANNER
This project is an AI-based Study Planner designed to help students automatically generate  study plans and find relevant educational videos.  The project consists of both frontend and backend components.  The user interacts with the system by uploading a syllabus, which is processed to extract  key topics.  


# 📚 AI-Based Study Planner

## 👨‍💻 Team Members
- **Tushar** – Frontend Developer  
- **Manipal** – Frontend & Backend Developer  
- **Poras** – Backend Developer  
- **Swayam** – Backend Developer

## 📝 Project Description
The AI-Based Study Planner is a personalized productivity tool built to help students plan, organize, and track their studies effectively. Using AI logic and a user-friendly interface, the planner suggests daily schedules based on subjects, deadlines, and individual study patterns. Our goal was to eliminate the stress of manual planning and help students maintain consistency, especially during exam seasons.

## 🎥 Video Explanation
[Click here to watch the project walkthrough video](https://your-video-link-here.com)

## 🛠️ Technologies Used
- **Python**  
- **Flask** (for backend)  
- **MySQL** (for data storage)  
- **HTML + CSS** (for frontend interface)  
- **AI Logic** (for planning and scheduling)

## 🚀 How to Run the Project

 first download the specific verision python that is 3.12.9
  becaue it has fix some unkown errors then import some libraies 
pip install flask
pip install pdfplumber
pip install werkzeug
pip install flask_sqlalchemy
pip install flask_login

PROJECT MUST BE FOLLOWING STRUCTUR ::--

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



