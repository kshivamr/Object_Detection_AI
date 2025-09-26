# Object_Detection_AI
A lightweight object detection AI using SSD MobileNet V3, trained on COCO dataset for 80 classes. Deployed on Raspberry Pi 4B (4GB) with Rev 1.3 webcam for real-time inference. Displays bounding boxes, labels, and scores on video feed. Perfect for IoT projects like smart cameras. FPS: 5-10. Built with TensorFlow and OpenCV.


# Object Detection Model on Raspberry Pi

This project implements a real-time object detection model using SSD MobileNet V3, fine-tuned on the COCO dataset. It runs on a Raspberry Pi 4B (4GB RAM) with a Rev 1.3 webcam, detecting common objects like people, cars, and animals via the camera feed. Ideal for edge AI applications like surveillance or robotics.

## Features
- Real-time object detection with bounding boxes and labels.
- Lightweight model (SSD MobileNet V3) optimized for low-power devices.
- Trained on COCO dataset (80 classes).
- Displays confidence scores for detections.
- Simple Python script for easy deployment.

## Prerequisites
- Raspberry Pi 4B with 4GB RAM.
- Raspberry Pi OS (or compatible Linux distro).
- Rev 1.3 webcam (or any USB webcam compatible with OpenCV).
- Python 3.7+ (RPi default works).
- Internet for initial setup (to install dependencies).

## Installation
1. Clone or download this project to your Raspberry Pi.
2. Set up a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install tensorflow opencv-python numpy picamera2  # If using Pi Camera; otherwise, skip picamera2
   ```
   - Note: For TensorFlow on RPi, use a pre-built wheel or install via `pip install tensorflow-aarch64` if on 64-bit OS.
4. Download the pre-trained SSD MobileNet V3 model from TensorFlow Model Garden or fine-tune on COCO if needed.

## Usage
1. Connect your webcam.
2. Run the script:
   ```
   python detect.py
   ```
3. The webcam feed will open with detected objects overlaid (bounding boxes, labels, scores).
4. Press 'q' to quit.
5. Customize thresholds or classes in the script as needed.

## Code Structure
- `detect.py`: Main script for loading the model, capturing video, and performing inference.
  - Uses TensorFlow for model loading and inference.
  - OpenCV for webcam access and visualization.

## Troubleshooting
- **Model Not Loading**: Ensure TensorFlow is installed correctly for ARM architecture.
- **Low FPS**: Reduce resolution in code (e.g., 320x240) for better performance on RPi.
- **Webcam Issues**: Test with `cv2.VideoCapture(0)`; adjust index if needed.
- **Overheating**: Use a heatsink or fan for prolonged use.

## Limitations
- Performance: ~5-10 FPS on RPi 4B due to hardware constraints.
- Accuracy: Dependent on lighting and object distance; COCO classes only.
- No multi-object tracking (just detection).

## Future Improvements
- Add post-processing for non-max suppression.
- Integrate with GPIO for hardware triggers.
- Fine-tune for custom datasets.

## License
MIT License.


