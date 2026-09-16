import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class TemperatureSensor(Node):

    def __init__(self):
        super().__init__('temp_sensor')

        self.publisher = self.create_publisher(
            Float32,
            'temperature',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_temperature
        )

        self.temperature = 25.0

    def publish_temperature(self):

        self.temperature += random.uniform(-0.5, 0.8)

        msg = Float32()
        msg.data = self.temperature

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Temperature: {self.temperature:.2f} °C'
        )


def main(args=None):

    rclpy.init(args=args)

    node = TemperatureSensor()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()