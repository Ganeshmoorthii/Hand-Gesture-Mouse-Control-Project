# Hand Gesture Mouse Control

This project uses Python, OpenCV, MediaPipe, and PyAutoGUI to control the mouse using hand gestures detected by a webcam.

## Project Overview

The hand gestures are recognized using **MediaPipe**, and the mouse movement is controlled with **PyAutoGUI**. The project leverages the real-time video feed from the webcam to capture hand landmarks and map the movement of specific fingers to the mouse pointer.

### Key Features:
- **Move the mouse pointer** using your index finger.
- **Click the mouse** when the distance between the index finger and thumb is small (indicating a click gesture).
- Works in real-time using the webcam feed.

## Requirements

Install the following libraries before running the project:

```bash
pip install opencv-python mediapipe pyautogui

## How It Works

1. The webcam captures the video feed.
2. **MediaPipe** processes the video to detect hand landmarks.
3. The tip of the index finger controls the mouse movement.
4. A click action is triggered when the distance between the index finger and thumb becomes small.

## Code Explanation

```python
import cv2
import mediapipe
import pyautogui
