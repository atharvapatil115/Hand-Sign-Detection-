import numpy as np
from joblib import load
import os 

base_path = os.path.join("..", "Saved_models")
model_path = os.path.join(base_path,"Gesture_trained_model.joblib")
encoder_model_path = os.path.join(base_path,"label_encoder.joblib")

def test_model_prediction():
    model = load(model_path)
    dummy_imput = np.random.rand(1,63)
    pred = model.predict(dummy_imput)
    assert pred is not None

test_model_prediction()