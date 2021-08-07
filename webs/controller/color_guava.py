import cv2
import numpy as np
from pandas.core import frame
import os 
def guava_find_color(img):
    if img is None:
        print('Wrong path:')
    else:
        frame = cv2.resize(img, dsize=(550, 400))
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #ดิบ
        low_raw = np.array([39,120,115])
        high_raw = np.array([48,255,230])
        raw_mask = cv2.inRange(hsv_frame, low_raw, high_raw)
        raw = cv2.bitwise_and(frame, frame, mask=raw_mask)

        #สุก
        low_rip = np.array([22, 33, 138])
        high_ripe = np.array([38, 246, 242])
        ripe_mask = cv2.inRange(hsv_frame, low_rip, high_ripe)
        ripe = cv2.bitwise_and(frame, frame, mask=ripe_mask)


    cv2.imwrite('webs/color/guava/ripe_guava.png',ripe)
    cv2.imwrite('webs/color/guava/raw_guava.png',raw)
        
