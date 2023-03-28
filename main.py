import cv2
import keyboard
import numpy as np
cap = cv2.VideoCapture('New Project 2 [49398A1].mp4')
# cap = cv2.VideoCapture('D:/video.mp4')
ret, frame = cap.read()
prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
if (cap.isOpened() == False):
    print('Error while trying to open video. Plese check again...')
# read until end of video
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)
        print(frame)
        if keyboard.is_pressed('y'):
            brt = 50  # задаем яркость
            frame = cv2.add(frame, brt)
            cv2.imshow('frame', frame)
        elif keyboard.is_pressed('w'):
            hue = 50  # задаем тон
            sat = 50  # задаем насыщенность
            val = 50  # задаем значение яркости
            hsv_vid = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            hsv_vid[:, :, 0] += hue
            hsv_vid[:, :, 1] += sat
            hsv_vid[:, :, 2] += val
            frame = cv2.cvtColor(hsv_vid, cv2.COLOR_HSV2BGR)
            cv2.imshow('frame', frame)

        elif keyboard.is_pressed('e'):
            gray_vid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            sepia_vid = cv2.merge((cv2.addWeighted(gray_vid, 0.5, 0, 0, 0), cv2.addWeighted(gray_vid, 0, 0.5, 0, 0),
                                   cv2.addWeighted(gray_vid, 0, 0, 0.5, 0)))
            cv2.imshow('frame', sepia_vid)
        elif keyboard.is_pressed('r'):
            blur = cv2.GaussianBlur(frame, (19, 19), 0)
            cv2.imshow('frame', blur)
        elif keyboard.is_pressed('t'):
            fps = cap.get(cv2.CAP_PROP_FPS)
            cv2.imshow('frame', fps)
        elif keyboard.is_pressed('x'):
            contrast = 0.002
            brightness = 20
            frame[:, :, 2] = np.clip(contrast * frame[:, :, 2] + brightness, 0, 180)
            frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
            frame = cv2.normalize(
                frame, None, alpha=100, beta=150, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
            cv2.imshow('frame', frame)

        #ищем эпилептические кадры (не работает((()
        # curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # diff = cv2.absdiff(curr_frame, prev_frame)
        # # извлекаем среднее значение изменений
    #     mean_diff = cv2.mean(diff)
        # если значение больше заданного порога,
        # то считаем, что на экране происходят быстрые изменения
        #     if mean_diff[0] > 50:
        #         print("Эпилептический контент обнаружен!")

        #ищем эпилептические кадры 2 (не работает((()
         #     laplacian = cv2.Laplacian(frame, cv2.CV_64F).var()
        #     if laplacian > 100:
        #         alpha = 1.5  # коэффициент увеличения контрастности
        #         beta = 50  # смещение яркости
        #         frame = np.clip(alpha * frame + beta, 0, 100).astype(np.uint8)
        #     cv2.imshow('frame', frame)
        #     # здесь может быть ваш код для обработки эпилептического контента
        #         cv2.imshow("Frame", frame)

        if cv2.waitKey(27) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()