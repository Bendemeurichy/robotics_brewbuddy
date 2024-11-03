# robotics_brewbuddy
repo for robotics project that serves coffee to people in need of caffeination using turtlebot with ROS2

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
