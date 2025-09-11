# Proyecto Roboracer con Librería Nav2

## Recorrido de circuito con Nav2
El coche puede ser visualizado en rviz y al ejecutar el archivo obstaculosFTG, iniciarà el recorrido del circuito según el mapa designado en el archivo sim.yaml.
```bash
#F1tenth
ros2 launch f1tenth_gym_ros gym_bridge_launch.py
ros2 run controllers obstaculosFTG
```
## Mapeo usando SLAM
Se implementó también la simulación en Gazebo donde se cuenta con el vehìculo con su lidar y cámara de profundidad, por el momento no se puede trasladar el movimiento del robot hacia Gazebo porque hay problemas con los topicos al usar ros2_control.

Los siguientes comandos son para ejecutar la simulación en Gazebo y trabajan con el xacro gazebo_racecar.xacro.
```bash
# F1tenth con gazebo
# Mundo vacío (default)
ros2 launch f1tenth_gym_ros gazebo_test.launch.py

# Con mundo personalizado
ros2 launch f1tenth_gym_ros gazebo_test.launch.py world:=./src/f1tenth_gym_ros/worlds/levine.world
```
