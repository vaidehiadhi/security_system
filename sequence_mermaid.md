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