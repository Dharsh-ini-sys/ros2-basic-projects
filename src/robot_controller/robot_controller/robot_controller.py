import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32


class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')

        self.declare_parameter('warning_distance', 1.0)
        self.declare_parameter('stop_distance', 0.5)

        self.subscription = self.create_subscription(
            Float32,
            '/distance',
            self.distance_callback,
            10
        )

    def distance_callback(self, msg):
        distance = msg.data

        warning_distance = self.get_parameter(
            'warning_distance'
        ).value

        stop_distance = self.get_parameter(
            'stop_distance'
        ).value

        if distance > warning_distance:
            status = 'SAFE'
        elif distance > stop_distance:
            status = 'WARNING'
        else:
            status = 'STOP'

        self.get_logger().info(
            f'Distance: {distance:.2f} m | Status: {status}'
        )


def main(args=None):
    rclpy.init(args=args)

    robot_controller = RobotController()

    rclpy.spin(robot_controller)

    robot_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
