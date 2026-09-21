import rclpy
from rclpy.node import Node

from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster


class TfBroadcaster(Node):
    def __init__(self):
        super().__init__('tf_broadcaster')

        self.broadcaster = TransformBroadcaster(self)

        self.x = 0.0

        self.timer = self.create_timer(
            1.0,
            self.broadcast_transform
        )

    def broadcast_transform(self):
        transform = TransformStamped()

        transform.header.stamp = self.get_clock().now().to_msg()

        transform.header.frame_id = 'odom'
        transform.child_frame_id = 'base_link'

        transform.transform.translation.x = self.x
        transform.transform.translation.y = 0.0
        transform.transform.translation.z = 0.0

        transform.transform.rotation.x = 0.0
        transform.transform.rotation.y = 0.0
        transform.transform.rotation.z = 0.0
        transform.transform.rotation.w = 1.0

        self.broadcaster.sendTransform(transform)

        self.get_logger().info(
            f'Robot position: x = {self.x:.2f} m'
        )

        self.x += 0.2


def main(args=None):
    rclpy.init(args=args)

    tf_broadcaster = TfBroadcaster()

    rclpy.spin(tf_broadcaster)

    tf_broadcaster.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
