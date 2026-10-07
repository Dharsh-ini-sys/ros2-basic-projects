import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan

import math


class ObstacleAnalyzer(Node):

    def __init__(self):
        super().__init__('obstacle_analyzer')

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

    def scan_callback(self, msg):

        front_distances = []
        left_distances = []
        right_distances = []

        for i, distance in enumerate(msg.ranges):

            angle = msg.angle_min + i * msg.angle_increment

            angle_degrees = math.degrees(angle)

            if -10 <= angle_degrees <= 10:
                front_distances.append(distance)

            elif 80 <= angle_degrees <= 100:
                left_distances.append(distance)

            elif -100 <= angle_degrees <= -80:
                right_distances.append(distance)

        front = min(front_distances)
        left = min(left_distances)
        right = min(right_distances)

        self.get_logger().info(
            f'Front: {front:.2f} m | '
            f'Left: {left:.2f} m | '
            f'Right: {right:.2f} m'
        )


def main(args=None):

    rclpy.init(args=args)

    obstacle_analyzer = ObstacleAnalyzer()

    rclpy.spin(obstacle_analyzer)

    obstacle_analyzer.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
