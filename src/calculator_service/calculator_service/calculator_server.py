import rclpy
from rclpy.node import Node

from calculator_interfaces.srv import AddTwoNumbers


class CalculatorServer(Node):
    def __init__(self):
        super().__init__('calculator_server')

        self.service = self.create_service(
            AddTwoNumbers,
            'add_two_numbers',
            self.add_two_numbers_callback
        )

    def add_two_numbers_callback(self, request, response):
        response.sum = request.a + request.b
        return response


def main(args=None):
    rclpy.init(args=args)

    calculator_server = CalculatorServer()

    rclpy.spin(calculator_server)

    calculator_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
