import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class TeleopController(Node):

    def __init__(self):
        super().__init__('teleop_controller')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.get_logger().info(
            'Teleop controller started'
        )

    def send_command(self, linear, angular):

        msg = Twist()

        msg.linear.x = linear
        msg.angular.z = angular

        self.publisher.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    teleop_controller = TeleopController()

    while rclpy.ok():

        command = input(
            'Command [f/b/l/r/s]: '
        ).lower()

        if command == 'f':
            teleop_controller.send_command(0.5, 0.0)

        elif command == 'b':
            teleop_controller.send_command(-0.5, 0.0)

        elif command == 'l':
            teleop_controller.send_command(0.0, 1.0)

        elif command == 'r':
            teleop_controller.send_command(0.0, -1.0)

        elif command == 's':
            teleop_controller.send_command(0.0, 0.0)

        else:
            print('Unknown command')

    teleop_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
