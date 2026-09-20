import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class DistanceSensor(Node):

    def __init__(self):
        super().__init__('distance_sensor')

        self.publisher = self.create_publisher(
            Float32,
            '/distance',
            10
        )

        self.distance = 2.5

        self.timer = self.create_timer(
            1.0,
            self.publish_distance
        )

    def publish_distance(self):
        msg = Float32()
        msg.data = self.distance

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Distance: {self.distance:.2f} m'
        )

        self.distance -= 0.2

        if self.distance < 0.1:
            self.distance = 2.5


def main(args=None):
    rclpy.init(args=args)

    node = DistanceSensor()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
