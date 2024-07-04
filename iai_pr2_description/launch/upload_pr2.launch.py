import os

import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    package_share_directory = get_package_share_directory('iai_pr2_description')

    xacro_file = os.path.join(package_share_directory, 'robots', 'pr2_with_ft2_cableguide.xacro')

    doc = xacro.process_file(xacro_file, mappings={'radius': '0.9'})
    robot_desc = doc.toprettyxml(indent='  ')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),
    ])
