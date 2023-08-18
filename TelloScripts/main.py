import cv2
from djitellopy import Tello
# работа с камерой (видео)
tello = Tello()
tello.connect()
print(tello.get_battery())

tello.streamon()

while True:
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    # img = cv2.resize(img, (1920, 1080))
    cv2.imshow("Image", img)
    cv2.waitKey(1)


