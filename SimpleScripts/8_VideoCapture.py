from djitellopy import tello
import cv2  # импорт библиотеки для работы с видео и изображениями

tello = tello.Tello()
tello.connect()

print("Заряд батареи:", tello.get_battery())

tello.streamon()  # включить видеопоток
# tello.set_video_fps(tello.FPS_30)  # Устанавливает FPS (FPS_15, FPS_30)(кадры/в секунду), FPS_5 - не работает
# tello.set_video_resolution(tello.RESOLUTION_720P)  # Устанавливает качество изображения 480P/720P
# tello.set_video_bitrate(tello.BITRATE_AUTO)  # Устанавливает битрейт видеопотока
tello.set_video_direction(tello.CAMERA_DOWNWARD)  # позволяет включить нижнюю камеру(CAMERA_DOWNWARD)
# по умолчанию CAMERA_FORWARD


while True:
    img = tello.get_frame_read().frame  # получить видео-кадр камеры
    # img = cv2.resize(img, (360, 240))  # изменить разрешение изображение
    img = cv2.resize(img, (1080, 720))  # разрешение камеры дрона
    # img = cv2.resize(img, (1280, 720))
    # img = cv2.resize(img, (1920, 1080))

    # cv2.imshow("Video from Tello - {}%".format(tello.get_battery()), img)
    cv2.imshow("Video from Tello", img)
    # отображение изображения на мониторе (Имя окна, изображение)

    if cv2.waitKey(1) == 27:  # функция указывает сколько миллисекунд показывать данный кадр, для картинок 0,
        # для вебки 1-10, для видео - 33.  27 - код клавиши ESC
        tello.streamoff()  # выключить видеопоток
        break  # выход из цикла

# Задание:
# 1) Написать программу, реализующую фотографирование нескольких объектов на земле.
# 2) Использовать нижнюю камеру.
# 3) Использовать 6, 7 примеры.
