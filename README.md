# Proyecto Roboracer con Librería Nav2

## Recorrido de circuito con Nav2
El coche puede ser visualizado en rviz y al ejecutar el archivo se definen puntos para que siga una trayectoria.
```bash
#definir ruta del world a utilizar
ros2 launch my_bot launch_sim.launch.py world:=./src/my_bot/worlds/obstacles.world
rviz2

#definir la ruta del mapa que se prefiera usar
ros2 launch my_bot localization_launch.py map:=./src/my_bot/maps/levine.yaml use_sim_time:=true
ros2 launch my_bot navigation_launch.py use_sim_time:=true map_subscribe_transient_local:=true
```
## Mapeo usando SLAM

```bash
# ejecutar simulacion, definir mundo a usar
ros2 launch my_bot launch_sim.launch.py world:=./src/my_bot/worlds/obstacles.world
rviz2

# ejecutar SLAM
ros2 launch slam_toolbox online_async_launch.py params_file:=./src/my_bot/config/mapper_params_online_async.yaml use_sim_time:=true

# mapear con teleop (eliminar lo que esta despues del 2do keyboard si hay problemas)
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
```
