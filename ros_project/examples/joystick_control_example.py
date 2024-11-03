import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoystickControl(Node):

    def __init__(self):
        super().__init__('joystick_control')
        self.subscription = self.create_subscription(
            Joy,
            'joy',
            self.joy_callback,
            10)
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.linear_axis = 1
        self.angular_axis = 0
        self.linear_scale = 1.0
        self.angular_scale = 1.0

    def joy_callback(self, msg):
        twist = Twist()
        twist.linear.x = self.linear_scale * msg.axes[self.linear_axis]
        twist.angular.z = self.angular_scale * msg.axes[self.angular_axis]
        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = JoystickControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
