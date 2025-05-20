# 🤖 Robot Project: AprilTag Simulation with Camera Bot

This project simulates a robot with a camera that detects AprilTags in a Gazebo environment using ROS 2 (Humble). It's perfect for learning how computer vision and robotics interact in simulation.

## 🚀 Features

- Gazebo simulation with custom AprilTag marker
- Camera sensor on a robot
- Real-time tag detection with `apriltag_ros`
- Live image stream and detection topic

## 🗂️ Project Structure

robot_project/
├── launch/ # ROS 2 launch files
├── models/ # Gazebo models (AprilTag + Camera bot)
├── worlds/ # Custom world with AprilTag
├── config/ # Camera calibration (if needed)
└── README.md


## 🛠️ Requirements

- ROS 2 Humble
- Gazebo 11
- apriltag_ros


## 🚀 How to Run

1. Start ROS 2 and Gazebo:
   ```bash
   source ~/.bashrc
   source /opt/ros/humble/setup.bash
   ros2 launch launch/sim_apriltag_world.launch.py

2. View detections:
ros2 run rqt_image_view rqt_image_view

3. View camera:
ros2 run rqt_image_view rqt_image_view


📎 License
MIT — feel free to use and modify.

