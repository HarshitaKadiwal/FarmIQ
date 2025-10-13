from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import json
import os

app = Flask(__name__)

# Load model & classes
model = tf.keras.models.load_model("tomato_disease_model.h5")
with open("class_indices.json", "r") as f:
    class_indices = json.load(f)
class_names = list(class_indices.keys())

def predict_leaf(img_path):
    img = image.load_img(img_path, target_size=(128,128))
    img_array = image.img_to_array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)
    return class_names[class_idx]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    img_path = None
    if request.method == "POST":
        file = request.files["file"]
        if not os.path.exists("static"):
            os.makedirs("static")
        file_path = os.path.join("static", file.filename)
        file.save(file_path)
        prediction = predict_leaf(file_path)
        img_path = file_path
    return render_template("index.html", prediction=prediction, img_path=img_path)

if __name__ == "__main__":
    app.run(debug=True)
