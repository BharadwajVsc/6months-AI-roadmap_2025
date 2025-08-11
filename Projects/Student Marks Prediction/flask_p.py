from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", prediction_text="")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        feature1 = request.form.get("feature1", "")
        feature2 = request.form.get("feature2", "")

        # Dummy prediction (replace with your model)
        prediction = f"Feature1: {feature1}, Feature2: {feature2}"

        return render_template("index.html", prediction_text=prediction)
    except Exception as e:
        return f"Error: {e}", 500


if __name__ == "__main__":
    app.run(debug=True)
