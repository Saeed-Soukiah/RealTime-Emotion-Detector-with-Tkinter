"""
Author: Saeed Soukiah
Date: 2025-05-29
Description: Facial Emotion Detection using OpenCV, FER, and Tkinter.
"""
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from fer import FER

# Initialize the emotion detector
emotion_detector = FER()

# Start the webcam feed (default camera index 0)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Define a scale factor to resize the frame for faster processing
scale_factor = 0.5

# Create the main Tkinter window
root = tk.Tk()
root.title("Facial Emotion Detection")

# Create a label widget to display our video frames
video_label = tk.Label(root)
video_label.pack()

def update_frame():
    """Capture frames from the webcam, process them and update the Tkinter label."""
    ret, frame = cap.read()
    if not ret:
        print("Error reading frame")
        video_label.after(10, update_frame)
        return

    # Resize the frame for faster emotion detection
    small_frame = cv2.resize(frame, (0, 0), fx=scale_factor, fy=scale_factor)

    # Detect emotions on the resized (small) frame
    emotions = emotion_detector.detect_emotions(small_frame)

    # Loop through the detected emotions/faces and annotate the frame
    for emotion_data in emotions:
        # Get the emotion with the highest confidence
        highest_confidence_emotion = max(emotion_data["emotions"], key=emotion_data["emotions"].get)
        # Unpack bounding box (x, y, width, height) from the detection (coordinates at the scaled image)
        (x, y, w, h) = emotion_data["box"]

        # Scale the coordinates back to the original frame dimensions
        x = int(x / scale_factor)
        y = int(y / scale_factor)
        w = int(w / scale_factor)
        h = int(h / scale_factor)

        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Place the emotion label above the rectangle
        cv2.putText(frame, highest_confidence_emotion, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Convert the frame from BGR (OpenCV format) to RGB (Tkinter/PIL format)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Convert the frame to a PIL Image
    img = Image.fromarray(frame_rgb)
    # Convert the PIL Image to ImageTk format
    imgtk = ImageTk.PhotoImage(image=img)

    # Update the Tkinter label with the new image
    video_label.imgtk = imgtk  # Keep a reference to avoid garbage collection
    video_label.configure(image=imgtk)

    # Schedule the next frame update
    video_label.after(10, update_frame)

def on_closing():
    """Handle the closing of the application window."""
    cap.release()  # Release the video capture
    root.destroy()  # Destroy the Tkinter window

# Set the protocol for closing the window
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start updating frames
update_frame()

# Start the Tkinter event loop
root.mainloop()
