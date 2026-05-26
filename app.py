import cv2
import numpy as np
import pytesseract
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from tensorflow.keras.preprocessing.image import img_to_array


# For Windows
# pytesseract.pytesseract.tesseract_cmd =
# r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# -----------------------------
# IMAGE RECOGNITION
# -----------------------------
model = MobileNetV2(weights="imagenet")


def recognize_image(image_path):

    image = cv2.imread(image_path)

    resized = cv2.resize(image, (224, 224))

    arr = img_to_array(resized)

    arr = np.expand_dims(arr, axis=0)

    arr = preprocess_input(arr)

    predictions = model.predict(arr)

    results = decode_predictions(predictions, top=3)[0]

    print("\nImage Recognition Result:")
    print("---------------------------")

    for (_, label, confidence) in results:
        print(
            f"{label} → {confidence*100:.2f}%"
        )


# -----------------------------
# TEXT RECOGNITION
# -----------------------------
def recognize_text(image_path):

    img = Image.open(image_path)

    text = pytesseract.image_to_string(img)

    print("\nRecognized Text:")
    print("---------------------------")

    if text.strip():
        print(text)

    else:
        print("No text detected.")


# -----------------------------
# MENU
# -----------------------------
while True:

    print("\nAI Recognition System")

    print("1. Image Recognition")

    print("2. Text Recognition")

    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":

        path = input(
            "Enter image path: "
        )

        recognize_image(path)

    elif choice == "2":

        path = input(
            "Enter image path: "
        )

        recognize_text(path)

    elif choice == "3":


        print("Exiting...")

        break

    else:

        print("Invalid choice")