# Obesity Prediction

## Overview

This project is a web application that predicts a person's obesity level based on various input features, including eating habits and physical condition. Built with a machine learning model at its core, the app utilizes a trained model to estimate the obesity level of a person based on 16 features/information.

## Model & Dataset

The model used in the app is based on Neural Network built with TensorFlow. The training script of the model can be accessed through [this Kaggle Notebook](https://www.kaggle.com/code/ramaastra/obesity-prediction). The model was trained with a dataset that can be accessed in UCI Machine Learning Repository ([Estimation of Obesity Levels Based On Eating Habits and Physical Condition](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition))

## Installation

1. Clone this repository

```bash
git clone https://github.com/ramaastra/obesity-prediction.git
cd obesity-prediction
```

2. Create virtual env

```bash
python3 -m venv obesity-prediction-env
source obesity-prediction-env/bin/activate
```

or using Conda

```bash
conda create -n obesity-prediction-env python=3.10
conda activate obesity-prediction-env
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create Django settings script

```bash
cp ./obesity_prediction/settings.example.py ./obesity_prediction/settings.py
```

5. Add secret key to the settings script

```python
# File: obesity_prediction/settings.py

...

# Replace the placeholder with your desired key
SECRET_KEY = "secret-key-goes-here"

...
```

6. Run Django migration

```bash
python manage.py migrate
```

7. Run the server

```bash
python manage.py runserver
```

8. Open the local server (http://127.0.0.1:8000/)
