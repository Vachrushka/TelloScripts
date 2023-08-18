from djitellopy import TelloSwarm


swarm = TelloSwarm.fromIps([
    "192.168.43.111",
    "192.168.43.103"
])

swarm.connect()

for tello in swarm.tellos:
    print("Drone:", tello.TELLO_IP, "btry%:", tello.get_battery())

swarm.takeoff()

swarm.move_up(20) # для всего роя одновременно
swarm.move_forward(20)


swarm.land()
