##ASL Learning Tool

Welcome to the ASL Learning Tool, web application designed to help users learn American Sign Language (ASL) efficiently and interactively.

Features
Interactive Learning Modules: Engaging lessons to learn ASL basics.
Step By Step Learning: There are three levels for your steady and strong progress. Start with Level One: Alphabets, and once you have mastered it, move on to Level Two: Numbers and Level Three:Simple Words.
Google Login Integration: Easy login with your Google account.

Installation
To run this project locally, follow these steps:

Clone the repository:
git clone https://github.com/aabhab/ASL-Learning-Tool

Navigate to the project directory
cd ASL-Course-main

Install dependencies
npm install

Start the application
npm start

Usage
Launch the app on your web browser.
Sign up or log in using your Google account.
Navigate through the learning modules to start learning ASL.

Dependencies
React: Core library for building user interfaces.
React DOM: For rendering React applications in the browser.
Axios: For making HTTP requests.
React Router DOM: For navigation and routing within the app.
Gapi-script: For integrating Google login functionality.
Material-UI: For a set of React components that implement Google's Material Design.


ASL Learning Tool Backend
This backend component of the ASL Learning Tool handles real-time ASL gesture recognition using a trained machine learning model. It also provides an API for starting and stopping the recognition process.

Features
Real-Time Recognition: Recognizes ASL gestures in real-time using a webcam.
Text-to-Speech: Converts recognized gestures into spoken words.
REST API: Provides endpoints to start and stop the recognition process.


Installation
To set up the backend locally, follow these steps:

Clone the repository:
git clone https://github.com/aabhab/ASL-Learning-Tool

Navigate to the project directory
cd Backend

Install dependencies
pip install -r requirements.txt // Please note to install any other dependencies that you may need to start the backend

Run train_model.py to train the model:
python train_model.py

Start the Flask application
python app.py

Access the API to start recognition by sending a POST request to /start-recognition.

API Endpoints
POST /start-recognition
Starts the real-time ASL recognition process.
Response: {"message": "Recognition started"}

Dependencies
Flask: Micro web framework for Python.
Flask-CORS: For handling Cross-Origin Resource Sharing (CORS).
OpenCV: Library for real-time computer vision.
NumPy: Library for numerical computing.
TensorFlow: Library for machine learning and deep learning.
pyttsx3: Text-to-speech conversion library.

