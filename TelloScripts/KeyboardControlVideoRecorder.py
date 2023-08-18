from djitellopy import tello
import KeyPressModule as kp
import time
import cv2
from threading import Thread

global img
kp.init()
tello = tello.Tello()
tello.connect()
print("Заряд батареи:", tello.get_battery())
keepRecording = False  # переменная, контролирующая запись видео
tello.streamon()
tello.set_video_direction(tello.CAMERA_DOWNWARD)  # позволяет включить нижнюю камеру(CAMERA_DOWNWARD)CAMERA_FORWARD
frame_read = tello.get_frame_read()  # получение настроек объекта кадра



def video_recorder():
    # создаем объект VideoWriter, записывающий в ./video.avi

    height, width, _ = frame_read.frame.shape  # получение размера кадра
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()


recorder = Thread(target=video_recorder)
tello.takeoff()

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
    global recorder
    global keepRecording

    if kp.getKey("r"):
        keepRecording = True
        recorder.start()
        time.sleep(0.3)

    if kp.getKey("t"):
        keepRecording = False  # переключение переменной для прекращения записи
        recorder.join()  # основная программа ждет завершения потока recorder
        time.sleep(0.3)

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    # img = cv2.resize(img, (1920, 1080))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
