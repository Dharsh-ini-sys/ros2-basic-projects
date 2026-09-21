import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from robot_interfaces.action import MoveRobot


class MoveRobotClient(Node):
    def __init__(self):
        super().__init__('move_robot_client')

        self.action_client = ActionClient(
            self,
            MoveRobot,
            'move_robot'
        )

    def send_goal(self, target_distance):
        goal_msg = MoveRobot.Goal()
        goal_msg.target_distance = target_distance

        self.action_client.wait_for_server()

        self.get_logger().info(
            f'Sending goal: {target_distance:.2f} m'
        )

        future = self.action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )

        future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')

        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(
            self.result_callback
        )

    def feedback_callback(self, feedback_msg):
        current_distance = feedback_msg.feedback.current_distance

        self.get_logger().info(
            f'Feedback: {current_distance:.2f} m'
        )

    def result_callback(self, future):
        result = future.result().result

        self.get_logger().info(
            f'Result: {result.final_distance:.2f} m'
        )

        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)

    move_robot_client = MoveRobotClient()

    move_robot_client.send_goal(5.0)

    rclpy.spin(move_robot_client)


if __name__ == '__main__':
    main()
