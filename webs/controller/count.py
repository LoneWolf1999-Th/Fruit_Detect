import os

def countimage():
    path, dirs, files = next(os.walk("webs/static/banana"))
    path, dirs, files2 = next(os.walk("webs/static/guava"))
    path, dirs, files3 = next(os.walk("webs/static/papaya"))
    file_count = (len(files) + len(files2)+ len(files3))
    
    return(file_count)