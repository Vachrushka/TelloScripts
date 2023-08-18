from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "192.168.0.100",
    "192.168.0.102"
    #"192.168.178.42",
    #"192.168.178.43",
    #"192.168.178.44"
])

swarm.connect()
swarm.sequential(lambda i, tello: print(str(tello.query_serial_number())+": "+str(tello.get_battery())))   # работает
swarm.sequential(lambda i, tello: tello.set_wifi_credentials("Tello-XXXX","tello"))   # работает
#swarm.reboot()
#swarm.set_wifi_credentials("Tello-XXXX","tello")
swarm.takeoff()
#battery = swarm.get_battery()
#print(battery)

# работает параллельно на всех Tello
#swarm.move_up(100)


# выполняется одним Tello за другим
#swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))
#swarm.sequential(lambda i, tello: tello.rotate_clockwise(180))

# заставить каждый Tello делать что-то уникальное параллельно
#swarm.parallel(lambda i, tello: tello.rotate_counter_clockwise(i*90))

#swarm.land()
#swarm.end()