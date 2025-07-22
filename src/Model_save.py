import cv2 as cv
import os
import mediapipe
import time
from hand_landmarks import HandDetector
from sklearn.neural_network import MLPClassifier
from gestures import HandGestures
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from joblib import dump



detector = HandDetector()
gestures = HandGestures()

# Increase max_iter for the MLPClassifier to help with convergence
model = MLPClassifier(
    hidden_layer_sizes=(128, 64),
    activation="relu",
    solver="adam",
    batch_size=100,
    learning_rate="adaptive",
    random_state=42,
    max_iter=500,  # Increased max_iter
    tol=1e-4 # Added tolerance for convergence
)
encoder = LabelEncoder()
X = []
Y = []
gesture_class = ["Abuse", "Hello", "i Love You", "peace", "stop", "thumb's up"]
base_path = os.path.join("..", "dataset")

for label in os.listdir(base_path):
    label_path = os.path.join(base_path, label)
    if label.endswith(".py"):
        continue

    for file in os.listdir(label_path):
        if file.endswith(".npy"):
            data = np.load(os.path.join(label_path, file))
            X.append(data)
            Y.append(label)
        else:
            print(f"No .npy file found in {label_path}") # More specific message

X = np.array(X)
Y = np.array(Y)
Y_encoded = encoder.fit_transform(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y_encoded, test_size=0.2, random_state=42)

# Ensure X_train and Y_train are not empty before fitting
if len(X_train) > 0 and len(Y_train) > 0:
    model.fit(X_train, Y_train)
else:
    print("Warning: Training data (X_train or Y_train) is empty. Model will not be trained.")

dump(model,"Gesture_trained_model.joblib")
dump(encoder, "label_encoder.joblib") # <--- SAVE THE ENCODER!
