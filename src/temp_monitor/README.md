````markdown
# ROS 2 Simulated Temperature Monitor 🌡️

A beginner ROS 2 project that simulates a temperature sensor and monitors the incoming temperature data in real time.

## Overview

This project simulates a temperature sensor using Python and publishes temperature readings through a ROS 2 topic.

A separate monitoring node subscribes to the readings and determines whether the temperature is `NORMAL` or `WARNING` based on a predefined threshold.

## ROS 2 Architecture

```text
┌─────────────────────────┐
│  Simulated Temperature  │
│        Sensor           │
│     temp_sensor         │
└────────────┬────────────┘
             │
             │ publishes
             ▼
       /temperature
             │
             │ subscribes
             ▼
┌─────────────────────────┐
│  Temperature Monitor    │
│     temp_monitor        │
└────────────┬────────────┘
             │
             ▼
       NORMAL / WARNING
````

## Technologies

* ROS 2 Humble
* Python
* Ubuntu 22.04
* WSL2
* Git & GitHub

## ROS 2 Concepts Practiced

* Nodes
* Publishers
* Subscribers
* Topics
* Messages
* Timers
* ROS 2 Python packages
* Colcon
* ROS 2 command-line tools

## Package Structure

```text
temp_monitor/
├── package.xml
├── setup.py
├── setup.cfg
├── resource/
│   └── temp_monitor
├── temp_monitor/
│   ├── __init__.py
│   ├── temp_sensor.py
│   └── temp_monitor.py
└── test/
```

## How to Run

### 1. Source ROS 2

```bash
source /opt/ros/humble/setup.bash
```

### 2. Source the workspace

```bash
source ~/ros2_work/install/setup.bash
```

### 3. Run the simulated temperature sensor

```bash
ros2 run temp_monitor temp_sensor
```

The sensor generates a changing temperature value and publishes it approximately every second.

Example:

```text
[INFO] [temp_sensor]: Temperature: 25.17 °C
[INFO] [temp_sensor]: Temperature: 25.46 °C
[INFO] [temp_sensor]: Temperature: 25.90 °C
```

### 4. Run the temperature monitor

Open a second terminal and source ROS 2 and the workspace:

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_work/install/setup.bash
```

Then run:

```bash
ros2 run temp_monitor temp_monitor
```

Example:

```text
[INFO] [temperature_monitor]: Temperature: 27.34 °C | Status: NORMAL
[INFO] [temperature_monitor]: Temperature: 29.81 °C | Status: NORMAL
[INFO] [temperature_monitor]: Temperature: 30.21 °C | Status: WARNING
```

## Inspecting the ROS Topic

The temperature data is published on:

```text
/temperature
```

View available topics:

```bash
ros2 topic list
```

View the temperature messages directly:

```bash
ros2 topic echo /temperature
```

View information about the topic:

```bash
ros2 topic info /temperature
```

The topic uses the message type:

```text
std_msgs/msg/Float32
```

## What I Learned

Through this project, I learned how ROS 2 nodes communicate using topics.

The simulated temperature sensor acts as a publisher, while the temperature monitor acts as a subscriber.

I also learned how to create a Python ROS 2 package, register executables using `setup.py`, build a package using `colcon`, source a ROS 2 workspace, and run ROS 2 nodes from the command line.

## Future Improvements

* Add a configurable temperature threshold using ROS 2 parameters.
* Add simulated sensor noise.
* Add temperature history and statistics.
* Add graphical visualization.
* Integrate the simulated sensor into a robot simulation.

## Project Status

Completed



```
```
