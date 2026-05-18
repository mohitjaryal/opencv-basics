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
├── Basics/                              # Core OpenCV basic concepts
│   ├── basic.py                         # Reading and displaying images
│   ├── crop.py                          # Cropping images
│   ├── cropping_tool.py                 # Interactive cropping tool
│   ├── drawing_shapes.py                # Drawing shapes on images
│   ├── flip_image.py                    # Flipping images horizontally/vertically
│   ├── live_direct_drawing.py           # Live drawing on webcam feed
│   ├── nature_small.png                 # Sample image file
│   ├── playing_video.py                 # Playing video files
│   ├── record_video_using_webcam.py     # Recording video using webcam
│   ├── resize.py                        # Resizing images
│   ├── save_image.py                    # Saving images to disk
│   ├── streached_rectangle.py           # Drawing stretched rectangles
│   └── working_with_rgb.py             # Working with RGB color channels
│
├── Bitwise-Operations/                  # Bitwise logical operations on images
│   ├── bitwise_and.py                   # AND operation between two images
│   ├── bitwise_not.py                   # NOT (invert) operation on image
│   └── bitwise_or.py                    # OR operation between two images
│
├── Colors-Shape-Detection/              # Detecting colors and shapes
│   └── contours.py                      # Finding and drawing contours in images
│
├── Drawing/                             # Drawing with OpenCV
│   ├── addText.py                       # Adding text on images
│   ├── circle.py                        # Drawing circles
│   ├── line.py                          # Drawing lines
│   └── rectangle.py                     # Drawing rectangles
│
├── Edge-Detection-and-Thresholding/     # Edge detection and thresholding techniques
│   ├── CannyEdgeDetection.py            # Detecting edges using Canny algorithm
│   └── thresholding.py                  # Applying binary thresholding on images
│
├── Face-Object-Detection/               # Face, eye and smile detection system
│   ├── files/                           # Pre-trained Haar Cascade XML models
│   │   ├── haarcascade_eye.xml          # Pre-trained model for eye detection
│   │   ├── haarcascade_frontalcatface.xml  # Pre-trained model for face detection
│   │   └── haarcascade_smile.xml        # Pre-trained model for smile detection
│   └── face_detection.py               # Main script for face, eye & smile detection
│
├── Image-Filtering-Process/             # Applying filters to images
│   ├── Blur/                            # Blurring techniques
│   │   ├── gaussianBlur.py              # Applying Gaussian blur
│   │   └── meidanBlur.py               # Applying Median blur
│   └── Sharpening/                      # Sharpening techniques
│       └── basicSharpening.py           # Sharpening images using kernels
│
├── Practice-Questions/                  # Practice exercises
│   ├── gray_nature.png                  # Sample grayscale image for practice
│   ├── drawShapes.py                    # Practice drawing shapes
│   ├── flipImage.py                     # Practice flipping images
│   ├── practice.py                      # General practice file
│   ├── practice2.py                     # Advanced practice file
│   ├── rotateImage.py                   # Practice rotating images
│   └── videoCapture.py                  # Practice capturing video
│
├── Video-Processing-Workflow/           # Video processing concepts
│   ├── basic.py                         # Basic video processing operations
│   └── savingVideoFile.py              # Saving processed video to file
│
├── img/                                 # Images used throughout the project
├── LICENSE                              # MIT License
└── README.md                            # Project documentation
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

## 🧠 Concepts Covered

- ✅ Image I/O (read, display, save)
- ✅ Image transformations (resize, crop, flip, rotate)
- ✅ Drawing on images (shapes, text, overlays)
- ✅ Color channel manipulation (BGR / RGB)
- ✅ Bitwise operations (AND, OR, NOT)
- ✅ Contour detection and shape analysis
- ✅ Edge detection (Canny algorithm)
- ✅ Image thresholding (binary conversion)
- ✅ Image filtering (Gaussian Blur, Median Blur, Sharpening)
- ✅ Video playback and frame processing
- ✅ Webcam capture and video recording
- ✅ Mouse event handling for interactive tools
- ✅ Real-time drawing on live video feed
- ✅ Face, Eye & Smile detection (Haar Cascade)

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

*Made by [Mohit Jaryal*](https://mohitjaryal.online)
