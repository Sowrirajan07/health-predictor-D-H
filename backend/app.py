from flask import Flask, request, jsonify
from predict import predict_diabetes, predict_heart

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    diabetes_data = request.json["diabetes"]
    heart_data = request.json["heart"]

    d_pred, d_prob = predict_diabetes(diabetes_data)
    h_pred, h_prob = predict_heart(heart_data)

    return jsonify({
        "diabetes": d_pred,
        "diabetes_probability": d_prob,
        "heart": h_pred,
        "heart_probability": h_prob
    })

if __name__ == "__main__":
    app.run(debug=True)