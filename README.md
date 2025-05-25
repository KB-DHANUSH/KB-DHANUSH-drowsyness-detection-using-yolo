# 💤 Drowsiness Detection with YOLOv8 & OpenCV

This project is a real-time **Drowsiness Detection System** using a custom-trained YOLOv8 model and your webcam. It helps detect signs of drowsiness or closed eyes, which can be useful in driver monitoring systems or fatigue analysis tools.

## 🔧 Features

* Live webcam feed with real-time detection
* Custom-trained YOLOv8 model (`best.pt`)
* Visual feedback with bounding boxes
* Press `q` to quit the program

## 📦 Requirements

Make sure you have the following Python packages installed:

```bash
pip install ultralytics opencv-python
```

> 💡 `ultralytics` is the official YOLOv8 library.

## 🧠 Model

The model used is `best.pt`, which is a YOLOv8 model trained to detect drowsiness (e.g., closed eyes, yawning).
Place the file in the root directory of the project.

## 📸 How It Works

1. The webcam captures frames.
2. The model predicts drowsiness indicators.
3. Bounding boxes and labels are drawn on the frame.
4. The frame is displayed in real-time.
5. Press `q` to exit.

## 🧾 Code Overview

```python
from ultralytics import YOLO
import cv2

model = YOLO('best.pt')        # Load the trained model
cap = cv2.VideoCapture(0)      # Start the webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)                 # Predict
    annotated_frame = results[0].plot()    # Draw results
    cv2.imshow('YOLOv8 Webcam Detection', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q'
        break

cap.release()
cv2.destroyAllWindows()
```

## 📁 Folder Structure

```
.
├── best.pt               # Your trained model
├── detect.py             # Detection script
├── README.md             # This file
```

## 🚀 Getting Started

To run the detection:

```bash
python detect.py
```

Make sure your webcam is connected and `best.pt` is in the correct location.

## 📌 Notes

* You can train your own model using Ultralytics' YOLOv8 training tools.
* Model accuracy depends on training data quality.

## 📄 License

MIT License
