import time

from djitellopy import tello

my_drone = tello.Tello()
my_drone.connect()
print("Заряд батареи:", my_drone.get_battery())
my_drone.set_speed(10)  # задать скорость в см/сек
my_drone.takeoff()

my_drone.move_forward(100)  # движение вперед
my_drone.move_left(100)  # влево
my_drone.set_speed(30)
my_drone.move_back(50)  # назад
my_drone.move_right(50)  # вправо

my_drone.move_up(50)  # вверх
my_drone.move_down(25)  # вниз

my_drone.rotate_clockwise(90)  # поворот по часовой стрелке
my_drone.rotate_counter_clockwise(180)  # против часовой
my_drone.land()

# Задание:
# 1) Написать программу полета дрона.
# 2) Автоматический взлет, подъем на высоту метра, пролететь по траектории квадрата на заданной высоте, вернувшись
#    в начальное положение, подъем на высоту два метра, пролет по траектории квадрата, расположенному вертикально.
# 3) Дрон должен вернуться в исходную точку взлета.
