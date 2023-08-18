from djitellopy import tello

tello = tello.Tello()
tello.connect()
tello.takeoff()

print("---=== Полетный контроллер ===---")
print("Заряд батареи:", tello.get_battery())
print("""
        1) Поворот по часовой стрелеке на 90 градусов
        2) Поворот против часовой стрелки на 90 градусов
        3) Посадить дрон
""")
user_instruction = int(input("Напишите номер инструкции: "))  # ввод цифры с клавиатуры

if user_instruction == 1:
    tello.rotate_clockwise(90)  # поворот по часовой стрелке
elif user_instruction == 2:
    tello.rotate_counter_clockwise(90)  # поворот против часосой стрелки
elif user_instruction == 3:
    tello.land()


# Задание:
# 1) Реализовать полноценное перемещение в пространстве.
# 2) Реализовать опрос и отправку команд в цикле.
# 3) Сбор и вывод в консоль телеметрии после отправки каждой инструкции.
