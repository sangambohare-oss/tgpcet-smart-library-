import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model("plant_disease_model.h5")

classes = ["Healthy", "Leaf Blight", "Rust", "Nutrient Deficiency"]

def predict(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    x = image.img_to_array(img)/255.0
    x = np.expand_dims(x, axis=0)

    pred = model.predict(x)
    idx = np.argmax(pred)

    return {
        "disease": classes[idx],
        "confidence": float(np.max(pred))
    }