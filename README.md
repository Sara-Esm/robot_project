# 🤖 Robot Project: AprilTag Simulation with Camera Bot

This project simulates a robot with a camera that detects AprilTags in a Gazebo environment using ROS 2 (Humble).  
It's perfect for learning ROS 2 simulation, AprilTag detection, and working with custom Gazebo models.

---

## 🚀 Features

- 🧭 Gazebo simulation with a custom AprilTag marker  
- 📸 Robot equipped with a camera sensor  
- 🏷️ Real-time tag detection using `apriltag_ros`  
- 🖼️ Live image stream and detection via ROS 2 topics  

---

## 🗂️ Project Structure

robot_project/
├── launch/ # ROS 2 launch files
├── models/ # Gazebo models (AprilTag + Camera bot)
├── worlds/ # Custom world with AprilTag
├── config/ # Camera calibration config (optional)
└── README.md # Project documentation


---

## 🛠️ Requirements

- ROS 2 Humble
- Gazebo 11
- `apriltag_ros` package

---

## 🚀 How to Run

1. Launch the simulation:

   ```bash
   source ~/.bashrc
   source /opt/ros/humble/setup.bash
   ros2 launch launch/sim_apriltag_world.launch.py

2. View detections (AprilTag overlays):
ros2 topic echo /detections

View the camera feed:
3. ros2 run rqt_image_view rqt_image_view


📎 License
MIT — feel free to use, modify, and share.

