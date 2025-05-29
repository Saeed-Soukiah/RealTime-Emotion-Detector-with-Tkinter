# RealTime Emotion Detector With Tkinter

## Overview
RealTime-Emotion-Detector is a Python application that performs real-time facial emotion detection using your webcam. It leverages [OpenCV](https://opencv.org/), [FER (Facial Expression Recognition)](https://github.com/justinshenk/fer), and [Tkinter](https://docs.python.org/3/library/tkinter.html) for a graphical user interface. The program captures video from your webcam, detects faces, and annotates each face with the most probable emotion.

## Features
- **Live Video Feed:** Captures real-time video feed using OpenCV.
- **Facial Emotion Detection:** Uses the FER library to detect emotions on detected faces.
- **GUI Display:** Integrates with Tkinter to display the video feed with emotion annotations.
- **Optimized Processing:** Resizes frames for faster emotion detection.
- **Executable Conversion:** Instructions provided to convert the script to an executable for ease of use on Windows.

## Requirements
Before running the application, ensure you have the following Python packages installed:

- OpenCV-Python
- Pillow
- FER
- Tkinter (typically comes with Python installations)

Install the required packages using pip:

```bash
pip install opencv-python pillow fer
