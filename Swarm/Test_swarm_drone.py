import threading
from djitellopy import TelloSwarm
import time
import math

swarm = TelloSwarm.fromIps([
    #"192.168.0.101"
    "192.168.0.102"
    #"192.168.0.108"
    #"192.168.0.104"
    #"192.168.178.42",
    #"192.168.178.43",
    #"192.168.178.44"
])

swarm.connect()
for tello in swarm:
    print("Drone:", tello.TELLO_IP, "btry%:", tello.get_battery())

swarm.takeoff()

#swarm.tellos[0].set_wifi_credentials("Tello_xxx", "12345678")
#swarm.tellos[0].connect_to_wifi("", "")

#swarm.curve_xyz_speed(20,20,30, 90, 90, 30, 15) #x y z x y z speed
#swarm.curve_xyz_speed(20,30,0, 60, 60, 0, 15) #x y z x y z speed 2
#swarm.curve_xyz_speed(-60,60,0, -20, 30, 0, 15) #x y z x y z speed 1
#swarm.curve_xyz_speed(60,-60,0, 20, -30, 0, 15) #x y z x y z speed 3

#проход по кругу
#swarm.curve_xyz_speed(20,50,0,70,70,0,15)
#swarm.curve_xyz_speed(50,-20,0,70,-70,0,15)
#swarm.curve_xyz_speed(-20,-50,0,-70,-70,0,15)
#swarm.curve_xyz_speed(-50,20,0,-70,70,0,15)

#полет по окружности в горизонтале (центр окружности по Y = 0, по игрику сдвинут на R)

top_arc_coordinate = 50   # x,y верхней точки круга и radius
half_arc_x = int(top_arc_coordinate * math.cos(45)) #27
half_arc_y = int(top_arc_coordinate * math.sin(45))
swarm.curve_xyz_speed(half_arc_x, half_arc_y, 0, top_arc_coordinate, top_arc_coordinate, 0, 15)
swarm.curve_xyz_speed(half_arc_y, -half_arc_x, 0, top_arc_coordinate,-top_arc_coordinate, 0, 15)
swarm.curve_xyz_speed(-half_arc_x, -half_arc_y, 0, -top_arc_coordinate, -top_arc_coordinate, 0, 15)
swarm.curve_xyz_speed(-half_arc_y, half_arc_x, 0, -top_arc_coordinate, top_arc_coordinate, 0, 15)
# (0 ;0) - центр
# 50 радиус
# x = 0 + 50*cos45 26
# y = 0 + 50*sin45 42


# swarm.go_xyz_speed(20, 20, 0, 20)  # дрон смотрит соосно с осью x
# swarm.go_xyz_speed(-40, 0, 0, 20)
# swarm.go_xyz_speed(0, -40, 0, 20)
# swarm.go_xyz_speed(40, 0, 0, 20)
# swarm.go_xyz_speed(0, 40, 0, 20)

swarm.land()
swarm.end()