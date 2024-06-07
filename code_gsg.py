"""
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

1. Ensure you have OpenCV installed (`pip3 install opencv-python`).
2. Run the script. The live feed will display on your screen.
3. Press 'q' to quit the application.
"""

import cv2
import datetime
import time

# Constants
SECONDS_TO_RECORD_AFTER_DETECTION = 5
FOURCC = cv2.VideoWriter_fourcc(*"mp4v") 

# Load Haarcascades
FACE_CASCADE = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
BODY_CASCADE = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

# Initialize variables
DETECTION = False
DETECTION_STOPPED_TIME = None
OUT = None
CAP = None


def start_recording(current_time):
    """
    Starts recording video when motion is detected.

    This function is called when motion is detected in the video stream.
    It creates a new video file with the specified filename based on the current timestamp.
    The video is recorded using the specified video codec (FOURCC) and frame rate.

    Args:
        current_time (str): The current timestamp formatted as a string, used as the video filename.

    Returns:
        None
    """
    global OUT, FRAME_WIDTH, FRAME_HEIGHT, CAP
    FRAME_WIDTH = int(CAP.get(3))
    FRAME_HEIGHT = int(CAP.get(4))
    OUT = cv2.VideoWriter(f"{current_time}.mp4", FOURCC, 20.0, (FRAME_WIDTH, FRAME_HEIGHT))
    print("Started Recording!")


def stop_recording():
    """
    Stops the video recording.

    This function is called when motion is no longer detected or when the specified duration
    after motion detection has passed. It releases the video writer object and prints a message
    indicating that the recording has stopped.

    Returns:
        None
    """
    global OUT
    if OUT is not None:
        OUT.release()
        OUT = None
        print("Stop Recording!")


def main():
    """
    Main function that runs the motion detection system.

    This function initializes the video capture device, loads the Haarcascades for face and body detection,
    and processes each frame of the video stream. It detects faces and bodies in the frames and starts
    recording video when motion is detected. The recording continues for a specified duration after the
    last motion detection. The function also draws rectangles around the detected faces in the video stream.

    Returns:
        None
    """
    global DETECTION, DETECTION_STOPPED_TIME, CAP

    # Open video capture device
    CAP = cv2.VideoCapture(0)

    # Check if camera opened successfully
    if not CAP.isOpened():
        print("Error opening video stream or file")
        return

    while CAP.isOpened():
        ret, frame = CAP.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces and bodies
            faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
            bodies = BODY_CASCADE.detectMultiScale(gray, 1.3, 5)

            # Handle detection events
            if len(faces) + len(bodies) > 0:
                if not DETECTION:
                    DETECTION = True
                    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                    start_recording(current_time)
            elif DETECTION:
                if DETECTION_STOPPED_TIME is not None:
                    if time.time() - DETECTION_STOPPED_TIME >= SECONDS_TO_RECORD_AFTER_DETECTION:
                        DETECTION = False
                        DETECTION_STOPPED_TIME = None
                        stop_recording()
                else:
                    DETECTION_STOPPED_TIME = time.time()

            # Record frames if detection is active
            if DETECTION:
                OUT.write(frame)

            # Draw rectangles around detected faces
            for (x, y, width, height) in faces:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

            cv2.imshow('Frame', frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        else:
            break

    # Release resources
    stop_recording()
    CAP.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()