```mermaid

graph LR
    A[Start] --> B{Open Camera}
    B -->|Failed| C[Error]
    B -->|Opened| D{Capture Frame}
    D --> E{Convert to Grayscale}
    E --> F{Detect Faces and Bodies}
    F -->|No Detection| G{Wait for 5 seconds}
    G --> D
    F -->|Detection| H{Detection}
    H --> I{Is Detection Ongoing?}
    I -->|No| J[Start Recording Timer]
    J --> K[Record for SECONDS_TO_RECORD_AFTER_DETECTION = 5 seconds]
    K --> D
    I -->|Yes| L[Reset Timer]
    L --> H
    D --> M{Display Frame}
    M --> N{Exit q key pressed}
    N -->|Yes| O[End]
    N -->|No| D