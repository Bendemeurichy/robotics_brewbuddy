import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='robotics_brewbuddy',
            executable='joystick_control',
            name='joystick_control',
            output='screen',
            parameters=[{'use_sim_time': False}]
        )
    ])
