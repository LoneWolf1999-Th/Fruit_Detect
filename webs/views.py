from os import name
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from subprocess import run, PIPE
import sys ,os
import detect
from webs.controller import count,data_label
from webs.controller import banana_ripe_or_raw,guava_ripe_or_raw,papaya_ripe_or_raw


# Create your views here.
def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def upimg(request):
    return render(request, 'upload.html')

def profile(request):
    return render(request, 'profile.html')


def upload(request):
    if  len(request.FILES) != 0:
        request.method == 'POST'
        image = request.FILES['image'] or None
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        fileurl = fs.open(filename)
        templateurl = fs.url(filename)
        print("file raw url:", filename)
        print("file full url:", fileurl)
        print("template url:", templateurl)
        image = run([sys.executable,'detect.py',str(fileurl)],shell=False,stdout=PIPE)
        file_count = count.countimage()
        classes_label = data_label.all_label()
        processdata = []
        allsend = []
        classes = []
        classes_label = []
        if os.stat("webs/text/data_label.txt").st_size == 0:
                send = 'Not'
                allsend.append(send)
        with open("webs/text/data_label.txt", "r") as f:
            classes = [line.strip() for line in f.readlines()]
            for x in classes:
                if x not in classes_label:
                    classes_label.append(x)  
        for i in classes_label:
            if i == 'Banana':
                send = 'Banana'
                allsend.append(send)
                data = banana_ripe_or_raw.banana_find_ripe_raw()
                processdata.append(data)
            elif i == 'Guava':
                send = 'Guava'
                allsend.append(send)
                data = guava_ripe_or_raw.guava_find_ripe_raw()
                processdata.append(data)
            elif i == 'Papaya':
                send = 'Papaya'
                allsend.append(send)
                data = papaya_ripe_or_raw.papaya_find_ripe_raw()
                processdata.append(data)
            
                
        fruit = processdata 
        
        
        return render(request, 'process.html', {'raw_url': templateurl,
                                                'file_count':file_count,
                                                'allsend': allsend,
                                                'fruit':fruit})
    else:
        return render(request, 'process.html')