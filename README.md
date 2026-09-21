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

## How to Run

### Project 1 — Temperature Monitor

Run the simulated sensor:

```bash
ros2 run temp_monitor temp_sensor
````

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

You can also call the service directly using the ROS 2 CLI:

```bash
ros2 service call /add_two_numbers calculator_interfaces/srv/AddTwoNumbers "{a: 10.0, b: 25.0}"
```

## Useful ROS 2 Commands

```bash
ros2 node list
ros2 topic list
ros2 topic echo /temperature
ros2 topic echo /distance
ros2 topic info /temperature
ros2 topic info /distance
ros2 service list
ros2 service type /add_two_numbers
ros2 interface show calculator_interfaces/srv/AddTwoNumbers
```

## Future Projects

This repository will grow as I learn more ROS 2 concepts, eventually moving toward more advanced robotics projects.

## Author

Dharshini
Robotics & Automation Engineering

