import time

import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from djitellopy import tello

tello = tello.Tello()
tello.connect()

table_data = []

fig = plt.figure()
plt.title("-=Данные состояния дрона и датчиков=-")
while True:
    break
    table_data.append(["Заряд батареи:", tello.get_battery()])
    table_data.append(["Значение барометра:", tello.get_barometer()])
    table_data.append(["Время полета:", tello.get_flight_time()])
    table_data.append(["Наибольшая температура:", tello.get_highest_temperature()])
    table_data.append(["Наименьшая температура:", tello.get_lowest_temperature()])
    table_data.append(["Средняя температура:", tello.get_temperature()])
    table_data.append(["Высота дрона:", tello.get_height()])
    table_data.append(["TOF высота дрона:", tello.get_distance_tof()])
    table_data.append(["Тангаж:", tello.get_pitch()])
    table_data.append(["Крен:", tello.get_roll()])
    table_data.append(["Рыскание:", tello.get_yaw()])
    table_data.append(["Скорость по X:", tello.get_speed_x()])
    table_data.append(["Скорость по Y:", tello.get_speed_y()])
    table_data.append(["Скорость по Z:", tello.get_speed_z()])
    table_data.append(["Ускорение по X:", tello.get_acceleration_x()])
    table_data.append(["Ускорение по Y:", tello.get_acceleration_y()])
    table_data.append(["Ускорение по Z:", tello.get_acceleration_z()])

    table = plt.table(cellText=table_data,  loc='center', edges="horizontal")
    table.auto_set_font_size(False)
    table.set_fontsize(11)

    plt.show()
    time.sleep(0.5)
    table_data.clear()

def init():
    table_data = []
    return table_data,

def animate(i):
    table_data.append(["Заряд батареи:", tello.get_battery()])
    table_data.append(["Значение барометра:", tello.get_barometer()])
    table_data.append(["Время полета:", tello.get_flight_time()])
    table_data.append(["Наибольшая температура:", tello.get_highest_temperature()])
    table_data.append(["Наименьшая температура:", tello.get_lowest_temperature()])
    table_data.append(["Средняя температура:", tello.get_temperature()])
    table_data.append(["Высота дрона:", tello.get_height()])
    table_data.append(["TOF высота дрона:", tello.get_distance_tof()])
    table_data.append(["Тангаж:", tello.get_pitch()])
    table_data.append(["Крен:", tello.get_roll()])
    table_data.append(["Рыскание:", tello.get_yaw()])
    table_data.append(["Скорость по X:", tello.get_speed_x()])
    table_data.append(["Скорость по Y:", tello.get_speed_y()])
    table_data.append(["Скорость по Z:", tello.get_speed_z()])
    table_data.append(["Ускорение по X:", tello.get_acceleration_x()])
    table_data.append(["Ускорение по Y:", tello.get_acceleration_y()])
    table_data.append(["Ускорение по Z:", tello.get_acceleration_z()])
    return table_data,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)


anim.save('sine_wave.gif', writer='imagemagick')