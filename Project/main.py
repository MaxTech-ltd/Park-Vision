import cv2
import pickle
import cvzone
import numpy as np

def checkParkingSpace(imgPro):

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y:y+height, x:x+width]

        try:
            count = cv2.countNonZero(imgCrop)
        except:
            count = 0
            print('exception')

        # Логика определения занятости
        if count < 200:
            color = (0, 255, 0)  # свободно
            thickness = 5
        else:
            color = (0, 0, 255)  # занято
            thickness = 2

        cv2.rectangle(img, pos, (x + width, y + height), color, thickness)


# Видео
cap = cv2.VideoCapture('carPark.mp4')

# Загрузка позиций парковочных мест
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 63, 31

while True:

    # Зацикливание видео
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()

    # Обработка изображения
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(
        imgBlur, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        25, 16
    )
    imgMedian = cv2.medianBlur(imgThreshold, 3)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    # Проверка парковки
    checkParkingSpace(imgDilate)

    # Вывод
    cv2.imshow("Parking", img)
    cv2.waitKey(1)