import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class TemperatureMonitor(Node):

    def __init__(self):
        super().__init__('temperature_monitor')

        self.subscription = self.create_subscription(
            Float32,
            'temperature',
            self.temperature_callback,
            10
        )

    def temperature_callback(self, msg):

        temperature = msg.data

        if temperature >= 30.0:
            status = 'WARNING'
        else:
            status = 'NORMAL'

        self.get_logger().info(
            f'Temperature: {temperature:.2f} °C | Status: {status}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = TemperatureMonitor()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()