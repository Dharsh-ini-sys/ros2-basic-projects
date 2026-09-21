import rclpy
from rclpy.node import Node

from calculator_interfaces.srv import AddTwoNumbers


class CalculatorClient(Node):
    def __init__(self):
        super().__init__('calculator_client')

        self.client = self.create_client(
            AddTwoNumbers,
            'add_two_numbers'
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Service not available, waiting again...'
            )

    def send_request(self, a, b):
        request = AddTwoNumbers.Request()
        request.a = a
        request.b = b

        future = self.client.call_async(request)

        return future


def main(args=None):
    rclpy.init(args=args)

    calculator_client = CalculatorClient()

    future = calculator_client.send_request(7.0, 5.0)

    rclpy.spin_until_future_complete(
        calculator_client,
        future
    )

    response = future.result()

    calculator_client.get_logger().info(
        f'{7.0} + {5.0} = {response.sum}'
    )

    calculator_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
