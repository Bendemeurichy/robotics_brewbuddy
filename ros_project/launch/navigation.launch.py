import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='nav2_bringup',
            executable='bringup_launch.py',
            name='nav2_bringup',
            output='screen',
            parameters=[{
                'use_sim_time': False,
                'autostart': True,
                'params_file': 'path/to/your/nav2_params.yaml'
            }]
        )
    ])
