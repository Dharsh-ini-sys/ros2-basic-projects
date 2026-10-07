# ROS 2 Basic Projects

A collection of beginner ROS 2 projects built while learning robotics and automation.

## Projects

### Project 1 — Simulated Temperature Monitor 🌡️

A simulated temperature sensor publishes temperature data, and a monitor node subscribes to it and classifies the temperature as NORMAL or WARNING.

**ROS concepts:**
- Nodes
- Topics
- Publisher
- Subscriber
- Timers
- `Float32` messages

### Project 2 — Simulated Distance Sensor & Obstacle Detector 📏🚧

A simulated distance sensor publishes decreasing distance values, while an obstacle detector classifies the distance as SAFE, WARNING, or STOP.

**ROS concepts:**
- Nodes
- Topics
- Publisher
- Subscriber
- Callbacks
- Conditional logic
- `Float32` messages

### Project 3 — Calculator Service 🧮

A ROS 2 service that accepts two numbers and returns their sum.

The project uses a custom `.srv` interface with a separate interface package.

**ROS concepts:**
- Services
- Client / Server
- Custom ROS interfaces
- `.srv` files
- `ament_cmake`
- `ament_python`
- Request / Response

### Project 4 — Robot Safety Controller ⚠️🤖

A simulated robot controller subscribes to distance data and uses ROS 2 parameters to determine whether the robot is SAFE, in WARNING range, or should STOP.

The warning and stop distances can be changed while the node is running without modifying the Python code.

**ROS concepts:**
- ROS 2 Parameters
- Parameter declaration
- Parameter retrieval
- Runtime parameter changes
- Topics
- Subscriber
- Callbacks
- `Float32` messages

### Project 5 — Simulated Robot Launch System 🚀

A ROS 2 launch file starts the simulated distance sensor and robot safety controller together as a single system.

Instead of opening multiple terminals and running each node separately, the complete system can be started with one `ros2 launch` command.

**ROS concepts:**
- Launch files
- `LaunchDescription`
- Launch actions
- Starting multiple nodes
- Package launch configuration
- `ros2 launch`

### Project 6 — Simulated Robot Action Controller 🎯🤖

A simulated robot receives a target distance as an action goal, moves toward the target gradually, publishes feedback during movement, and returns a final result.

The project uses a custom `.action` interface with separate goal, feedback, and result definitions.

**ROS concepts:**
- ROS 2 Actions
- Action Server
- Action Client
- Custom ROS interfaces
- `.action` files
- Goals
- Feedback
- Results
- Goal cancellation
- `ament_cmake`
- `ament_python`

### Project 7 — TF2 Robot Frames 🧭

A simulated robot broadcasts its position using TF2, with `base_link` represented relative to the `odom` frame. A separate listener queries the transform and reports the robot's current position.

**ROS concepts:**
- TF2
- Coordinate frames
- `odom`
- `base_link`
- Transform broadcasting
- Transform listening
- `TransformStamped`
- `TransformBroadcaster`
- `TransformListener`
- `lookup_transform()`

### Project 8 — Simulated 2D LiDAR 📡

A simulated 2D LiDAR publishes `LaserScan` data containing 360 distance measurements. The project simulates obstacles at different distances and includes an obstacle analyzer that extracts front, left, and right distances.

The LiDAR data was visualized in RViz2 using the `/scan` topic.

**ROS concepts:**
- `sensor_msgs/msg/LaserScan`
- LiDAR simulation
- Range measurements
- Sensor data processing
- Topic publishing/subscribing
- RViz2
- LaserScan visualization
- Basic obstacle analysis
- Coordinate frames

### Project 9 — Robot Motion & Teleoperation 🤖

A simulated robot receives velocity commands through `/cmd_vel` using `geometry_msgs/msg/Twist`.

The robot simulator integrates linear and angular velocity to update the robot's simulated position and orientation. TF2 is used to publish the robot's `odom → base_link` transform.

A teleoperation node allows the robot to move forward, backward, turn, and stop using simple keyboard commands.

**ROS concepts:**
- `geometry_msgs/msg/Twist`
- `/cmd_vel`
- Velocity commands
- Robot motion simulation
- Linear and angular velocity
- Basic differential-drive-style motion equations
- TF2
- Quaternion orientation
- Teleoperation
- `odom → base_link`

### Project 10 — rosbag Data Recording & Replay 📦

ROS 2 topics from the simulated robot system were recorded using `ros2 bag`.

The project records and replays sensor data, velocity commands, and TF information. Recorded bags were inspected using `ros2 bag info` and replayed using `ros2 bag play`.

The final experiment recorded:

- `/cmd_vel`
- `/scan`
- `/tf`

The recorded dataset contained 339 messages over approximately 28.5 seconds.

