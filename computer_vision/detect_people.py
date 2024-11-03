import tensorflow as tf
import numpy as np

# Load the pre-trained TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path="computer_vision/models/your_model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def detect_people(image):
    # Preprocess the image to fit the model input requirements
    input_shape = input_details[0]['shape']
    input_data = np.expand_dims(image, axis=0).astype(np.float32)

    # Set the tensor to point to the input data to be inferred
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Run the inference
    interpreter.invoke()

    # Get the results
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Process the results to extract coordinates of detected people
    detected_people = []
    for detection in output_data[0]:
        if detection[1] > 0.5:  # Confidence threshold
            detected_people.append(detection[2:6])  # Extract bounding box coordinates

    return detected_people
