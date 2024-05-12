import cv2
import numpy as np
import tensorflow as tf
import pyttsx3

stop_thread = False

def real_time_recognition():
    global stop_thread
    model = tf.keras.models.load_model('saved_model/my_model')  # Load the model
    with open('categories.txt', 'r') as f:
        categories = [line.strip() for line in f.readlines()]
    
    camera = cv2.VideoCapture(0)
    engine = pyttsx3.init()

    while not stop_thread:
        ret, frame = camera.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        roi = gray_frame[100:300, 100:300]
        resized_roi = cv2.resize(roi, (64, 64))
        normalized_roi = resized_roi / 255.0
        prediction = model.predict(normalized_roi.reshape(-1, 64, 64, 1))
        predicted_label = np.argmax(prediction)
        label = categories[predicted_label]

        engine.say(label)
        engine.runAndWait()

        cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
        cv2.putText(frame, label, (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.imshow('Sign Language Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

# This function would be called by your Flask route to start/stop recognition