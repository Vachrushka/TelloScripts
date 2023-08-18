from djitellopy import tello  # импортируем библиотеку

my_drone = tello.Tello()  # создание экземпляра дрона
my_drone.connect()  # подключение к дрону
print("Заряд батареи:", my_drone.get_battery())
my_drone.takeoff()  # автоматический взлет
my_drone.land()  # автоматическая посадка