**ROS concepts:**
- rosbag
- Recording ROS topics
- Replaying recorded data
- `ros2 bag record`
- `ros2 bag info`
- `ros2 bag play`
- SQLite3 bag storage
- Message timestamps
- Recorded datasets
- Multi-topic recording
- ROS data analysis

## How to Run

### Project 1 — Temperature Monitor

Run the simulated sensor:

```bash
ros2 run temp_monitor temp_sensor
```

In another terminal:

```bash
ros2 run temp_monitor temp_monitor
```

### Project 2 — Distance Sensor

Run the simulated distance sensor:

```bash
ros2 run distance_sensor distance_sensor
```

In another terminal:

```bash
ros2 run distance_sensor obstacle_detector
```

### Project 3 — Calculator Service

Run the calculator server:

```bash
ros2 run calculator_service calculator_server
```

In another terminal:

```bash
ros2 run calculator_service calculator_client
```

You can also call the service directly:

```bash
ros2 service call /add_two_numbers calculator_interfaces/srv/AddTwoNumbers "{a: 10.0, b: 25.0}"
```

### Project 4 — Robot Safety Controller

Run the simulated distance sensor:

```bash
ros2 run distance_sensor distance_sensor
```

In another terminal:

```bash
ros2 run robot_controller robot_controller
```

View the parameters:

```bash
ros2 param list
```

Check the warning distance:

```bash
ros2 param get /robot_controller warning_distance
```

Change the warning distance while the node is running:

```bash
ros2 param set /robot_controller warning_distance 1.5
```

### Project 5 — Simulated Robot Launch System

Start the complete system with one command:

```bash
ros2 launch robot_controller robot_system.launch.py
```

This launches:

- `distance_sensor`
- `robot_controller`

together.

### Project 6 — Simulated Robot Action Controller

Run the action server:

```bash
ros2 run robot_action_controller action_server
```

In another terminal:

```bash
ros2 run robot_action_controller action_client
```

Inspect the action:

```bash
ros2 action list
ros2 action info /move_robot
```

### Project 7 — TF2 Robot Frames

Run the TF broadcaster:

```bash
ros2 run tf2_demo tf_broadcaster
```

In another terminal:

```bash
ros2 run tf2_demo tf_listener
```

You can also inspect the transform directly:

```bash
ros2 run tf2_ros tf2_echo odom base_link
```

### Project 8 — Simulated 2D LiDAR

Run the LiDAR simulator:

```bash
ros2 run lidar_demo lidar_simulator
```

In another terminal, run the obstacle analyzer:

```bash
ros2 run lidar_demo obstacle_analyzer
```

Inspect the LiDAR data:

```bash
ros2 topic echo /scan
```

The `/scan` topic can also be visualized in RViz2 using a `LaserScan` display.

### Project 9 — Robot Motion & Teleoperation

Run the robot simulator:

```bash
ros2 run robot_motion robot_simulator
```

In another terminal, run the teleoperation controller:

```bash
ros2 run robot_motion teleop_controller
```

The teleoperation commands are:

```text
f → forward
b → backward
l → rotate left
r → rotate right
s → stop
```

The robot receives velocity commands through:

```text
/cmd_vel
```

The robot's transform can be inspected using:

```bash
ros2 run tf2_ros tf2_echo odom base_link
```

### Project 10 — rosbag Recording & Replay

Record selected ROS topics:

```bash
ros2 bag record /scan /cmd_vel /tf
```

Inspect the recorded bag:

```bash
ros2 bag info <bag_name>
```

Replay the recorded data:

```bash
ros2 bag play <bag_name>
```

While the bag is playing, the recorded topics are published again as ROS topics.

## Useful ROS 2 Commands

### Nodes

```bash
ros2 node list
ros2 node info <node_name>
```

### Topics

```bash
ros2 topic list
ros2 topic echo <topic>
ros2 topic info <topic>
ros2 topic hz <topic>
```

### Services

```bash
ros2 service list
ros2 service type /add_two_numbers
ros2 interface show calculator_interfaces/srv/AddTwoNumbers
```

### Parameters

```bash
ros2 param list
ros2 param get /robot_controller warning_distance
ros2 param set /robot_controller warning_distance 1.5
```

### Launch

```bash
ros2 launch robot_controller robot_system.launch.py
```

### Actions

```bash
ros2 action list
ros2 action info /move_robot
```

### TF2

```bash
ros2 run tf2_ros tf2_echo odom base_link
```

### rosbag

```bash
ros2 bag record <topic>
ros2 bag info <bag_name>
ros2 bag play <bag_name>
```

## Future Projects

This repository will grow as I learn more ROS 2 concepts, eventually moving toward more advanced robotics projects such as:

- URDF / Xacro
- `robot_state_publisher`
- Gazebo simulation
- Sensor integration
- SLAM
- Localization
- Nav2
- Autonomous mobile robot systems

## Author

Dharshini  
Robotics & Automation Engineering
