import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Package name
    package_name = 'my_bot'
    
    # Launch configuration variables
    use_sim_time = LaunchConfiguration('use_sim_time')
    map_file = LaunchConfiguration('map')
    params_file = LaunchConfiguration('params_file')
    
    # Paths
    nav2_launch_file_dir = os.path.join(get_package_share_directory('nav2_bringup'), 'launch')
    default_params_file = os.path.join(
        get_package_share_directory(package_name), 
        'config', 
        'nav2_params.yaml'  # Tu archivo corregido
    )
    rviz_config_file = os.path.join(
        get_package_share_directory(package_name),
        'config',
        'view_bot.rviz'
    )
    
    # Declare launch arguments
    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',  # True para simulación
        description='Use simulation (Gazebo) clock if true'
    )
    
    declare_map_cmd = DeclareLaunchArgument(
        'map',
        description='Full path to map file to load'
    )
    
    declare_params_file_cmd = DeclareLaunchArgument(
        'params_file',
        default_value=default_params_file,
        description='Full path to param file to load'
    )
    
    # Launch Nav2
    nav2_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_launch_file_dir, 'bringup_launch.py')
        ),
        launch_arguments={
            'map': map_file,
            'use_sim_time': use_sim_time,
            'params_file': params_file
        }.items(),
    )
    
    # Launch RViz (opcional)
    rviz_cmd = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )
    
    # Create launch description
    ld = LaunchDescription()
    
    # Add launch arguments
    ld.add_action(declare_use_sim_time_cmd)
    ld.add_action(declare_map_cmd)
    ld.add_action(declare_params_file_cmd)
    
    # Add actions
    ld.add_action(nav2_cmd)
    ld.add_action(rviz_cmd)  # Descomenta si quieres RViz automático
    
    return ld