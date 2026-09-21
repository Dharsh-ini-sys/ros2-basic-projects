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

## How to Run

### Project 1 — Temperature Monitor

Run the simulated sensor:

```bash
ros2 run temp_monitor temp_sensor

In another terminal:

ros2 run temp_monitor temp_monitor
Project 2 — Distance Sensor

Run the simulated distance sensor:

ros2 run distance_sensor distance_sensor

In another terminal:

ros2 run distance_sensor obstacle_detector
Project 3 — Calculator Service

Run the calculator server:

ros2 run calculator_service calculator_server

In another terminal:

ros2 run calculator_service calculator_client

You can also call the service directly using the ROS 2 CLI:

ros2 service call /add_two_numbers calculator_interfaces/srv/AddTwoNumbers "{a: 10.0, b: 25.0}"
Project 4 — Robot Safety Controller

Run the simulated distance sensor:

ros2 run distance_sensor distance_sensor

In another terminal:

ros2 run robot_controller robot_controller

View the parameters:

ros2 param list

Check the warning distance:

ros2 param get /robot_controller warning_distance

Change the warning distance while the node is running:

ros2 param set /robot_controller warning_distance 1.5
Project 5 — Simulated Robot Launch System

Start the complete system with one command:

ros2 launch robot_controller robot_system.launch.py

This launches:

distance_sensor
robot_controller

together.

Project 6 — Simulated Robot Action Controller

Run the action server:

ros2 run robot_action_controller action_server

In another terminal:

ros2 run robot_action_controller action_client

The client sends a goal of 5.0 m and receives feedback while the simulated robot moves toward the goal.

You can inspect the action with:

ros2 action list

and:

ros2 action info /move_robot
Useful ROS 2 Commands
ros2 node list
ros2 topic list
ros2 topic echo /temperature
ros2 topic echo /distance
ros2 topic info /temperature
ros2 topic info /distance
ros2 service list
ros2 service type /add_two_numbers
ros2 interface show calculator_interfaces/srv/AddTwoNumbers
ros2 param list
ros2 param get /robot_controller warning_distance
ros2 param set /robot_controller warning_distance 1.5
ros2 launch robot_controller robot_system.launch.py
ros2 action list
ros2 action info /move_robot
Future Projects

This repository will grow as I learn more ROS 2 concepts, eventually moving toward more advanced robotics projects.

Author

Dharshini
Robotics & Automation Engineering
