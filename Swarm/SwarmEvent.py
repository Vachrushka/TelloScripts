import threading
from djitellopy import TelloSwarm
import time

swarm = TelloSwarm.fromIps([
    "192.168.0.101",
    "192.168.0.102",
    "192.168.0.103",
    "192.168.0.104"
    #"192.168.178.42",
    #"192.168.178.43",
    #"192.168.178.44"
])

swarm.connect()
for tello in swarm:
    print("Drone:", tello.TELLO_IP, "btry%:", tello.get_battery())

swarm.takeoff()


swarm.parallel(lambda i, tello: tello.move_up(i*10+20))

swarm.rotate_counter_clockwise(45)
swarm.move_forward(50)

swarm.parallel(lambda i, tello: tello.move_down(i*10+20))

swarm.parallel(lambda i, tello: tello.rotate_clockwise(i*90))

swarm.move_forward(30)

#swarm.parallel(lambda i, tello: tello.rotate_clockwise(i*90))  # 270 135 45 -45
swarm.tellos[0].rotate_counter_clockwise(135)
swarm.tellos[1].rotate_clockwise(135)
swarm.tellos[2].rotate_clockwise(45)
swarm.tellos[3].rotate_counter_clockwise(45)

swarm.move_forward(40)

swarm.land()
swarm.end()

