Python Quest 
( Learn Python by Doing)


1. Overview
Python Quest is a small, interactive command-line learning application created to make Python fundamentals easier to practise.
Instead of presenting only a long list of quiz questions, the application follows a simple learning cycle:
Learn 
 Practice 
 Get feedback 
 Save progress 
 Review

The project covers the five academic units already present in the original project:
Problem Solving and Algorithms
Python Basics
Fundamental Algorithms and Control Flow
Factoring / Mathematical Algorithms
Python Data Structures

The project is intentionally built with Python's standard library so that a student can run it without installing a large number of external packages.


2. Features
Learner profile using a name
Five syllabus-based learning units
Interactive multiple-choice checkpoints
Input validation for menu and question choices
Immediate feedback and explanations
Score tracking
Accuracy calculation
Completed-unit tracking
Mistake tracking for revision
JSON-based progress saving
Progress report
Reset-progress option
Unit and model tests


3. Functional Modules
Module 1 
 Learning
Shows short, human-readable explanations for each unit.
Module 2 
 Practice
Presents questions, validates answers and gives immediate feedback.
Module 3 
 Progress & Reporting
Tracks score, accuracy, completed units and questions that need revision.

Supporting functionality
Player/profile management
JSON storage
Input validation
Automated tests


4. Project Structure
vityarthi_python_quest/

 main.py
 requirements.txt
 README.md
 statement.md
 .gitignore

 app/
 __init__.py
 models.py
 questions.py
 lessons.py
 quiz.py
 reports.py
 storage.py
 ui.py

 data/
  progress.json          # created after the first save

 tests/
 test_models.py
 test_questions.py
 test_storage.py

 docs/
     design.md
     use_case.mmd
     workflow.mmd
     sequence.mmd
     class_diagram.mmd
     schema.md


5. Technologies
Python 3.10+
Python standard library
JSON for local progress storage
unittest for testing
Git/GitHub for version control


6. How to Run
Open a terminal in the project folder:
python main.py
No external package installation is required.


7. How to Test
Run:
python -m unittest discover -s tests -v
The tests check the player model, question bank and save/load behaviour.


8. Typical User Flow
Start the application.
Enter a name.
Choose Learn a unit to read a short explanation.
Choose Practice a unit.
Answer the checkpoint questions.
Receive immediate feedback.
View the progress report.
Exit; progress is saved automatically.
Return later and continue from the saved profile.


9. Design Decisions
Why a CLI?
The original project was already a console-based Python learning game. Keeping the CLI makes the conversion realistic and lets the project focus on Python concepts rather than spending most of the implementation time on a graphical framework.
Why JSON?
The project only needs to store one learner's lightweight progress. JSON is easy to understand, inspect and maintain for a student-level application.
Why separate modules?
Separating models, questions, lessons, quiz logic, storage, reporting and UI makes the project easier to understand, test and extend than keeping all 500+ lines in one file.


10. Future Enhancements
Add a graphical interface
Add a larger question bank
Add difficulty levels
Add timed challenges
Add a leaderboard for classroom use
Store multiple learner profiles
Add charts showing progress over time
Add a teacher/admin question-management screen
