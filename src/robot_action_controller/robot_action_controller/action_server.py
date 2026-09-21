import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from robot_interfaces.action import MoveRobot

import time


class MoveRobotServer(Node):
    def __init__(self):
        super().__init__('move_robot_server')

        self.action_server = ActionServer(
            self,
            MoveRobot,
            'move_robot',
            self.execute_callback
        )

    def execute_callback(self, goal_handle):
        target_distance = goal_handle.request.target_distance

        self.get_logger().info(
            f'Received goal: {target_distance:.2f} m'
        )

        current_distance = 0.0
        feedback_msg = MoveRobot.Feedback()

        while current_distance < target_distance:

            if goal_handle.is_cancel_requested:
                goal_handle.canceled()

                result = MoveRobot.Result()
                result.final_distance = current_distance

                self.get_logger().info('Goal canceled')

                return result

            current_distance += 0.5

            if current_distance > target_distance:
                current_distance = target_distance

            feedback_msg.current_distance = current_distance
            goal_handle.publish_feedback(feedback_msg)

            self.get_logger().info(
                f'Current distance: {current_distance:.2f} m'
            )

            time.sleep(1.0)

        goal_handle.succeed()

        result = MoveRobot.Result()
        result.final_distance = current_distance

        self.get_logger().info(
            f'Goal reached: {current_distance:.2f} m'
        )

        return result


def main(args=None):
    rclpy.init(args=args)

    move_robot_server = MoveRobotServer()

    rclpy.spin(move_robot_server)

    move_robot_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
