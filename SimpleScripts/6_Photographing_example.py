from djitellopy import Tello
import cv2  # импорт библиотеки для работы с видео и изображениями

tello = Tello()
tello.connect()

tello.streamon()  # включить видеопоток

cartinka = tello.get_frame_read()
frame_read = cartinka.frame
#frame_read = tello.get_frame_read().frame  # получить кадр c камеры
cv2.imwrite("../Resources/Images/picture12.png", frame_read)  # сохранить изображение в память компьютера
# cv2.imwrite("picture.png", frame_read)  # сохранить изображение в память компьютера
