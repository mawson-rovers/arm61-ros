#!/usr/bin/env python3

import os
import sys

from ament_index_python.packages import get_package_share_directory

import launch
import launch_ros.actions


def generate_launch_description():
    # Load the URDF into a parameter
    bringup_dir = get_package_share_directory('arm61')

    # URDF path: uncomment the high or low resolution version
    # urdf_path = os.path.join(bringup_dir, 'urdf', 'arm61_lowPoly.urdf')
    urdf_path = os.path.join(bringup_dir, 'urdf', 'arm61_highPoly.urdf')

    # open URDF
    urdf = open(urdf_path).read()

    return launch.LaunchDescription([
        launch_ros.actions.Node(
            name='robot_state_publisher',
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': urdf}],
        ),
        launch_ros.actions.Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
        ),
        launch_ros.actions.Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d' + os.path.join(get_package_share_directory('arm61'), 'rviz', 'arm61.rviz')]
        ),
    ])


def main(argv=sys.argv[1:]):
    # rospy.init_node('joint_state_publisher_gui')
    # """Run lifecycle nodes via launch."""
    ld = generate_launch_description()
    ls = launch.LaunchService(argv=argv)
    ls.include_launch_description(ld)
    return ls.run()


if __name__ == '__main__':
    main()