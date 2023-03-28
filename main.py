# import cv2
#
# # загружаем видеофайл
# video = cv2.VideoCapture("New Project 2 [49398A1].mp4")
# ret, frame = video.read()
# prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# while True:
#     # читаем текущий кадр из видеофайла
#     ret, frame = video.read()
#     if not ret:
#         break
#
#     # преобразуем текущий кадр в черно-белый
#     curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # вычисляем изменения между двумя соседними кадрами
#
#     diff = cv2.absdiff(curr_frame, prev_frame)
#     # извлекаем среднее значение изменений
#     mean_diff = cv2.mean(diff)
#     # если значение больше заданного порога,
#     # то считаем, что на экране происходят быстрые изменения
#     if mean_diff[0] > 50:
#         print("Эпилептический контент обнаружен!")
#         frame = cv2.GaussianBlur(frame, (5, 5), 2)
#         # здесь может быть ваш код для обработки эпилептического контента
#     cv2.imshow("Frame", frame)
#     cv2.imshow("Diff", diff)
#     prev_frame = curr_frame
# video.release()

# import cv2
#
# cap = cv2.VideoCapture("New Project 2 [49398A1].mp4")
# ret, frame = cap.read()
# prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     diff = cv2.absdiff(curr_frame, prev_frame)
#
#     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
#     diff = cv2.erode(diff, kernel, iterations=1)
#     diff = cv2.dilate(diff, kernel, iterations=2)
#
#     contours, _ = cv2.findContours(diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     for contour in contours:
#         if cv2.contourArea(contour) > 500:
#             frame = cv2.GaussianBlur(frame, (5, 5), 2)
#
#     cv2.imshow("Frame", frame)
#     cv2.imshow("Diff", diff)
#
#     prev_frame = curr_frame.copy()
#
#     if cv2.waitKey(1) == ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# # create VideoCapture object
# cap = cv2.VideoCapture('New Project 2 [49398A1].mp4')
# if (cap.isOpened() == False):
#     print('Error while trying to open video. Plese check again...')
# # get the frame width and height
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
# # define codec and create VideoWriter object
# out = cv2.VideoWriter('out_videos/marketing_out.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width, frame_height))
# # read until end of video
# while(cap.isOpened()):
#     # capture each frame of the video
#     ret, frame = cap.read()
#     # prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     if ret == True:
#         # # вычисляем изменения между двумя соседними кадрами
#         # diff = cv2.absdiff(curr_frame, prev_frame)
#         # # извлекаем среднее значение изменений
#         # mean_diff = cv2.mean(diff)
#         # если значение больше заданного порога,
#         # то считаем, что на экране происходят быстрые изменения
#         # if mean_diff[0] > 50:
#         #     print("Эпилептический контент обнаружен!")
#         # add gaussian blurring to frame
#         frame = cv2.GaussianBlur(frame, (19, 19), 0)
#         # else:
#         #     curr_frame = frame
#         # display frame
#         cv2.imshow('Video', frame)
#         # press `q` to exit
#         if cv2.waitKey(27) & 0xFF == ord('q'):
#             break
#     # if no frame found
#     else:
#         break
# # release VideoCapture()
# cap.release()
# # close all frames and video windows
# cv2.destroyAllWindows()

# import cv2
# import subprocess
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#
# # Загрузка видео
# cap = cv2.VideoCapture('New Project 2 [49398A1].mp4')
#
# # Получение частоты кадров и размера видео
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
# # Детекция опасных кадров
# dangerous = []
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if not ret:
#         break
#     # Алгоритм детекции лиц или движения
#     is_dangerous = []
#     prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     diff = cv2.absdiff(curr_frame, prev_frame)
#     mean_diff = cv2.mean(diff)
#     if mean_diff[0] > 50:
#         print("Эпилептический контент обнаружен!")
#         is_dangerous.append(frame)
#
#     # Если кадр опасный, добавляем его в список
#     if is_dangerous:
#         dangerous.append(cap.get(cv2.CAP_PROP_POS_FRAMES))
#
# cap.release()
#
# # Обрезка видео
# for i, frame_number in enumerate(dangerous):
#     # Вырезаем кадр
#     ffmpeg_extract_subclip('New Project 2 [49398A1].mp4', frame_number/fps - 2, frame_number/fps + 2, 'dangerous_%d.mp4'%i)
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     cv2.imshow('Video', frame)

# import cv2
#
# # загружаем видео
# cap = cv2.VideoCapture('New Project 2 [49398A1].mp4')
#
# # цикл по окнам видео
# while cap.isOpened():
#     # читаем кадр
#     ret, frame = cap.read()
#     if not ret:
#         break
#     if ret == True:
#         # применяем цветокоррекцию
#         # увеличиваем насыщенность
#         # if cv2.waitKey(2) & 0xFF == ord('a'):
#         frame = cv2.convertScaleAbs(frame, alpha=2, beta=0)
#         #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         # выводим видео
#         cv2.imshow('frame', frame)
#
#         # ожидаем нажатия клавиши
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# cap.release()
# cv2.destroyAllWindows()


import cv2
import keyboard
# create VideoCapture object
cap = cv2.VideoCapture('New Project 2 [49398A1].mp4')
if (cap.isOpened() == False):
    print('Error while trying to open video. Plese check again...')
# read until end of video
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)
        if keyboard.is_pressed('b'):
            brt = 50  # задаем яркость
            frame = cv2.add(frame, brt)
            cv2.imshow('frame', frame)
        elif keyboard.is_pressed('c'):
            hue = 50  # задаем тон
            sat = 50  # задаем насыщенность
            val = 50  # задаем значение яркости
            hsv_vid = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            hsv_vid[:, :, 0] += hue
            hsv_vid[:, :, 1] += sat
            hsv_vid[:, :, 2] += val
            frame = cv2.cvtColor(hsv_vid, cv2.COLOR_HSV2BGR)
            cv2.imshow('frame', frame)

        elif keyboard.is_pressed('s'):
            gray_vid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            sepia_vid = cv2.merge((cv2.addWeighted(gray_vid, 0.5, 0, 0, 0), cv2.addWeighted(gray_vid, 0, 0.5, 0, 0),
                                   cv2.addWeighted(gray_vid, 0, 0, 0.5, 0)))
            cv2.imshow('frame', sepia_vid)

        if cv2.waitKey(27) & 0xFF == ord('q'):
            break
    else:
        break
# release VideoCapture()
cap.release()
# close all frames and video windows
cv2.destroyAllWindows()