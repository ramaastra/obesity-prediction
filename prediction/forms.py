from django import forms


class ObesityPredictionForm(forms.Form):
    gender = forms.ChoiceField(
        choices=[("Male", "Male"), ("Female", "Female")],
        required=True,
        label="Gender",
    )
    age = forms.IntegerField(min_value=1, required=True, label="Age")
    height = forms.FloatField(min_value=0.1, required=True, label="Height (metres)")
    weight = forms.FloatField(min_value=1, required=True, label="Weight (kilograms)")
    history = forms.ChoiceField(
        choices=[("no", "No"), ("yes", "Yes")],
        required=True,
        label="Has a family member suffered or suffers from overweight?",
    )
    favc = forms.ChoiceField(
        choices=[("no", "No"), ("yes", "Yes")],
        required=True,
        label="Do you eat high caloric food frequently?",
    )
    fcvc = forms.ChoiceField(
        choices=[("1", "Never"), ("2", "Sometimes"), ("3", "Always")],
        required=True,
        label="Do you usually eat vegetables in your meals?",
    )
    ncp = forms.IntegerField(
        min_value=1, required=True, label="How many main meals do you have daily?"
    )
    caec = forms.ChoiceField(
        choices=[
            ("no", "No"),
            ("Sometimes", "Sometimes"),
            ("Frequently", "Frequently"),
            ("Always", "Always"),
        ],
        required=True,
        label="Do you eat any food between meals?",
    )
    smoke = forms.ChoiceField(
        choices=[("no", "No"), ("yes", "Yes")], required=True, label="Do you smoke?"
    )
    ch2o = forms.FloatField(
        min_value=0.1,
        required=True,
        label="How much water do you drink daily? (Litres)",
    )
    scc = forms.ChoiceField(
        choices=[("no", "No"), ("yes", "Yes")],
        required=True,
        label="Do you monitor the calories you eat daily?",
    )
    faf = forms.ChoiceField(
        choices=[
            ("0", "I do not have"),
            ("1", "1 or 2 days"),
            ("2", "2 or 4 days"),
            ("3", "4 or 5 days"),
        ],
        required=True,
        label="How often do you have physical activity? (Weekly)",
    )
    tue = forms.ChoiceField(
        choices=[("0", "0-2 hours"), ("1", "3-5 hours"), ("2", "More than 5 hours")],
        required=True,
        label="How much time do you use technological devices? (Daily)",
    )
    calc = forms.ChoiceField(
        choices=[
            ("no", "No"),
            ("Sometimes", "Sometimes"),
            ("Frequently", "Frequently"),
            ("Always", "Always"),
        ],
        required=True,
        label="How often do you drink alcohol?",
    )
    mtrans = forms.ChoiceField(
        choices=[
            ("Public_Transportation", "Public Transportation"),
            ("Automobile", "Automobile"),
            ("Walking", "Walking"),
            ("Motorbike", "Motorbike"),
            ("Bike", "Bike"),
        ],
        required=True,
        label="Which transportation do you usually use?",
    )
