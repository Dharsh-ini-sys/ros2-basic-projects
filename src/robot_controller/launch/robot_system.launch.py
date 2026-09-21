from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='distance_sensor',
            executable='distance_sensor',
            name='distance_sensor'
        ),

        Node(
            package='robot_controller',
            executable='robot_controller',
            name='robot_controller'
        )
    ])
