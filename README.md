# 🤖 AprilTag Simulation with Camera Bot

This project simulates a mobile robot equipped with a camera that detects AprilTags in a Gazebo environment using **ROS 2 Humble**. It is designed for learning and demonstrating core robotics concepts like simulation, perception, and tag-based localization.

---

## 🚀 Features

- 🧭 Gazebo simulation with a custom AprilTag marker
- 📸 Mobile robot with a simulated camera sensor
- 🏷️ Real-time AprilTag detection using `apriltag_ros`
- 🖼️ Live camera feed and detection data via ROS 2 topics

---

## 🗂️ Project Structure

robot_project/
├── config/                # Camera calibration (optional)
├── launch/                # ROS 2 launch files
├── models/
│   ├── camera_bot/        # Robot model with camera
│   └── apriltag_marker/   # AprilTag marker model and textures
├── worlds/                # Custom Gazebo world
└── README.md              # Project overview and instructions


---

## 🛠️ Requirements

- [ROS 2 Humble](https://docs.ros.org/en/humble/index.html)
- [Gazebo 11](http://gazebosim.org/)
- [`apriltag_ros`](https://github.com/AprilRobotics/apriltag_ros)

---

