
# Security System with OpenCV

This Python script implements a motion detection system using OpenCV. It captures video from the default camera, detects faces and bodies using Haarcascades, and records video when motion is detected. The recording stops after a specified period of no motion detected and saves recored videos with the date and time.


## Documentation

This Python Script implements a motion detection system using OpenCV.
It captures video from the default camera, detects faces and bodies using Haarcascades,
and records video when motion is detected. The recording stops after a specified period
of no motion detected.

**Key Functionalities:**

* Accesses the default webcam.
* Employs Haarcascades for face and body detection.
* Initiates video recording upon detection and continues for a specified duration after the last detection.
* Displays a live feed with bounding boxes around detected faces.
* Allows for termination using the 'q' key.

**Limitations:**

* Relies on pre-trained Haarcascades, which might have limitations in accuracy and robustness.
* Records continuously upon detection, which could lead to large video files. More sophisticated motion detection could be implemented for efficiency.
* Lacks features like email or cloud storage integration for recordings.

**Usage:**

* Ensure you have OpenCV installed (`pip3 install opencv-python`).
* Run the script. The live feed will display on your screen.
* Press 'q' to quit the application.

**Sequence Diagram:**
```mermaid

sequenceDiagram
    participant User
    participant Security System
    participant Camera
    participant OpenCV
    participant DateTime
    participant face_cascade
    participant body_cascade

    User->>Security System: Activate
    activate Security System
    Security System->>User: Security System Activated
    Security System->>Camera: Start camera
    Camera-->>Security System: Camera started
    Camera->>Security System: Convert to Grayscale

    loop Detect Movement
        Security System->>OpenCV: Get frame
        OpenCV->>Camera: Read frame
        Camera-->>OpenCV: Frame data
        OpenCV-->>Security System: Processed frame
        Camera-->>face_cascade: Face detected
        Camera-->>body_cascade: Body detected
        OpenCV-->>Security System: Draw Rectangle box around face
    

        Security System->>face_cascade: Detect faces
        face_cascade-->>Security System: Face detection results

        Security System->>body_cascade: Detect bodies
        body_cascade-->>Security System: Body detection results

        alt Movement Detected
            Security System->>datetime: Get current time
            datetime-->>Security System: Current time
            Security System->>OpenCV: Start recording
            Security System->>User: Movement detected!
            Security System->>User: Starting recording...
            datetime->>User: Recording for {RECORDING_DURATION = 5} seconds
            loop Recording
                OpenCV->>Camera: Read frame
                Camera-->>OpenCV: Frame data
                OpenCV-->>Security System: Recorded frame
                Security System->>OpenCV: Write frame to video
            end
        else No Movement
            Security System->>User: No movement detected
        end
    end

    User->>Security System: Exit q key pressed
    Security System->>OpenCV: Stop recording
    Security System->>Camera: Stop camera
    Camera-->>Security System: Camera stopped
    deactivate Security System
```



## Installation

Clone the repository or download the script:

```bash
  git clone https://github.com/vaidehiadhi/security_system.git
```
Navigate to the project directory:
```bash
cd security_system
```
Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate
```
Install the required dependencies mentioned in the requirements.txt file 
```bash
pip install -r requirements.txt
```

    
## Usage

Run the script using the following command:
```bash
python security_system.py
```
The live feed will display on your screen, and recording will start when motion is detected.

Press 'q' to quit the application.


## Authors

- [@vaidehiadhi](https://www.github.com/vaidehiadhi)


## License

[MIT](https://choosealicense.com/licenses/mit/)

