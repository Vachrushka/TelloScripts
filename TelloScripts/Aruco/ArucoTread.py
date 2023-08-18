import time
from threading import Thread

import numpy as np
from djitellopy import tello  # 2.4.0
import cv2  # импорт библиотеки для работы с видео и изображениями
import cv2.aruco as aruco  # opencv-contrib-python 4.5.5.62

tello = tello.Tello()
tello.connect()
print("Заряд батареи:", tello.get_battery())

# tello.send_command_with_return(tello.CAMERA_DOWNWARD) гугл    #downvision 1
tello.set_video_direction(tello.CAMERA_DOWNWARD)
# tello.set_video_fps(tello.FPS_30)  # Устанавливает FPS (FPS_15, FPS_30)(кадры/в секунду), FPS_5 - не работает
# tello.set_video_resolution(tello.RESOLUTION_720P)  # Устанавливает качество изображения 480P/720P
# tello.set_video_bitrate(tello.BITRATE_AUTO)  # Устанавливает битрейт видеопотока
# tello.set_video_direction(tello.CAMERA_FORWARD)  # позволяет включить нижнюю камеру(CAMERA_DOWNWARD)
# по умолчанию CAMERA_FORWARD
tello.streamon()  # включить видеопоток

aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
parameters = aruco.DetectorParameters_create()
marker_buffer = None
command_execution = False
working = True


def get_markers():
    while True:
        img = tello.get_frame_read().frame  # получить видео-кадр камеры
        # img = cv2.resize(img, (360, 240))  # изменить разрешение изображение
        img = cv2.resize(img, (1080, 720))  # разрешение камеры дрона
        # img = cv2.resize(img, (1280, 720))
        # img = cv2.resize(img, (1920, 1080))

        # cv2.imshow("Video from Tello - {}%".format(tello.get_battery()), img)
        # cv2.imshow("Video from Tello", img)
        # отображение изображения на мониторе (Имя окна, изображение)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # gray = img

        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        markers = aruco.drawDetectedMarkers(img.copy(), corners, ids)
        global marker_buffer

        if not command_execution:
            for index, id in np.ndenumerate(ids):
                if id is not None:
                    marker_buffer = id



        cv2.imshow('frame', markers)

        time.sleep(.100)

        key = cv2.waitKey(1) & 0xFF
        # print(key)

        if key == ord('w'):
            print("Keyboard: Forward")
            tello.move_forward(20)
        elif key == ord('s'):
            print("Keyboard: Back")
            tello.move_back(20)
        elif key == ord('a'):
            print("Keyboard: Left")
            tello.move_left(20)
        elif key == ord('d'):
            print("Keyboard: Right")
            tello.move_right(20)


        elif key == ord('q'):
            print("Keyboard: Rotation Left")
            tello.rotate_counter_clockwise(15)
        elif key == ord('e'):
            print("Keyboard: Rotation Right")
            tello.rotate_clockwise(15)


        elif key == ord('r'):
            print("Keyboard: Up")
            tello.move_up(20)
        elif key == ord('f'):
            print("Keyboard: Down")
            tello.move_down(20)


        elif key == ord('t'):
            print("Keyboard: Take off")
            tello.takeoff()

        elif key == 27:
            print("Keyboard: Land and Stop")
            tello.streamoff()
            tello.land()
            global working
            working = False
            break

    cv2.destroyAllWindows()

def send_command(id):
    global command_execution
    global marker_buffer
    command_execution = True
    if id == 0:
        tello.land()

    if id == 1:
        tello.rotate_clockwise(90)
        tello.move_forward(50)

    if id == 2:
        tello.rotate_clockwise(90)
        tello.move_forward(50)
    if id == 3:
        tello.rotate_clockwise(90)
        tello.move_forward(50)
    if id == 4:
        tello.rotate_clockwise(90)
        tello.move_forward(50)
    marker_buffer = None
    command_execution = False


search_marker = Thread(target=get_markers)
search_marker.start()

while working:

    if marker_buffer is not None:
        id_m = marker_buffer
        print("Найдено ID:", id_m)
        send_command(id_m)
    time.sleep(.100)


search_marker.join()

