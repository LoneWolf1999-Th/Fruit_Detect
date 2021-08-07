from PIL import Image
from django.shortcuts import render
import os
def guava_find_ripe_raw():
    path = 'webs/color/guava/'
    directory= os.listdir(path)
    if len(directory) == 2:
        img = Image.open('webs/color/guava/raw_guava.png')
        black = 0
        guava_raw = 0
        for pixel in img.getdata():
            if pixel == (0, 0, 0): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
                black += 1
            else:
                guava_raw += 1
        #print('yellow='+str(yellow_raw))


        img = Image.open('webs/color/guava/ripe_guava.png')
        black = 0
        guava_ripe = 0
        for pixel in img.getdata():
            if pixel == (0, 0, 0): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
                black += 1
            else:
                guava_ripe += 1
        #print('yellow='+str(yellow_ripe))


        if (guava_raw > guava_ripe):
            data = 'guava is raw'
        elif(guava_raw < guava_ripe):
            data = 'guava is ripe'
        elif(guava_raw == guava_ripe):
            data = 'Not image in range'
    else:
        data = 'Not image in range'

    return(data)
    