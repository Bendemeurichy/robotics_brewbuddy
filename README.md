# robotics_brewbuddy
repo for robotics project that serves coffee to people in need of caffeination using turtlebot with ROS2

## Text-to-Speech
The `src/text_to_speech.py` file provides text-to-speech functionality using the Google Text-to-Speech API. This allows the robot to speak out messages.

### How to use
1. Install the `requests` library using pip:
   ```
   pip install requests
   ```
2. Use the `Assistant` class from the `src/text_to_speech.py` file to make the robot speak a given text.

Example:
```python
from src.text_to_speech import Assistant

settings = {
    "voice_speed": 0.5125,
    "voice_lang": "en-US",
    "voice_pitch": 1,
    "demonVoice": True
}

assistant = Assistant(settings)
assistant.welcome()
```
