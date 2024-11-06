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
        ),
        launch_ros.actions.Node(
            package='robotics_brewbuddy',
            executable='audio_processing',
            name='audio_processing',
            output='screen',
            parameters=[{'use_sim_time': False}]
        ),
        launch_ros.actions.Node(
            package='robotics_brewbuddy',
            executable='sentiment_analysis',
            name='sentiment_analysis',
            output='screen',
            parameters=[{'use_sim_time': False}]
        )
    ])
