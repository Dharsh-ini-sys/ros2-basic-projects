# ROS 2 Basic Projects 🤖

A collection of beginner ROS 2 projects built while learning ROS 2, Python, nodes, topics, publishers, subscribers, and robot decision-making.

---

## Projects

### 01 — Simulated Temperature Monitor 

A simulated temperature sensor publishes temperature readings, while a monitor node subscribes to the `/temperature` topic and classifies the temperature as NORMAL or WARNING.

#### Architecture

```text
Simulated Temperature Sensor
            ↓
      /temperature
            ↓
    Temperature Monitor

ROS concepts
Publisher
Subscriber
Topics
std_msgs/msg/Float32
Timers
Callbacks


02 — Simulated Distance Sensor + Obstacle Detector

A simulated distance sensor publishes changing distance values. An obstacle detector subscribes to the /distance topic and determines whether the environment is SAFE, WARNING, or STOP.

Architecture
Simulated Distance Sensor
            ↓
        /distance
            ↓
     Obstacle Detector
       ↓      ↓      ↓
     SAFE  WARNING  STOP
Decision Logic
Distance > 1.0 m     → SAFE
0.5 m < Distance ≤ 1.0 m → WARNING
Distance ≤ 0.5 m     → STOP
ROS concepts
Publisher
Subscriber
Topics
std_msgs/msg/Float32
Timers
Callbacks
Conditional decision logic
Node-to-node communication
Technologies
ROS 2 Humble
Python
Ubuntu 22.04
WSL2
Git
GitHub
ROS 2 Concepts Practiced
Nodes
Topics
Publishers
Subscribers
Message types
Timers
Callbacks
Decision logic
ROS 2 package creation
Building with colcon
Running ROS 2 nodes
Git and GitHub workflow
Workspace Structure
ros2_work/
└── src/
    ├── temp_monitor/
    │   ├── temp_monitor/
    │   ├── package.xml
    │   ├── setup.py
    │   └── README.md
    │
    └── distance_sensor/
        ├── distance_sensor/
        │   ├── distance_sensor.py
        │   └── obstacle_detector.py
        ├── package.xml
        └── setup.py
How to Build

From the workspace:

cd ~/ros2_work
colcon build
source install/setup.bash
How to Run
Project 1 — Temperature Monitor

Run the simulated sensor:

ros2 run temp_monitor temp_sensor

In another terminal:

ros2 run temp_monitor temp_monitor
Project 2 — Distance Sensor

Run the simulated distance sensor:

ros2 run distance_sensor distance_sensor

In another terminal:

ros2 run distance_sensor obstacle_detector
Useful ROS 2 Commands
ros2 node list
ros2 topic list
ros2 topic echo /temperature
ros2 topic echo /distance
ros2 topic info /temperature
ros2 topic info /distance
Future Projects

This repository will grow as I learn more ROS 2 concepts, eventually moving from basic simulated nodes toward robot control, sensors, navigation, and SLAM.

Author

Dharshini
Robotics & Automation Engineering
