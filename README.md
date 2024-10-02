# AgeEye
AgeEye leverages deep learning for real-time age detection. Utilizing advanced techniques, including FaceMaskNet-9, this project accurately estimates age even with face masks. Ideal for retail environments, it enhances compliance with age restrictions, optimizing user experience while ensuring safety and privacy.
# AgeEye - Intelligent Age Detection System

AgeEye is an intelligent age verification system utilizing the **DeepFace** library for real-time age estimation from facial images. The system uses OpenCV for face detection and integrates with deep learning techniques to ensure accurate and real-time age detection, even in challenging scenarios like partial facial occlusion (e.g., masks).

## Features

- **Real-time Face Detection**: Utilizes Haar Cascade Classifier to detect faces from live webcam feed.
- **Age Estimation**: Leverages DeepFace to analyze facial features and estimate the age of the detected individual.
- **Scalability**: Easily extendable for additional features, such as gender detection or emotion analysis, using DeepFace's multi-function capabilities.

## Technologies Used

- **Python**: Core language used for implementation.
- **OpenCV**: Used for video capture and face detection.
- **DeepFace**: For deep learning-based age estimation.
- **Haar Cascade Classifier**: Utilized for efficient face detection from the webcam input.

## Setup & Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/AgeEye.git
   cd AgeEye


