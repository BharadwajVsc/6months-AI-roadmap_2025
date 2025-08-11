import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load(
    r"D:\fsds\projects\Student Marks Predictor\student_marks_predictor_model.pkl"
)
df = pd.DataFrame()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    global df

    input_features = [float(x) for x in request.form.values()]
    features_value = np.array(input_features)

    if input_features[0] < 0 or input_features[0] > 24:
        return render_template(
            "index.html",
            prediction_text="Please enter valid hours between 1 to 24 cuz lets be real here, no one studies more than 13 hours a day.",
        )
    output = model.predict([features_value])[0][0].round(2)

    df = pd.concat(
        [
            df,
            pd.DataFrame({"Study Hours": input_features, "Predicted Output": [output]}),
        ],
        ignore_index=True,
    )
    print(df)
    df.to_csv("smp_data_from_app.csv", index=False)

    return render_template(
        "index.html",
        prediction_text=f"You will get {output}% marks, when you do study {int(features_value[0])} hours per day".format(
            output, int(features_value[0])
        ),
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
