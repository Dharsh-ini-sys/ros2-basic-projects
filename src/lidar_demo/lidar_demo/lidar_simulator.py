import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan

import math


class LidarSimulator(Node):

    def __init__(self):
        super().__init__('lidar_simulator')

        self.publisher = self.create_publisher(
            LaserScan,
            '/scan',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_scan
        )

    def publish_scan(self):

        scan = LaserScan()

        scan.header.stamp = self.get_clock().now().to_msg()
        scan.header.frame_id = 'laser_frame'

        scan.angle_min = -math.pi
        scan.angle_max = math.pi
        scan.angle_increment = math.radians(1)

        scan.range_min = 0.1
        scan.range_max = 10.0

        scan.ranges = [10.0] * 360

        # Front obstacle: 2 meters
        for i in range(175, 186):
            scan.ranges[i] = 2.0

        # Left obstacle: 1 meter
        for i in range(265, 276):
            scan.ranges[i] = 1.0

        # Right obstacle: 1.5 meters
        for i in range(85, 96):
            scan.ranges[i] = 1.5

        self.publisher.publish(scan)

        self.get_logger().info(
            'Published simulated LiDAR scan'
        )


def main(args=None):

    rclpy.init(args=args)

    lidar_simulator = LidarSimulator()

    rclpy.spin(lidar_simulator)

    lidar_simulator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

