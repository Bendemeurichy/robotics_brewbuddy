import launch
import launch_ros.actions
from launch import LaunchService
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import IncludeLaunchDescription
import os

def main():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='robotics_brewbuddy',
            executable='joystick_control',
            name='joystick_control',
            output='screen',
            parameters=[{'use_sim_time': False}]
        ),
        launch_ros.actions.Node(
            package='robotics_brewbuddy',
            executable='detect_people',
            name='detect_people',
            output='screen',
            parameters=[{'use_sim_time': False}]
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('robotics_brewbuddy'), 'launch', 'slam_toolbox.launch.py')])
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('robotics_brewbuddy'), 'launch', 'navigation_with_people_detection.launch.py')])
        )
    ])

    ls = LaunchService()
    ls.include_launch_description(ld)
    ls.run()

if __name__ == '__main__':
    main()
