import cv2
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import os

def prepare_model():
    data_directory = 'asl_alphabet_train'
    categories = os.listdir(data_directory)
    num_classes = len(categories)
    image_size = 64
    X, y = [], []
    max_images_per_category = 1000

    for category_id, category in enumerate(categories):
        folder_path = os.path.join(data_directory, category)
        image_count = 0
        for img in os.listdir(folder_path):
            if image_count >= max_images_per_category:
                break
            image_path = os.path.join(folder_path, img)
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = cv2.resize(image, (image_size, image_size))
            X.append(image)
            y.append(category_id)
            image_count += 1

    X = np.array(X) / 255.0
    y = np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train = X_train.reshape(-1, image_size, image_size, 1)
    X_test = X_test.reshape(-1, image_size, image_size, 1)

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

    model.save('saved_model/my_model')  # Save the model
    with open('categories.txt', 'w') as f:
        for category in categories:
            f.write("%s\n" % category)

if __name__ == "__main__":
    prepare_model()
