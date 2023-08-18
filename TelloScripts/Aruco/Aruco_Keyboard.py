from threading import Thread

import numpy as np
from djitellopy import tello
import KeyPressModule as kp
import time
import cv2
import cv2.aruco as aruco

global img
kp.init()
aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
parameters = aruco.DetectorParameters_create()
tello = tello.Tello()
tello.connect()
print(tello.get_battery())
tello.set_video_direction(tello.CAMERA_DOWNWARD)
tello.streamon()
time.sleep(1)
tello.takeoff()
time.sleep(1)
cmd_in_progress = False

plan = [5,1,2,3,4]
current_step = 0

#time.sleep(2)

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


def send_cmd(id):
    global cmd_in_progress
    global current_step

    #if current_step > len(plan) or id != plan[current_step]:
    ##    cmd_in_progress = False
     #   return
    #current_step += 1

    if id == 0:
        tello.land()

    elif id == 1:
        tello.rotate_clockwise(90)
        tello.move_forward(50)

    elif id == 2:
        tello.rotate_clockwise(90)
        tello.move_forward(50)
    elif id == 3:
        tello.rotate_clockwise(90)
        tello.move_forward(50)
    elif id == 4:
        tello.rotate_clockwise(90)
        tello.move_forward(50)
    elif id == 5:
        tello.move_forward(100)
    elif id == 6:
        tello.rotate_clockwise(30)
    elif id == 7:
        tello.rotate_counter_clockwise(30)
    elif id == 8:
        tello.flip_forward()
    elif id == 9:
        tello.takeoff()

    cmd_in_progress = False

#start_cmd = True
while True:
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    markers = aruco.drawDetectedMarkers(img.copy(), corners, ids)

    for index, id in np.ndenumerate(ids):
        if id is not None and not cmd_in_progress:
            cmd_in_progress = True
            print("Найдено ID:", id)
            send_cmd(id)

    #if start_cmd:
    #    tello.move_forward(175)
    #    start_cmd = False


    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    # img = cv2.resize(img, (1920, 1080))
    cv2.imshow("Image", markers)
    cv2.waitKey(1)
