import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    package_share_directory = get_package_share_directory('iai_pr2_description')

    # Path to the upload_pr2.launch.py file
    upload_pr2_launch = os.path.join(package_share_directory, 'launch', 'upload_pr2.launch.py')

    rviz_config_file = os.path.join(package_share_directory, 'rviz', 'display_config.rviz')

    return LaunchDescription([
        # Include the upload_pr2 launch file
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(upload_pr2_launch)
        ),
        # Joint state publisher GUI node
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),
        # Static transform publisher (example, modify as needed for your robot)
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'base_footprint']
        ),
        # RViz node
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
        ),
    ])

