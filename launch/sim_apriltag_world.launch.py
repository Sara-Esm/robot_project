from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    # Dynamically get the absolute path to the world file
    world_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            'worlds',
            'apriltag_world.world'
        )
    )

    return LaunchDescription([
        # Start Gazebo with the absolute path to the custom world
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_path],
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

