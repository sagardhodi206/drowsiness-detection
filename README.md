# 😴 Drowsiness Detection using AI

A real-time **Drowsiness Detection System** built using **Python, OpenCV, and Computer Vision**. The system monitors a person's eyes through a webcam and detects signs of drowsiness.

## 🚀 Features

* 🎥 Real-time webcam monitoring
* 👁️ Eye detection and monitoring
* 😴 Drowsiness detection
* 🔔 Alert when drowsiness is detected
* ⚡ Real-time video processing
* 🤖 Computer Vision based system

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

## 📁 Project Structure

```text id="m2y5f1"
drowsiness-detection/
│
├── app.py
├── requirements.txt
└── README.md
```

## 📦 Installation

### 1. Clone the Repository

```bash id="lq0z7k"
git clone https://github.com/sagardhodi206/drowsiness-detection.git
```

### 2. Open the Project Folder

```bash id="9h0f7e"
cd drowsiness-detection
```

### 3. Install Required Libraries

```bash id="u2q6u5"
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the required libraries manually:

```bash id="nd6k2a"
pip install opencv-python mediapipe numpy
```

## ▶️ Run the Project

Start the application using:

```bash id="xg8e1x"
python app.py
```

The webcam will open and the system will start monitoring the user's eyes.

## 🔄 How It Works

```text id="i8p6wq"
Webcam
   ↓
Capture Video Frame
   ↓
Face Detection
   ↓
Eye Detection
   ↓
Monitor Eye State
   ↓
Detect Drowsiness
   ↓
Trigger Alert
```

## 🧠 Detection Logic

The system continuously monitors the user's eye state through the webcam.

When the system detects prolonged signs of closed or inactive eyes, it identifies a possible drowsiness state and activates an alert.

## 🎯 Applications

This project demonstrates applications of:

* Computer Vision
* Face and Eye Tracking
* Real-time AI
* Human Monitoring Systems
* Driver Safety Technology

Possible applications include:

* 🚗 Driver monitoring
* 🏭 Industrial safety
* 🖥️ Workstation monitoring
* 🛡️ Safety assistance systems

> **Note:** This project is a demonstration/educational system and should not be relied upon as the sole safety mechanism in real-world situations.

## 🔮 Future Improvements

* Improve detection accuracy
* Add head-pose estimation
* Add yawning detection
* Add multiple alert levels
* Add event logging
* Add dashboard for monitoring
* Integrate with IoT alert systems

## 👨‍💻 Author

**Sagar Dhodi**

GitHub:
https://github.com/sagardhodi206

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.