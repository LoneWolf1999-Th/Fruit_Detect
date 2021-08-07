from PIL import Image
from django.shortcuts import render
import os
def papaya_find_ripe_raw():
    path = 'webs/color/papaya/'
    directory= os.listdir(path)
    if len(directory) == 2:
        img = Image.open('webs/color/papaya/raw_papaya.png')
        black = 0
        papaya_raw = 0
        for pixel in img.getdata():
            if pixel == (0, 0, 0): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
                black += 1
            else:
                papaya_raw += 1
        #print('yellow='+str(yellow_raw))


        img = Image.open('webs/color/papaya/ripe_papaya.png')
        black = 0
        papaya_ripe = 0
        for pixel in img.getdata():
            if pixel == (0, 0, 0): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
                black += 1
            else:
                papaya_ripe += 1
        #print('yellow='+str(yellow_ripe))


        if (papaya_raw > papaya_ripe):
            data = 'papaya is raw'
        elif(papaya_raw < papaya_ripe):
            data = 'papaya is ripe'
        elif (papaya_raw == papaya_ripe) :
            data = 'Not image in range'
    else:
        data = 'Not image in range'

    return(data)
    