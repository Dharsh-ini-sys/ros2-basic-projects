import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TransformStamped

from tf2_ros import TransformBroadcaster

import math


class RobotSimulator(Node):

    def __init__(self):
        super().__init__('robot_simulator')

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        self.linear_velocity = 0.0
        self.angular_velocity = 0.0

        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.velocity_callback,
            10
        )

        self.broadcaster = TransformBroadcaster(self)

        self.timer = self.create_timer(
            0.1,
            self.update_robot
        )

    def velocity_callback(self, msg):

        self.linear_velocity = msg.linear.x
        self.angular_velocity = msg.angular.z

    def update_robot(self):

        dt = 0.1

        self.x += (
            self.linear_velocity
            * math.cos(self.theta)
            * dt
        )

        self.y += (
            self.linear_velocity
            * math.sin(self.theta)
            * dt
        )

        self.theta += self.angular_velocity * dt

        transform = TransformStamped()

        transform.header.stamp = self.get_clock().now().to_msg()

        transform.header.frame_id = 'odom'
        transform.child_frame_id = 'base_link'

        transform.transform.translation.x = self.x
        transform.transform.translation.y = self.y
        transform.transform.translation.z = 0.0

        transform.transform.rotation.z = math.sin(
            self.theta / 2
        )

        transform.transform.rotation.w = math.cos(
            self.theta / 2
        )

        self.broadcaster.sendTransform(transform)

        self.get_logger().info(
            f'Position: x={self.x:.2f} m, '
            f'y={self.y:.2f} m, '
            f'theta={math.degrees(self.theta):.1f}°'
        )


def main(args=None):

    rclpy.init(args=args)

    robot_simulator = RobotSimulator()

    rclpy.spin(robot_simulator)

    robot_simulator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
