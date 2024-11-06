import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from textblob import TextBlob

class SentimentAnalysis(Node):

    def __init__(self):
        super().__init__('sentiment_analysis')
        self.subscription = self.create_subscription(
            String,
            'audio_text',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(String, 'sentiment_result', 10)

    def listener_callback(self, msg):
        text = msg.data
        sentiment = self.analyze_sentiment(text)
        self.publisher_.publish(String(data=sentiment))
        self.get_logger().info(f"Sentiment result: {sentiment}")

    def analyze_sentiment(self, text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity < 0:
            return 'sad'
        elif 'tired' in text.lower():
            return 'tired'
        else:
            return 'neutral'

def main(args=None):
    rclpy.init(args=args)
    node = SentimentAnalysis()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
