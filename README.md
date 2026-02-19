# Form Detection Assistant 
A real-time Computer Vision application built with **Python**, **OpenCV**, and **MediaPipe** to track your workout form and automatically count your repetitions. This program calculates the exact joint angles of your arms to determine if you are doing a full range of motion.
Currently, the system supports tracking for Push-Ups, Left Bicep Curls, and Right Bicep Curls, complete with an interactive terminal menu and audio feedback for every successful rep!

## Key Features

* **Real-time Detections:** Detects range of motion in real time and instantly counts repetitions.
* **Automatic Counter:** The counted repetitions will be saved and displayed on the camera.
* **Improve the Form for Practice:** Calculate based on proximity in the form.
* **Multi-Exercise Tracking:** Choose between Push-Ups or Bicep Curls (Left/Right) via a clean terminal menu.
* **Audio Feedback:** Plays a "ding" sound automatically every time you complete a successful repetition.
  
## Screenshots

| Push Up | Left Bicep | Right Bicep |
| :---: | :---: | :---: |
| ![PU](./assets/Screenshot%20from%202026-01-23%2022-02-52.png) | ![Left B](./assets/Screenshot%20from%202026-01-23%2022-05-07.png) | ![Right B](./assets/Screenshot%20from%202026-01-23%2022-03-06.png) |

## Limitations

### 1. Need Distance from the Camera
   In order to get the appropriate calculations and measurements, it is necessary to provide a distance between the person and the camera.
### 2. Cannot detect other forms yet
   In the new development period there is push up and bicep curl detection (right/left).
### 3. Form change limitation on homepage
   Changing the form can only be done once, if you want to change the form you must stop the program first.
### 4. Library
To run this project, you need Python installed along with the following libraries:

* opencv-contrib-python
* numpy
* mediapipe==0.10.13

## Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/DNALWANA/Form-Detection-with-camera.git
    cd Form-Detection-with-camera
    ```

2.  **Install requirements**
    ```bash
    pip install -r requirement.txt
    ```

## Usage
```bash
python3 pttrainer.py
```

## How to run the program

### 1. Detection Object
Point the object in front of the camera and let the system detect it.
### 2. Stop Program
Press 'Q' to stop the program and let the system count the detected objects based on their classes.
### 3. Calculate the Object
Object count by class will appear in the terminal.


