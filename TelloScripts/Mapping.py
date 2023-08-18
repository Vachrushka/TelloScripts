import math
from djitellopy import tello
import KeyPressModule as kp
import numpy as np
import time
import cv2

# Параметры
fSpeed = 200 / 10  # скорость дрона в см/сек (15 см/сек)
# fSpeed = 117 / 10  # скорость дрона в см/сек (15 см/сек)
aSpeed = 360 / 10  # угловая скорость в градусах/ceк (50d/s)
interval = 0.25
dInterval = fSpeed * interval
aInterval = aSpeed * interval
yaw = 0
x, y = 500, 500
a = 0

######

kp.init()
tello = tello.Tello()
tello.connect()
print(tello.get_battery())
tello.streamon()
points = [(0, 0), (0, 0)]

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 15
    aspeed = 50
    global x, y, yaw, a
    d = 0

    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = - 180

    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270
    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = - 90

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("d"):
        yv = aspeed
        yaw += aInterval
    elif kp.getKey("a"):
        yv = -aspeed
        yaw -= aInterval

    if kp.getKey("q"):  tello.land(); time.sleep(3)
    if kp.getKey("e"):  tello.takeoff()

    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    time.sleep(interval)
    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y]


def drawPoints(_img, _points):
    for point in _points:
        cv2.circle(_img, point, 5, (0, 0, 255), cv2.FILLED)
    cv2.circle(_img, _points[-1], 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(_img, f'({(_points[-1][0]- 500)/100},{(_points[-1][1]- 500)/100})m',
                (_points[-1][0]+10, _points[-1][0]+30), cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),1)


while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000, 1000, 3), np.uint8)
    if points[-1][0] != vals[4] or points[-1][1] != vals[5]:
        points.append((vals[4],vals[5]))

    #cv2.imshow("Output", img)
    #cv2.waitKey(1)

    img = tello.get_frame_read().frame
    # img = cv2.resize(img, (360, 240))
    # img = cv2.resize(img, (1920, 1080))
    img = cv2.resize(img, (1024, 600))

    drawPoints(img, points)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
