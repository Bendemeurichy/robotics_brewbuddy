import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from nav_msgs.msg import Path
from sensor_msgs.msg import LaserScan
import math

class Navigation(Node):

    def __init__(self):
        super().__init__('navigation')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            String,
            'people_detection',
            self.people_detection_callback,
            10)
        self.path_subscription = self.create_subscription(
            Path,
            'planned_path',
            self.path_callback,
            10)
        self.scan_subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback,
            10)
        self.current_path = None
        self.people_detected = False
        self.stop_distance = 1.0  # Distance to stop if people are detected

    def people_detection_callback(self, msg):
        if msg.data == "people_detected":
            self.people_detected = True
        else:
            self.people_detected = False

    def path_callback(self, msg):
        self.current_path = msg

    def scan_callback(self, msg):
        if self.people_detected:
            self.stop_robot()
        else:
            self.follow_path()

    def stop_robot(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher.publish(twist)

    def follow_path(self):
        if self.current_path is None:
            return

        # Simple path following logic
        for pose in self.current_path.poses:
            twist = Twist()
            twist.linear.x = 0.2  # Move forward
            twist.angular.z = 0.0  # No rotation
            self.publisher.publish(twist)
            rclpy.spin_once(self, timeout_sec=0.1)

def main(args=None):
    rclpy.init(args=args)
    node = Navigation()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
