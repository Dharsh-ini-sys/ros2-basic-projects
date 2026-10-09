from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    # Path to the robot URDF
    urdf_file = os.path.join(
        get_package_share_directory('urdf_demo'),
        'urdf',
        'robot.urdf'
    )

    # Path to the LiDAR test world
    world_file = os.path.join(
        get_package_share_directory('urdf_demo'),
        'worlds',
        'lidar_test.world'
    )

    # Read the robot URDF
    with open(urdf_file, 'r') as file:
        robot_description = file.read()

    return LaunchDescription([

        # Start Gazebo with our custom world
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    '/opt/ros/humble/share/gazebo_ros/launch',
                    'gazebo.launch.py'
                )
            ),
            launch_arguments={
                'world': world_file
            }.items()
        ),

        # Publish robot description and TF
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[
                {'robot_description': robot_description, 'use_sim_time': True}
            ],
            output='screen'
        ),

        # Wait for Gazebo to start, then spawn the robot
        TimerAction(
            period=3.0,
            actions=[
                Node(
                    package='gazebo_ros',
                    executable='spawn_entity.py',
                    arguments=[
                        '-entity', 'my_robot',
                        '-topic', 'robot_description'
                    ],
                    output='screen'
                )
            ]
        )

    ])
