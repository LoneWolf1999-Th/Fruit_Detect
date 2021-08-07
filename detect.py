import cv2
import numpy as np
import os
import glob
from django.shortcuts import render
from django.core.files import File
from webs.controller import color_guava,color_banana,color_papaya
from webs.controller import banana_ripe_or_raw,guava_ripe_or_raw,papaya_ripe_or_raw
import sys
from PIL import Image


image_name=sys.argv[1]
net = cv2.dnn.readNet("yolov3_custom.cfg", "yolov3_custom_6000.weights")

labelname = []
classes = []

with open("classes.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1]
                for i in net.getUnconnectedOutLayers()]

path = glob.glob(str(image_name))

for file in path:
    
    img = cv2.imread(file)
    img = cv2.resize(img, (650, 600))
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(
        img, 0.0054, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)
    
    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    with open('webs/text/data_label.txt','w') as data_label:
        for out in outs:
            for detection in out:
                scores = detection[5:]

                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.7:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        

        counts = dict()
        number_object_detected = len(boxes)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(number_object_detected):
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            crop_img = img[y:y + h, x: x + w]
            
            labelname.append(label)
            
            
            for row in labelname:
                s = "".join(map(str, row))
                data_label.write(s+'\n')
            
            if (label == 'Banana'):
                path2 = "webs/static/banana/"
                crop_img = cv2.resize(crop_img, (650, 600))
                cv2.imwrite(os.path.join(path2)+''+str(label)+'.jpg',crop_img)
                color_banana.banana_find_color(crop_img)
                banana_ripe_or_raw.banana_find_ripe_raw()
            elif (label == 'Guava'):
                path2 = "webs/static/guava/"
                crop_img = cv2.resize(crop_img, (650, 600))
                cv2.imwrite(os.path.join(path2)+''+str(label)+'.jpg',crop_img)
                color_guava.guava_find_color(crop_img)
                guava_ripe_or_raw.guava_find_ripe_raw()
            elif (label == 'Papaya'):
                path2 = "webs/static/papaya/"
                crop_img = cv2.resize(crop_img, (650, 600))
                cv2.imwrite(os.path.join(path2)+''+str(label)+'.jpg',crop_img)
                color_papaya.papaya_find_color(crop_img)
                papaya_ripe_or_raw.papaya_find_ripe_raw()
            
    data_label.close()
    


         

    
