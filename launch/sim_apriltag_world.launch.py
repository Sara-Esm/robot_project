from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Start Gazebo with the custom world
        ExecuteProcess(
            cmd=['gazebo', '--verbose', 'robot_project/worlds/apriltag_world.world'],
            output='screen'
        ),

        # Start AprilTag node
        Node(
            package='apriltag_ros',
            executable='apriltag_node',
            name='apriltag_node',
            output='screen',
            parameters=[{'publish_tf': True}]
        )
    ])
