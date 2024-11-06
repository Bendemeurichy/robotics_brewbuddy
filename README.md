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
## Speech-to-Text Functionality
This project includes a speech-to-text functionality that allows the robot to understand and respond to voice commands. The speech-to-text functionality is implemented using the `speech_recognition` library.

### Dependencies
To use the speech-to-text functionality, you need to install the following dependencies:
- `speech_recognition`

## People Detection using TensorFlow Lite

### Setup TensorFlow Lite

1. Install TensorFlow Lite:
   ```bash
   pip install tflite-runtime
   ```

2. Download the pre-trained TensorFlow Lite model and place it in the `computer_vision/models/` directory.

### Using the `detect_people.py` script

1. Ensure you have the necessary dependencies installed:
   ```bash
   pip install tensorflow numpy
   ```

2. Run the `detect_people.py` script with an input image:
   ```bash
   python computer_vision/detect_people.py --image path_to_your_image.jpg
   ```

3. The script will output the coordinates of detected people in the image.

## Conversation Generation using DialoGPT

### Setup DialoGPT

1. Install the necessary dependencies:
   ```bash
   pip install transformers torch
   ```

### Using the `conversation_generation.py` script

1. Run the `conversation_generation.py` script:
   ```bash
   python conversation_generation.py
   ```

2. The script will prompt you to enter a message, and it will generate a response using the DialoGPT model.

## Setting up the LLM Server

### Setup Flask and Run the Server

1. Install the necessary dependencies:
   ```bash
   pip install flask transformers torch
   ```

2. Run the `conversation_generation.py` script to start the server:
   ```bash
   python conversation_generation.py
   ```

3. The server will be running on `http://0.0.0.0:5000`.

## Using the new ROS2 node `llm_client.py`

### Setup and Run the ROS2 Node

1. Ensure you have the necessary dependencies installed:
   ```bash
   pip install requests
   ```

2. Build the ROS2 package:
   ```bash
   colcon build
   ```

3. Run the `llm_client` node:
   ```bash
   ros2 run robotics_brewbuddy llm_client
   ```

4. The node will subscribe to the `input_text` topic, send the input text to the LLM server, and publish the response to the `response_text` topic.
