import cv2
import time
from threading import Thread

from djitellopy import Tello

tello = Tello()
tello.connect()

keepRecording = True  # переменная, контролирующая запись видео
tello.streamon()
frame_read = tello.get_frame_read()  # получение настроек объекта кадра

def video_recorder():
    # создаем объект VideoWriter, записывающий в ./video.avi

    height, width, _ = frame_read.frame.shape  # получение размера кадра
    video = cv2.VideoWriter('video2.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()


# нам нужно запустить рекордер в отдельном потоке, иначе блокируются опции
# предотвратит добавление кадров в видео
recorder = Thread(target=video_recorder)  # создание отдельного потока recorder
# который будет выполнять функцию video_recorder
recorder.start()    # запуск отдельного потока recorder

time.sleep(10)  # небольшое ожидание
tello.takeoff()
tello.move_up(100)
tello.rotate_counter_clockwise(360)
tello.land()
keepRecording = False  # переключение переменной для прекращения записи
recorder.join()  # основная программа ждет завершения потока recorder

# Задание:
# 1) Написать программу, реализующую съемку объекта, стоящего на земле.
# 2) Использовать переднюю камеру.
# 3) Объект должен быть снят со всех сторон, не выходить из кадра.
