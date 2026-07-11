from flask import Flask, request, jsonify
from PIL import Image

app = Flask(__name__)

def predict_disease(image):
    return {
        "crop": "Tomato",
        "disease": "Leaf Blight",
        "confidence": 0.82,
        "action": "Spray copper fungicide"
    }

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]
    img = Image.open(file.stream)

    result = predict_disease(img)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)