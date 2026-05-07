# oaqjp-final-project-emb-ai

## Emotion Detector - AI-Based Web Application

This project implements an AI-based emotion detection web application using the Watson NLP library and Flask.

### Project Overview

The Emotion Detector analyzes text input and returns emotion scores for the following emotions:
- Anger
- Disgust
- Fear
- Joy
- Sadness

It also identifies the dominant emotion from the analysis.

### Project Structure
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── init.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── README.md
### Requirements

- Python 3.x
- Flask
- Requests
- PyLint

### Setup & Run

```bash
pip install flask requests
python server.py
```

### Running Unit Tests

```bash
python -m pytest test_emotion_detection.py -v
```

### Static Code Analysis

```bash
pylint server.py
```
