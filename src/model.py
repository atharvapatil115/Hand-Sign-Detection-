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
from joblib import load

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
model_path = os.path.join(root_dir, "Saved_models", "Gesture_trained_model.joblib")
encoder_model_path = os.path.join(root_dir, "Saved_models", "label_encoder.joblib")

cap = cv.VideoCapture(0)
previous_time = 0
current_time = 0
encoder = load(encoder_model_path)
detector=HandDetector()
model = load(model_path)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame")
        break

    img = detector.findHands(img)
    current_time = time.time()

    lmlist = detector.findPosition(img)

    if lmlist:  # Check if lmlist is not empty
        # Flatten the list of landmarks and reshape it for the model
        # It should be a 2D array: (number of samples, number of features)
        # In this case, 1 sample and 21 * 3 features (x, y, z for 21 landmarks)
        input_data = np.array(lmlist).flatten().reshape(1, -1)

        # Only predict if input_data has the correct number of features for the model
        # The number of features should match what the model was trained on
        # For 21 landmarks (x, y, z), it's 21 * 3 = 63 features
        expected_features = 21 * 3
        if input_data.shape[1] == expected_features:
            pred = model.predict(input_data)
            pred_label = encoder.inverse_transform(pred)[0]
            cv.putText(img, pred_label, (10, 100), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        else:
            cv.putText(img, "Incorrect features", (10, 90), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
            print(f"Warning: Landmark list has {len(lmlist)} points, but expected 21. Reshaped input has {input_data.shape[1]} features, expected {expected_features}.")
    else:
        print("No landmarks detected")
        cv.putText(img, "No hand detected", (10, 90), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)


    fps = 1 / (current_time - previous_time)
    previous_time = current_time
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv.imshow("image", img)

    if cv.waitKey(1) & 0xFF == ord('q'): # Add a way to exit the loop
        break

cap.release()
cv.destroyAllWindows()