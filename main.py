import cv2
import keyboard
cap = cv2.VideoCapture('D:/vid.mp4')
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
        elif keyboard.is_pressed('n'):
            blur = cv2.GaussianBlur(frame, (19, 19), 0)
            cv2.imshow('frame', blur)

        if cv2.waitKey(27) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()