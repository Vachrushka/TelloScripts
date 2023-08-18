from djitellopy import tello
import KeyPressModule as kp
import time
import cv2
from threading import Thread
from pyzbar import pyzbar
import numpy as np

global img
kp.init()
tello = tello.Tello()
tello.connect()
print(tello.get_battery())
tello.set_video_direction(tello.CAMERA_DOWNWARD)
#tello.set_video_direction(tello.CAMERA_FORWARD)
tello.streamon()
time.sleep(3)
#tello.takeoff()

marker_buffer = None  # буфер увиденной команды
command_execution = False  # выполняет ли дрон команду сейчас
working = True  # управление отправкой комманд


def getKeyboardInput():  # метод интерпретации нажатых клавиш
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("d"):
        yv = speed
    elif kp.getKey("a"):
        yv = -speed

    #if kp.getKey("q"): yv = tello.land();
    #if kp.getKey("e"): yv = tello.takeoff();

    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]


def command_sender():  # метод отправки команд для демона, если они найдены
    global marker_buffer
    global command_execution
    while working:
        if marker_buffer is not None:  # если в буфере есть команда, выполняем ее
            id_m = marker_buffer
            print("Отправлено ID:", id_m)
            try:
                send_command(id_m)
            except Exception as e:  # если произошла ошибка, зачищаем буфер, завершаем выполнение команд
                print(e)
                marker_buffer = None
                command_execution = False
        time.sleep(.100)


def send_command(id):  # отправка и выполнение команды, взависимости от номера
    global command_execution
    global marker_buffer
    print("На выполнении")
    command_execution = True
    if id == 0:
        #tello.takeoff()
        print("взлет")

    elif id == 1:
        tello.land()

    elif id == 2:
        tello.move_up(30)

    elif id == 3:
        tello.move_down(30)

    elif id == 4:
        tello.move_forward(50)
        tello.rotate_counter_clockwise(45)
    elif id == 5:
        tello.rotate_clockwise(90)
        tello.move_forward(20)

    elif id == 6:
        tello.flip_back()

    elif id == 7:
        tello.move_left(30)
    elif id == 8:
        tello.move_right(30)
    elif id == 9:
        tello.move_back(30)

    print("Выполнено")
    marker_buffer = None  # когда команда выполнена, очищаем буфер и завершаем выполнение команды
    command_execution = False


def draw_barcode(decoded, image):  # отрисовка квадратика по контуру найденного куаркода
    # n_points = len(decoded.polygon)
    # for i in range(n_points):
    #     image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                          (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                          color=(0, 255, 0),
                          thickness=5)
    return image


def decode(image):  # расшифровка куаркода в картинки
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    data = None
    for obj in decoded_objects:
        # draw the barcode
        image = draw_barcode(obj, image)
        # print barcode type & data
        data = obj.data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

    return image, data


search_marker = Thread(target=command_sender)
search_marker.start()  # создание и запуск демона для отправки команд

while True:  # основной цикл

    vals = getKeyboardInput()  # получаем нажатые клавиши и отправляем дрону, если они есть
    if vals is None:
        vals = [0, 0, 0, 0]
    else:
        for val in vals:
            if val is None:
                val = 0

    if not command_execution:  # если команды не исполняются, то отправляем команды с клавиатуры
        tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = tello.get_frame_read().frame
    # img = cv2.resize(img, (360, 240))
    img = cv2.resize(img, (1080, 720))  # получаем и готовим картинку

    img, data = decode(img)  # получаем данные о кркодах с картинки

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    # markers = aruco.drawDetectedMarkers(img.copy(), corners, ids)

    if not command_execution:  # если нет выполняемых комманд, то записываем номер команды в буфер
        if data is not None:
            try:
                data = int(((str(data)).split()[1]).replace("'", ""))  # получаем номер команды
            except:
                pass
            else:
                marker_buffer = data

    cv2.imshow("Image", img)  # показ картинки
    # time.sleep(.100)
    cv2.waitKey(1)
    key = cv2.waitKey(1)
    if key == 27:  # функция указывает сколько миллисекунд показывать данный кадр, для картинок 0,
        # для вебки 1-10, для видео - 33.  27 - код клавиши ESC
        tello.streamoff()  # выключить видеопоток
        working = False
        command_execution = False
        break  # выход из цикла
    elif key == ord('q'):
        command_execution = True
        tello.takeoff()

    elif key == ord('e'):
        command_execution = True
        tello.land()

    elif key == ord('c'):
        print("command_execution = False")
        command_execution = False
