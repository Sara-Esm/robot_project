# 🤖 Robot Project: AprilTag Simulation with Camera Bot

This project simulates a mobile robot equipped with a camera inside a Gazebo world containing an AprilTag marker. It demonstrates how to integrate the `apriltag_ros` package to detect fiducial markers in a simulated environment.

## 🧠 Key Features

- Custom Gazebo world (`apriltag_world.world`) with AprilTag marker.
- `camera_bot` robot model with an integrated camera sensor.
- Launch file to:
  - Start Gazebo with the custom world.
  - Launch the `apriltag_ros` node for tag detection.
- Python-based ROS 2 launch system (`.launch.py` file).
