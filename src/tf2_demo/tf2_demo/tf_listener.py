import rclpy
from rclpy.node import Node
from rclpy.time import Time

from tf2_ros import Buffer
from tf2_ros import TransformListener
from tf2_ros import TransformException


class TfListener(Node):
    def __init__(self):
        super().__init__('tf_listener')

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(
            self.tf_buffer,
            self
        )

        self.timer = self.create_timer(
            1.0,
            self.get_transform
        )

    def get_transform(self):
        try:
            transform = self.tf_buffer.lookup_transform(
                'odom',
                'base_link',
                Time()
            )

            x = transform.transform.translation.x
            y = transform.transform.translation.y
            z = transform.transform.translation.z

            self.get_logger().info(
                f'Robot position: '
                f'x={x:.2f} m, '
                f'y={y:.2f} m, '
                f'z={z:.2f} m'
            )

        except TransformException as ex:
            self.get_logger().warn(
                f'Could not get transform: {ex}'
            )


def main(args=None):
    rclpy.init(args=args)

    tf_listener = TfListener()

    rclpy.spin(tf_listener)

    tf_listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

