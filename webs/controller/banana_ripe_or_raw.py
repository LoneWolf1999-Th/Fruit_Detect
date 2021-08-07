from PIL import Image
from django.shortcuts import render
import os
def banana_find_ripe_raw():
    path = 'webs/color/banana/'
    directory= os.listdir(path)
    if len(directory) == 4:
        img = Image.open('webs/color/banana/under_ripe_banana.png')  #ดิบ
        black = 0
        under_ripe = 0
        for pixel in img.getdata():
            if pixel == (0, 0, 0): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
                black += 1
            else:
                under_ripe += 1
        
        img = Image.open('webs/color/banana/barely_ripe_banana.png')
        black = 0
        barely_ripe = 0
        for pixel in img.getdata():
            if pixel == (0, 0, 0): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
                black += 1
            else:
                barely_ripe += 1
        
        img = Image.open('webs/color/banana/ripe_banana.png')
        black = 0
        ripe = 0
        for pixel in img.getdata():
            if pixel == (0, 0, 0): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
                black += 1
            else:
                ripe += 1


        img = Image.open('webs/color/banana/very_ripe_banana.png')
        black = 0
        very_ripe = 0
        for pixel in img.getdata():
            if pixel == (0, 0, 0): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
                black += 1
            else:
                very_ripe += 1
        


        if (under_ripe > barely_ripe and under_ripe > ripe and under_ripe > very_ripe):
            data = 'banana is under_ripe'
        elif (barely_ripe > under_ripe and barely_ripe > ripe and barely_ripe > very_ripe):
            data = 'banana is barely_ripe'
        elif (ripe > under_ripe and ripe > barely_ripe and ripe > very_ripe):
            data = 'banana is ripe'
        elif (very_ripe > under_ripe and very_ripe > barely_ripe and very_ripe > ripe):
            data = 'banana is very_ripe'
        elif (very_ripe == under_ripe == ripe == very_ripe) :
            data = 'Not image in range'
    else:
        data = 'Not image in range'

    return(data)
    