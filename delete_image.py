import os
import detect
from django.shortcuts import render

def deletefile(request):

    folder = (r'webs\image')
    test = os.listdir(folder)
    for images in test:    
        if images.endswith('.jpg'):
            os.remove(os.path.join(folder, images))
            
    folder = (r'webs\image')
    test = os.listdir(folder)
    for images in test:    
        if images.endswith('.png'):
            os.remove(os.path.join(folder, images))
            
    folder_txt = (r'webs\text')
    test = os.listdir(folder_txt)
    for images in test:    
        if images.endswith('.txt'):
            os.remove(os.path.join(folder_txt, images))
            

    folder_banana = (r'webs\static\banana')
    test = os.listdir(folder_banana)
    for images in test:    
        if images.endswith('.jpg'):
            os.remove(os.path.join(folder_banana, images))
            

    folder_guava = (r'webs\static\guava')
    test = os.listdir(folder_guava)
    for images in test:   
        if images.endswith('.jpg'):
            os.remove(os.path.join(folder_guava, images))
            

    folder_papaya = (r'webs\static\papaya')
    test = os.listdir(folder_papaya)
    for images in test:
        if images.endswith('.jpg'):
            os.remove(os.path.join(folder_papaya, images))
            
    folder_color_papaya = (r'webs\color\banana')
    test = os.listdir(folder_color_papaya)
    for images in test:
        if images.endswith('.png'):
            os.remove(os.path.join(folder_color_papaya, images))
            
    folder_color_papaya = (r'webs\color\guava')
    test = os.listdir(folder_color_papaya)
    for images in test:
        if images.endswith('.png'):
            os.remove(os.path.join(folder_color_papaya, images)) 
            
    folder_color_papaya = (r'webs\color\papaya')
    test = os.listdir(folder_color_papaya)
    for images in test:
        if images.endswith('.png'):
            os.remove(os.path.join(folder_color_papaya, images))      
            
    return render(request, 'upload.html')
    