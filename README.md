# 🖼️ OpenCV Basics

> A beginner-friendly collection of Python scripts covering the core fundamentals of **OpenCV** — from reading images to live drawing on webcam feed.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv&logoColor=white)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Portfolio](https://img.shields.io/badge/Portfolio-mohitjaryal.online-orange)](https://mohitjaryal.online/)

---

## 📁 Project Structure

```
opencv-basics/
│
├── basic.py                  # Reading, displaying & saving images
├── save_image.py             # Saving processed images to disk
├── resize.py                 # Resizing images
├── crop.py                   # Cropping a region from an image
├── cropping_tool.py          # Interactive mouse-based cropping tool
├── flip_image.py             # Flipping images (horizontal / vertical / both)
├── drawing_shapes.py         # Drawing lines, circles, rectangles & text
├── streached_rectangle.py    # Drawing stretched/custom rectangles
├── working_with_rgb.py       # Exploring and manipulating color channels
├── playing_video.py          # Playing a video file using OpenCV
├── record_video_using_webcam.py  # Recording video from webcam
├── live_direct_drawing.py    # Drawing on live webcam feed in real-time
│
└── nature_small.png          # Sample image used across scripts
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed, then install the required libraries:

```bash
pip install opencv-python numpy
```

### Clone the Repository

```bash
git clone https://github.com/mohitjaryal/opencv-basics.git
cd opencv-basics
```

### Run Any Script

```bash
python gaussianBlur.py
python cropping_tool.py
python live_direct_drawing.py
# ...and so on
```

---

## 📜 Script Descriptions

| Script | Description |
|---|---|
| `basic.py` | Load and display an image using `cv2.imread` and `cv2.imshow` |
| `save_image.py` | Save a modified image to disk using `cv2.imwrite` |
| `resize.py` | Resize images to custom dimensions |
| `crop.py` | Crop a specific region using NumPy slicing |
| `cropping_tool.py` | Interactive tool — drag to select and crop a region |
| `flip_image.py` | Flip images along horizontal, vertical, or both axes |
| `drawing_shapes.py` | Draw lines, rectangles, circles, and add text overlays |
| `streached_rectangle.py` | Draw filled or stretched rectangles for custom overlays |
| `working_with_rgb.py` | Split and visualize individual RGB/BGR color channels |
| `playing_video.py` | Read and play a video file frame-by-frame |
| `record_video_using_webcam.py` | Capture and save video from your webcam |
| `live_direct_drawing.py` | Draw shapes in real-time on a live webcam stream |

---

## 🧠 Concepts Covered

- ✅ Image I/O (read, display, save)
- ✅ Image transformations (resize, crop, flip)
- ✅ Drawing on images (shapes, text, overlays)
- ✅ Color channel manipulation (BGR / RGB)
- ✅ Video playback and frame processing
- ✅ Webcam capture and video recording
- ✅ Mouse event handling for interactive tools
- ✅ Real-time drawing on live video feed

---

## 🛠️ Built With

- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)

---

## 📬 Connect with Me

| Platform | Link |
| --- | --- |
| 🌐 Website | [mohitjaryal.online](https://mohitjaryal.online) |
| 💼 LinkedIn | [in/mohitjaryal](https://www.linkedin.com/in/mohitjaryal) |
| 🐦 Twitter/X | [@mohitjaryal04](https://x.com/mohitjaryal04) |
| 💻 GitHub | [mohitjaryal](https://github.com/mohitjaryal) |
| 🧩 LeetCode | [mohitjaryal](https://leetcode.com/u/mohitjaryal) |
| 🧩 HackerRank | [mohitjaryal](https://hackerrank.com/u/mohitjaryal) |

---

**⭐ If this repo helped you, consider giving it a star — it motivates me to keep learning and sharing!**

*Made with 💙 by [Mohit Jaryal*](https://mohitjaryal.online)
