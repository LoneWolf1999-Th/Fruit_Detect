import cv2
import numpy as np
from pandas.core import frame

def papaya_find_color(img):
    if img is None:
        print('Wrong path:')
    else:
        frame = cv2.resize(img, dsize=(550, 400))
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Green color
        low_raw = np.array([26,51,101])
        high_raw = np.array([39,250,220])
        raw_mask = cv2.inRange(hsv_frame, low_raw, high_raw)
        raw = cv2.bitwise_and(frame, frame, mask=raw_mask)

        # yellow color
        low_ripe = np.array([11, 33, 74])
        high_ripe = np.array([25, 186, 218])
        ripe_mask = cv2.inRange(hsv_frame, low_ripe, high_ripe)
        ripe = cv2.bitwise_and(frame, frame, mask=ripe_mask)

    cv2.imwrite('webs/color/papaya/raw_papaya.png',raw)
    cv2.imwrite('webs/color/papaya/ripe_papaya.png',ripe)
