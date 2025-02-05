from django.shortcuts import render, redirect
from .forms import ObesityPredictionForm
from .ml_artifacts.preprocessing import preprocess_input
from .ml_artifacts.prediction import predict


def index(request):
    context = {}

    prediction_history = request.session.get("prediction")
    if prediction_history:
        context["prediction_result"] = prediction_history["result"]
        context["form"] = ObesityPredictionForm(initial=prediction_history["data"])
    else:
        context["form"] = ObesityPredictionForm()

    return render(request, "prediction/index.html", context)


def predict_input(request):
    form = ObesityPredictionForm(request.POST)
    if form.is_valid():
        preprocessed_data = preprocess_input(form.cleaned_data)
        prediction = predict(preprocessed_data).replace("_", " ")
        request.session["prediction"] = {
            "data": form.cleaned_data,
            "result": prediction,
        }
        return redirect("index")
