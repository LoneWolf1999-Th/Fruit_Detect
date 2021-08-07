import cv2
import numpy as np
from pandas.core import frame

def banana_find_color(img):
    if img is None:
        print('Wrong path:')
    else:
        frame = cv2.resize(img, dsize=(550, 400))
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #ดิบ
        low_under_ripe = np.array([25,39,91])
        high_under_ripe = np.array([45,159,172])
        under_ripe_mask = cv2.inRange(hsv_frame, low_under_ripe, high_under_ripe)
        under_ripe = cv2.bitwise_and(frame, frame, mask=under_ripe_mask)

        #ห่าม
        low_barely_ripe = np.array([20,95,114])
        high_barely_ripe = np.array([36,222,233])
        barely_ripe_mask = cv2.inRange(hsv_frame, low_barely_ripe, high_barely_ripe)
        barely_ripe = cv2.bitwise_and(frame, frame, mask=barely_ripe_mask)

        #สุก
        low_ripe = np.array([21,179,117])
        high_ripe = np.array([34,255,255])
        ripe_mask = cv2.inRange(hsv_frame, low_ripe, high_ripe)
        ripe = cv2.bitwise_and(frame, frame, mask=ripe_mask)
        
        #หง่อม
        low_very_ripe = np.array([9,108,61])
        high_very_ripe = np.array([26,255,232])
        very_ripe_mask = cv2.inRange(hsv_frame, low_very_ripe, high_very_ripe)
        very_ripe = cv2.bitwise_and(frame, frame, mask=very_ripe_mask)

    cv2.imwrite('webs/color/banana/under_ripe_banana.png',under_ripe)
    cv2.imwrite('webs/color/banana/barely_ripe_banana.png',barely_ripe)
    cv2.imwrite('webs/color/banana/ripe_banana.png',ripe)
    cv2.imwrite('webs/color/banana/very_ripe_banana.png',very_ripe)
        
        
    