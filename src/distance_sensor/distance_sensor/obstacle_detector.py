import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class ObstacleDetector(Node):

    def __init__(self):
        super().__init__('obstacle_detector')

        self.subscription = self.create_subscription(
            Float32,
            '/distance',
            self.distance_callback,
            10
        )

    def distance_callback(self, msg):
        distance = msg.data

        if distance > 1.0:
            status = 'SAFE'
        elif distance > 0.5:
            status = 'WARNING'
        else:
            status = 'STOP'

        self.get_logger().info(
            f'Distance: {distance:.2f} m → {status}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = ObstacleDetector()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
