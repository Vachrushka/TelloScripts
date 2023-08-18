from djitellopy import tello
import KeyPressModule as kp
import time
import cv2
import cv2.aruco as aruco
from threading import Thread

import numpy as np
global img
kp.init()
tello = tello.Tello()
tello.connect()
print(tello.get_battery())
tello.set_video_direction(tello.CAMERA_DOWNWARD)
tello.streamon()
tello.takeoff()

aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
parameters = aruco.DetectorParameters_create()
marker_buffer = None
command_execution = False
working = True


def getKeyboardInput():
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

    if kp.getKey("q"): yv = tello.land(); time.sleep(3)
    if kp.getKey("e"): yv = tello.takeoff()

    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]


def command_sender():
    global marker_buffer
    while working:
        if marker_buffer is not None:
            id_m = marker_buffer
            print("Найдено ID:", id_m)
            send_command(id_m)
        time.sleep(.100)


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


search_marker = Thread(target=command_sender)
search_marker.start()

while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    #img = cv2.resize(img, (1080, 720))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    markers = aruco.drawDetectedMarkers(img.copy(), corners, ids)


    if not command_execution:
        for index, id in np.ndenumerate(ids):
            if id is not None:
                marker_buffer = id

    cv2.imshow("Image", markers)
    #time.sleep(.100)
    cv2.waitKey(1)