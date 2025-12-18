
# AI-Based Real-Time Accident Detection System

![Python](https://img.shields.io/badge/python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/tensorflow-2.12-orange)
![OpenCV](https://img.shields.io/badge/opencv-4.7.0-brightgreen)

A real-time accident detection system built using **TensorFlow/Keras CNN** and **OpenCV**, capable of analyzing live video feeds to accurately detect road accidents. The system includes **automated email alerts**, **sound notifications**, and **time/location tagging** using Geocoder to enable immediate emergency response.

---

## 1. Demonstration

You can showcase your demo video or GIF here:

### Option 1: GIF Preview
```md
![Demo](assets/demo.gif)
````

### Option 2: YouTube or hosted video

[Watch Demo Video](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

---

## 2. Project Description

* Built a **real-time accident detection system** using TensorFlow/Keras CNN and OpenCV
* Integrated **automated email alerts (SMTP)** and **sound notifications**
* Included **time and location tagging** for emergency response
* **Tech Stack:** Python, TensorFlow, Keras, OpenCV, NumPy, winsound, Email API, geocoder, datetime

---

## 3. What is an Accident Detection System?

An Accident Detection System detects accidents via video or CCTV footage. Road accidents are a major global issue causing significant loss of life. This project explores how CCTV footage combined with Deep Learning can automatically detect accidents and enable faster emergency response.

---

## 4. Prerequisites

* Python >= 3.6
* Basic knowledge of Python scripting, Machine Learning, and Deep Learning
* Camera connected to your device (or a prerecorded video)

---

## 5. Getting Started

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

1. Train and generate model weights:

```bash
accident-classification.ipynb
```

This creates:

* `model.json`
* `model_weights.h5`

2. Run the main Python program:

```bash
python main.py
```

> ⚠️ **Note:** `model_weights.h5` is not included due to GitHub size limits. Run the notebook to generate it.

---

## 6. Description of Files

* `data/` – Kaggle dataset for accident detection from CCTV footage
* `accident-classification.ipynb` – Notebook to train the CNN model and generate `model.json` and `model_weights.h5`
* `detection.py` – Loads the trained model and performs accident detection
* `camera.py` – Captures video frames and displays accident probability in real time

---

## 7. Future Work

* Integrate automated emergency call alerts
* Estimate accident severity using advanced models
* Deploy on edge devices for real-time monitoring

---

## 8. Research Paper

You can link your ResearchGate paper or a PDF uploaded in your repo:

```md
[Read Our Research Paper]([https://www.researchgate.net/publication/YOUR_PAPER_ID](https://www.researchgate.net/publication/397173859_A_MINI_PROJECT_REPORT_ON_ACCIDENT_DETECTION_USING_AI))
```

Or, if uploading a PDF to `docs/` folder:

```md
[Download PDF](docs/Accident-Detection-Paper.pdf)
```

---

## 9. Contact / Support

* Author: Sowmya Reddy
* GitHub: [https://github.com/sowmyareddyy](https://github.com/sowmyareddyy)
* Email: [your-email@example.com](mailto:your-email@example.com)

---

```

### ✅ Notes for your repo:

1. **Video:** Convert demo clip to GIF for inline preview or link to YouTube.  
2. **Research paper:** Either link ResearchGate URL or include PDF in `docs/`.  
3. **Badges:** Already included; you can adjust versions if needed.  
4. **Screenshots:** Add images/GIFs in `assets/` and reference them in the README.  

---

If you want, I can also make a **slimmer, recruiter-friendly version** under 150–200 words that highlights **impact, tech stack, and results**, perfect for GitHub portfolios.  

Do you want me to do that next?
```

