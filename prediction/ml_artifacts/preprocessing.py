import pandas as pd
import pickle

FEATURES_ENCODER_PATH = "prediction/ml_artifacts/features_encoder.pkl"
CATEGORICAL_COLS = [
    "Gender",
    "family_history_with_overweight",
    "FAVC",
    "CAEC",
    "SMOKE",
    "SCC",
    "CALC",
    "MTRANS",
]
FEATURES_SCALER_PATH = "prediction/ml_artifacts/features_scaler.pkl"
NUMERICAL_COLS = ["Age", "Height", "Weight", "FCVC", "NCP", "CH2O", "FAF", "TUE"]


def encode_features(
    df,
    features_encoder_path=FEATURES_ENCODER_PATH,
    categorical_cols=CATEGORICAL_COLS,
):
    with open(features_encoder_path, "rb") as f:
        encoder = pickle.load(f)

    features_encoded = encoder.transform(df[categorical_cols])
    features_encoded_df = pd.DataFrame(
        features_encoded, columns=encoder.get_feature_names_out(categorical_cols)
    )
    df = pd.concat([df.reset_index(drop=True), features_encoded_df], axis=1)
    df = df.drop(categorical_cols, axis=1)

    return df


def scale_features(
    df,
    features_scaler_path=FEATURES_SCALER_PATH,
    numerical_cols=NUMERICAL_COLS,
):
    with open(features_scaler_path, "rb") as f:
        scaler = pickle.load(f)

    features_scaled = scaler.transform(df[numerical_cols])
    features_scaled_df = pd.DataFrame(
        features_scaled, columns=scaler.get_feature_names_out(numerical_cols)
    )
    df[numerical_cols] = features_scaled_df[numerical_cols]

    return df


def preprocess_input(
    raw_data,
    features_encoder_path=FEATURES_ENCODER_PATH,
    categorical_cols=CATEGORICAL_COLS,
    features_scaler_path=FEATURES_SCALER_PATH,
    numerical_cols=NUMERICAL_COLS,
):
    df = pd.DataFrame(
        {
            "Gender": [raw_data["gender"]],
            "Age": [raw_data["age"]],
            "Height": [raw_data["height"]],
            "Weight": [raw_data["weight"]],
            "family_history_with_overweight": [raw_data["history"]],
            "FAVC": [raw_data["favc"]],
            "FCVC": [int(raw_data["fcvc"])],
            "NCP": [raw_data["ncp"]],
            "CAEC": [raw_data["caec"]],
            "SMOKE": [raw_data["smoke"]],
            "CH2O": [raw_data["ch2o"]],
            "SCC": [raw_data["scc"]],
            "FAF": [int(raw_data["faf"])],
            "TUE": [int(raw_data["tue"])],
            "CALC": [raw_data["calc"]],
            "MTRANS": [raw_data["mtrans"]],
        }
    )

    preprocessed_df = encode_features(df, features_encoder_path, categorical_cols)
    preprocessed_df = scale_features(
        preprocessed_df, features_scaler_path, numerical_cols
    )

    return preprocessed_df
