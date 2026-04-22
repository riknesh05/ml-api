from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ML API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    status = data.get("status", "")

    if status == "ok":
        result = {
            "label": "OK",
            "message": "Signal received. All good!",
            "confidence": 1.0
        }
    else:
        result = {
            "label": "UNKNOWN",
            "message": "Unexpected signal received",
            "confidence": 0.0
        }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)