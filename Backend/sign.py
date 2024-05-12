#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import cv2
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import pyttsx3


# In[ ]:


# Step 1: Data Loading and Preprocessing
data_directory = 'asl_alphabet_train'
categories = os.listdir(data_directory)
num_classes = len(categories)
image_size = 64
X = []
y = []
max_images_per_category = 1000  # Limit the number of images per category


# In[ ]:


for category_id, category in enumerate(categories):
    folder_path = os.path.join(data_directory, category)
    image_count = 0
    for img in os.listdir(folder_path):
        if image_count >= max_images_per_category:
            break
        image_path = os.path.join(folder_path, img)
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        image = cv2.resize(image, (image_size, image_size))
        X.append(image)
        y.append(category_id)
        image_count += 1
    
X = np.array(X) / 255.0
y = np.array(y)


# In[ ]:


# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[ ]:


# Reshape the data for TensorFlow compatibility
X_train = X_train.reshape(-1, image_size, image_size, 1)
X_test = X_test.reshape(-1, image_size, image_size, 1)


# In[ ]:


# Step 2: Model Building
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(image_size, image_size, 1)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))


# In[ ]:


# Function to draw bounding box and label
def draw_bbox(frame, x, y, w, h, label):
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


# In[ ]:


# Step 4: Real-Time Image Recognition with ROI and Bounding Box
camera = cv2.VideoCapture(0)
engine = pyttsx3.init()

while True:
    ret, frame = camera.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Define the region of interest (ROI)
    #roi = frame[100:300, 100:300]
    roi = gray_frame[100:300, 100:300]
    
    resized_roi = cv2.resize(roi, (image_size, image_size))
    normalized_roi = resized_roi / 255.0
    prediction = model.predict(normalized_roi.reshape(-1, image_size, image_size, 1))
    predicted_label = np.argmax(prediction)
    label = categories[predicted_label]
    
    # Speak out the predicted label
    engine.say(label)
    engine.runAndWait()
    
    # Draw bounding box around ROI with label
    draw_bbox(frame, 100, 100, 200, 200, label)
    
    cv2.imshow('Sign Language Recognition', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()


# In[ ]:




