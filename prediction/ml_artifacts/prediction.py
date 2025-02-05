import tensorflow as tf
import numpy as np
import pickle

MODEL_PATH = "prediction/ml_artifacts/model.keras"
LABEL_ENCODER_PATH = "prediction/ml_artifacts/label_encoder.pkl"


def predict(df, model_path=MODEL_PATH, label_encoder_path=LABEL_ENCODER_PATH):
    model = tf.keras.models.load_model(model_path)

    with open(label_encoder_path, "rb") as f:
        label_encoder = pickle.load(f)

    y_proba = model.predict(df, verbose=0)
    y_pred = np.argmax(y_proba[0])
    pred_label = label_encoder.categories_[0][y_pred]

    return pred_label
