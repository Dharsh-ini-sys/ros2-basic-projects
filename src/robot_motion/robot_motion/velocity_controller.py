import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class VelocityController(Node):

    def __init__(self):
        super().__init__('velocity_controller')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_velocity
        )

    def publish_velocity(self):

        msg = Twist()

        msg.linear.x = 0.5
        msg.linear.y = 0.0
        msg.linear.z = 0.0

        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0

        self.publisher.publish(msg)

        self.get_logger().info(
            'Moving forward at 0.5 m/s'
        )


def main(args=None):

    rclpy.init(args=args)

    velocity_controller = VelocityController()

    rclpy.spin(velocity_controller)

    velocity_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
