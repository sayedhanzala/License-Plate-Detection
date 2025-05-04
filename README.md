# 🚘 License Plate Detection & Recognition with YOLOv8 & EasyOCR

An end-to-end system for detecting and recognizing license plates using **YOLOv8** for object detection and **EasyOCR** for optical character recognition. This project enables real-time inference on videos and supports training on custom datasets.

---
# 📽️ Output Video

[![Video](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](assets/output.mp4)

---

## ✨ Features

- 🔍 **Accurate License Plate Detection** using a custom-trained YOLOv8 model  
- 🔠 **Text Extraction** with EasyOCR to recognize license plate numbers  
- 🎥 **Real-Time Video Processing** with OpenCV  
- 📁 **Custom Dataset Support** – easily train and evaluate on your own data  
- 🧪 **Experimentation Ready** – includes a Jupyter notebook for model training and evaluation

---

## 📁 Project Structure

```
├── assets/                         # Sample input videos
│   ├── a.mp4
│   ├── demo.mp4
│   └── ...
├── datasets/                       # Dataset directory
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   ├── val/
│   │   ├── images/
│   │   └── labels/
│   └── test/
├── runs/detect/train/weights/      # YOLOv8 trained weights
│   ├── best.pt
│   └── last.pt
├── main.py                         # Inference script (video-based)
├── data.yml                        # YOLO dataset configuration
├── LicensePlateDetection.ipynb     # Notebook for training & testing
└── README.md                       # Project documentation
```

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sayedhanzala/License-Plate-Detection
cd License_Plate_Detection/DL
```

### 2. Install Required Packages

Make sure you're using Python 3.8+.

```bash
pip install ultralytics opencv-python easyocr pytesseract numpy pillow
```

---

## 🧠 Train Your Own YOLOv8 Model (Optional)

If you want to train the model from scratch on your custom dataset:

```bash
yolo detect train data=data.yml model=yolov8n.pt epochs=30 imgsz=640 batch=16
```

- The best model weights will be saved at: `runs/detect/train/weights/best.pt`

---

## 🚀 Inference: Run LPR on a Video

By default, `main.py` uses `assets/a.mp4`. You can run it with:

```bash
python main.py
```

- Press `q` to quit the video window.
- The license plate detection and recognized text will be displayed on the video frames.

To use a different video, simply update the path in `main.py`:

```python
cap = cv2.VideoCapture("assets/your_video.mp4")
```

---

## 🧾 Dataset Format

- **Images** should be placed under:
  - `datasets/train/images/`
  - `datasets/val/images/`

- **Labels** in YOLO format go into:
  - `datasets/train/labels/`
  - `datasets/val/labels/`

- **Only one class** is used: `"license_plate"`

Example `data.yml`:

```yaml
train: ./datasets/train/images
val: ./datasets/val/images
nc: 1
names: ["license_plate"]
```

---

## 🔗 Dependencies

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)

---

## 🙌 Credits

- **YOLOv8** by Ultralytics  
- **EasyOCR** by JaidedAI  
- Project design and implementation by community contributors

---

## 📜 License

This project is intended for **educational and research purposes only**. Please refer to [YOLOv8](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) and [EasyOCR](https://github.com/JaidedAI/EasyOCR/blob/master/LICENSE) licenses before any commercial use.
