import threading
from djitellopy import TelloSwarm
import time
import math

swarm = TelloSwarm.fromIps([
    # "192.168.0.100",
    # "192.168.0.101",
    "192.168.0.102",
    "192.168.0.103"
    # "192.168.0.104",
    # "192.168.0.105",
    # "192.168.0.106",
    # "192.168.0.107"
    # "192.168.0.108"
])
all_tellos = swarm.tellos

swarm.connect()
for tello in swarm:
    print("Drone:", tello.TELLO_IP, "btry%:", tello.get_battery())

# дроны стоят в углах шестиугольника и смотрят в одну сторону. 1 дрон - нижний левый угол. 4 дрон верхний правый угол шестиугольника
# сторона шестиугольника 70 см
swarm.takeoff()
swarm.parallel(lambda i, tello: tello.rotate_clockwise(30 + i * 60))


def doTrio(i, tello):
    if i % 2 == 0:
        tello.move_up(30)
    else:
        tello.move_down(20)
    # make all other drones wait for one to complete its flip
    swarm.sync()


def doCyrcle(i, tello):
    top_arc_coordinate = 50  # x,y верхней точки круга и radius
    half_arc_x = int(top_arc_coordinate * math.cos(45))  # 27
    half_arc_y = int(top_arc_coordinate * math.sin(45))
    tello.curve_xyz_speed(half_arc_x, half_arc_y, 0, top_arc_coordinate, top_arc_coordinate, 0, 15)
    swarm.sync()
    tello.curve_xyz_speed(half_arc_y, -half_arc_x, 0, top_arc_coordinate, -top_arc_coordinate, 0, 15)
    swarm.sync()
    tello.curve_xyz_speed(-half_arc_x, -half_arc_y, 0, -top_arc_coordinate, -top_arc_coordinate, 0, 15)
    swarm.sync()
    tello.curve_xyz_speed(-half_arc_y, half_arc_x, 0, -top_arc_coordinate, top_arc_coordinate, 0, 15)
    swarm.sync()


def shift(i, tello):
    n = 0
    if i % 2 == 0:
        tello.rotate_clockwise(60)
    else:
        tello.rotate_counter_clockwise(60)

    swarm.sync()
    while n < 6:
        if i % 2 == 0:
            tello.move_forward(70)
        else:
            tello.move_forward(70)

        swarm.sync()

        if i % 2 == 0:
            tello.rotate_counter_clockwise(60)
        else:
            tello.rotate_clockwise(60)

        swarm.sync()
        if n % 2 == 0:
            if i % 2 == 0:
                tello.move_down(50)
            else:
                tello.move_up(50)

        else:
            if i % 2 == 0:
                tello.move_up(50)
            else:
                tello.move_down(50)

        swarm.sync()
        n += 1


def sixangleFly(swarm):
    swarm.rotate_counter_clockwise(60)
    swarm.move_forward(70)
    swarm.rotate_clockwise(60)
    swarm.move_forward(70)
    swarm.rotate_clockwise(60)
    swarm.move_forward(70)
    swarm.rotate_clockwise(60)
    swarm.move_forward(70)
    swarm.rotate_clockwise(120)


# полет в 6 по шестиугольнику
# sixangleFly(swarm) # ок

# swarm.parallel(lambda i, tello: tello.rotate_counter_clockwise(i*60))
# swarm.parallel(doCyrcle)

swarm.parallel(doTrio)  # ок разделены

# swarm.parallel(lambda i, tello: tello.rotate_clockwise(i*60)) # смотрят в центр

swarm.parallel(shift)

# полет в тройках
# swarm.move_forward(120)
# swarm.rotate_counter_clockwise(60)
#
# swarm.move_left(60)
# swarm.rotate_counter_clockwise(30)


# swarm.parallel(lambda i, tello: tello.move_up(i*10+20))
#
# swarm.rotate_counter_clockwise(45)
# swarm.move_forward(50)
#
# swarm.parallel(lambda i, tello: tello.move_down(i*10+20))
#
# swarm.parallel(lambda i, tello: tello.rotate_clockwise(i*90))
#
# swarm.move_forward(30)
#
# #swarm.parallel(lambda i, tello: tello.rotate_clockwise(i*90))  # 270 135 45 -45
# swarm.tellos[0].rotate_counter_clockwise(135)
# swarm.tellos[1].rotate_clockwise(135)
# swarm.tellos[2].rotate_clockwise(45)
# swarm.tellos[3].rotate_counter_clockwise(45)
#
# swarm.move_forward(40)

swarm.land()
swarm.end()
