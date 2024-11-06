import requests
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LLMClient(Node):

    def __init__(self):
        super().__init__('llm_client')
        self.subscription = self.create_subscription(
            String,
            'input_text',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(String, 'response_text', 10)

    def listener_callback(self, msg):
        input_text = msg.data
        response_text = self.send_request_to_llm_server(input_text)
        self.publisher_.publish(String(data=response_text))

    def send_request_to_llm_server(self, input_text):
        url = 'http://<LLM_SERVER_IP>:5000/generate'
        payload = {'input_text': input_text}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get('response_text', '')
        else:
            self.get_logger().error(f"Failed to get response from LLM server: {response.status_code}")
            return ''

def main(args=None):
    rclpy.init(args=args)
    node = LLMClient()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
