
import cv2
import pickle


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)


img = cv2.imread('carParkImg.png')
width, height = 63, 31
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

while True:

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
    cv2.imshow("image", img)
    cv2.setMouseCallback("image", mouseClick)
    cv2.waitKey(1)

with open('CarParkPos', 'wb') as f:
    pickle.dump(posList, f)


'''
    cv2.rectangle(img, (113, 112), (176, 142), (255, 0, 0), 2)
    cv2.rectangle(img, (113, 18), (176, 47), (255, 0, 255), 2)
    cv2.rectangle(img, (113, 49), (176, 77), (255, 255, 255), 2)
    cv2.rectangle(img, (113, 49+31), (176, 77+31), (190, 255, 255), 2)
'''
