import rclpy
from rclpy.node import Node
import speech_recognition as sr
from std_msgs.msg import String

class AudioProcessing(Node):

    def __init__(self):
        super().__init__('audio_processing')
        self.publisher_ = self.create_publisher(String, 'audio_text', 10)
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.timer = self.create_timer(5.0, self.timer_callback)

    def timer_callback(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            self.publisher_.publish(String(data=text))
            self.get_logger().info(f"Recognized text: {text}")
        except sr.UnknownValueError:
            self.get_logger().error("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            self.get_logger().error(f"Could not request results from Google Speech Recognition service; {e}")

def main(args=None):
    rclpy.init(args=args)
    node = AudioProcessing()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
