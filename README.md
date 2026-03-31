# 🦺 Smart PPE Detection System using YOLOv8

## 📌 Description

The Smart PPE Detection System is a computer vision-based project that detects whether workers are wearing Personal Protective Equipment (PPE) such as helmets and safety vests.

This system uses the YOLOv8 object detection model to identify people and safety gear in images. It aims to improve safety compliance in environments like construction sites where accidents can occur if proper protective equipment is not used.

This project focuses on applying a pre-trained model to a real-world problem rather than training a model from scratch.

---

## 🎯 Problem Statement

On construction sites, workers often fail to follow safety rules like wearing helmets and vests, which increases the risk of accidents.

---

## 💡 Solution

This project provides an automated solution that:

* Detects people in images
* Identifies safety helmets and vests
* Displays results using bounding boxes

This helps in quickly checking whether safety guidelines are being followed.

---

## 🚀 Features

* Object detection using YOLOv8
* Detects humans and PPE
* Displays output with bounding boxes
* Easy to use and understand
* Works on input images

---

## 🛠️ Tech Stack

* Python
* OpenCV
* Ultralytics YOLOv8
* NumPy

---

## 📂 Project Structure

```id="t5zj4x"
Smart_PPE_Detection_system_using_YOLOv8/
│
├── assets/
├── data/
├── models/
├── output/
├── results/
├── src/
│   └── main.py
│
├── screenshots/
├── Project_Report.pdf
├── README.md
```

---

## ⚙️ Installation

Follow these steps to run the project:

```bash id="4d6m0m"
git clone https://github.com/your-username/Smart_PPE_Detection_system_using_YOLOv8.git
cd Smart_PPE_Detection_system_using_YOLOv8
pip install ultralytics opencv-python numpy
```

---

## ▶️ Usage

```bash id="d6p7qz"
python src/main.py
```

* Make sure to update the input image path inside the code
* The output will display detected objects with bounding boxes

---

## 📄 Project Report

📥 Download the full report here:
👉 [Click to View Report](./Project_Report.pdf)

---

## ⚠️ Challenges Faced

* Installing and setting up required libraries
* Understanding YOLOv8 usage
* Debugging runtime errors
* Managing file paths

---

## 📚 Key Learnings

* Understanding object detection in real-world applications
* Using pre-trained models effectively
* Applying computer vision to solve practical problems
* Using OpenCV for visualization

---

## 🔮 Future Scope

* Extend to real-time video detection
* Improve accuracy with custom training
* Detect additional safety equipment
* Deploy as a real-time monitoring system

---

## 👤 Author

**Tanya Chandrakar**
Computer Vision BYOP Project

---

## 📚 References

* Ultralytics YOLOv8 Documentation
* OpenCV Documentation
* Online resources related to PPE detection

---

## ⭐ Acknowledgement

This project was developed as part of the Computer Vision BYOP course to apply AI concepts to real-world problems.
