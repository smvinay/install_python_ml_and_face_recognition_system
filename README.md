# install_python_ml_and_face_recognition_system
A simple Face Recognition system using Python, OpenCV, and face_recognition library.  The system detects faces from the webcam and recognizes them using a dataset of known faces.


Face Recognition System (Python + ML)

A simple Face Recognition system using Python, OpenCV, and face_recognition library.

The system detects faces from the webcam and recognizes them using a dataset of known faces.

1. System Requirements
Software	Version
OS	Windows 10 / Windows 11
Python	3.10.11
pip	26.0+
numpy	1.23.5
dlib	19.22.99
face-recognition	1.3.0
opencv-python	4.13.0

Important:

numpy 2.x is NOT supported by dlib

Use:

numpy==1.23.5
2. Install Python

Download Python:

https://www.python.org/downloads/release/python-31011/

During installation:

Enable:

Add Python to PATH

Verify installation:

python --version

Output:

Python 3.10.11
3. Install Visual Studio Build Tools (Required for dlib)

Download:

https://visualstudio.microsoft.com/visual-cpp-build-tools/

Install workload:

Desktop development with C++

Required components:

MSVC v143 C++ build tools
Windows 10/11 SDK
C++ CMake tools
4. Create Project Folder

Create a folder:

D:\python\face_recognition_project

Navigate to folder:

cd D:\python\face_recognition_project
5. Create Virtual Environment

Create venv:

python -m venv venv

Activate environment:

venv\Scripts\activate

Terminal should show:

(venv)

Verify Python path:

Get-Command python

Expected:

venv\Scripts\python.exe
6. Install Required Libraries

Upgrade pip:

python -m pip install --upgrade pip

Install packages:

pip install numpy==1.23.5
pip install opencv-python
pip install dlib
pip install face-recognition
pip install pillow

Verify installation:

pip list

Expected output:

numpy                 1.23.5
opencv-python         4.13.0
dlib                  19.22.99
face-recognition      1.3.0
pillow
7. Project Structure
face_recognition_project
│
├── dataset
│   ├── john.jpg
│   ├── alice.jpg
│
├── main.py
├── README.md
└── venv

Each image in dataset represents a known person.

8. Face Recognition Code

Create main.py
code is in file 

9. Run the Application

Run:

python main.py

The webcam will open.

Detected faces will display:

Person Name

or

Unknown

Press:

ESC

to exit.

10. How Face Recognition Works

The ML pipeline:

Image
 ↓
Face Detection
 ↓
Face Encoding (128 feature vector)
 ↓
Compare Encodings
 ↓
Recognition

Example encoding:

[0.123, -0.543, 0.981, ... 128 values]

These 128 numbers uniquely represent a face.

11. Adding New People

Add images to the dataset folder:

dataset
 ├── john.jpg
 ├── david.jpg
 ├── alice.jpg

The file name becomes the recognized label.

12. Future Improvements

Possible extensions:

Face Attendance System
Database storage
Multiple camera support
Face training pipeline
Face recognition API
13. GitHub Setup

Initialize repository:

git init

Add files:

git add .

Commit:

git commit -m "Initial Face Recognition System"

Push to GitHub:

git remote add origin https://github.com/username/face-recognition-system.git
git push -u origin main
14. License

MIT License
