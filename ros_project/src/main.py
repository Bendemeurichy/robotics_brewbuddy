import launch
import launch_ros.actions
from launch import LaunchService

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
        )
    ])

    ls = LaunchService()
    ls.include_launch_description(ld)
    ls.run()

if __name__ == '__main__':
    main()
