from djitellopy import tello  # импортируем библиотеку

tello = tello.Tello()  # создание экземпляра дрона
tello.connect()  # подключение к дрону

print("\n-=Данные состояния дрона и датчиков=-")

print("Заряд батареи:", tello.get_battery())
print("Значение барометра:", tello.get_barometer())
print("Время полета:", tello.get_flight_time())

print("Наибольшая температура:", tello.get_highest_temperature())
print("Наименьшая температура:", tello.get_lowest_temperature())
print("Средняя температура:", tello.get_temperature())


print("\n-=Данные положения дрона=-")

print("Высота дрона:", tello.get_height())
print("TOF высота дрона:", tello.get_distance_tof())

print("Тангаж:", tello.get_pitch())
print("Крен:", tello.get_roll())
print("Рыскание:", tello.get_yaw())

print("Скорость по X:", tello.get_speed_x())
print("Скорость по Y:", tello.get_speed_y())
print("Скорость по Z:", tello.get_speed_z())

print("Ускорение по X:", tello.get_acceleration_x())
print("Ускорение по Y:", tello.get_acceleration_y())
print("Ускорение по Z:", tello.get_acceleration_z())


print("\n-=Работа с площадками=-")  # для Tello Edu (черных)
print("Была обнаружена площадка:", tello.get_mission_pad_id())
print("Расстояние до площадки по X:", tello.get_mission_pad_distance_x())
print("Расстояние до площадки по Y:", tello.get_mission_pad_distance_y())
print("Расстояние до площадки по Z:", tello.get_mission_pad_distance_z())


# Задание
# 1) Бесконечно выводить данные о дроне раз в 5 секунд
# 2) Импортировать библиотеку time
# 3) Замораживать программу командой time.sleep(t), где t время











