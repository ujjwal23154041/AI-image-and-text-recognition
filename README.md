# AI-image-and-text-recognition
# 🧠 AI Image or Text Recognition (Basic)

A simple Artificial Intelligence project that performs **Image Recognition** and **Text Recognition (OCR)** using pre-trained AI libraries.

This project demonstrates how AI models can recognize objects in images and extract text from images.

---

## 📌 Project Overview

This project is developed to implement basic AI recognition tasks using available libraries.

### Features
✅ Image Recognition using a pre-trained model  
✅ Text Recognition (OCR) from images  
✅ User-friendly command line interface  
✅ Clear output display  
✅ Easy setup and execution  

---

## 🚀 Technologies Used

- Python
- TensorFlow
- MobileNetV2
- OpenCV
- Tesseract OCR
- Pillow
- NumPy

---

## 📂 Project Structure

```plaintext
AI_Image_Text_Recognition/
│
├── app.py
├── requirements.txt
├── README.md
├── sample_images/
│   └── sample.jpg
└── output/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI_Image_Text_Recognition.git
```

### Move into Project Folder

```bash
cd AI_Image_Text_Recognition
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Install Tesseract OCR

### Windows

Download and install:

https://github.com/UB-Mannheim/tesseract/wiki

After installation add this inside `app.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## ▶️ Run Project

```bash
python app.py
```

---

## 📷 Image Recognition

Detects objects inside an image using **MobileNetV2**.

Example:

Input:
```plaintext
dog.jpg
```

Output:
```plaintext
labrador → 95%
golden_retriever → 3%
beagle → 2%
```

---

## 📝 Text Recognition (OCR)

Extracts text from images.

Example:

Input:
```plaintext
book.jpg
```

Output:
```plaintext
Artificial Intelligence Project
```

---

## 💡 How It Works

### Image Recognition
- Load image
- Resize image
- Apply preprocessing
- Predict using MobileNetV2
- Display top predictions

### Text Recognition
- Load image
- Process using Tesseract OCR
- Extract and display text

---

## 📌 Requirements

```txt
opencv-python
numpy
tensorflow
pillow
pytesseract
```

Install manually:

```bash
pip install opencv-python numpy tensorflow pillow pytesseract
```

---

## 🎯 Learning Outcomes

- Understanding AI model outputs
- Using pre-trained models
- Implementing OCR
- Working with computer vision

---

## 📜 License

This project is open-source and available for educational purposes.

---

## 👨‍💻 Author

**Ujjwal Pandit**

Artificial Intelligence Project – Project 4
