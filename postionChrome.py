from time import sleep
from win32api import GetSystemMetrics

def setPositionChrome(width, height, count):
    width_scr, height_scr = GetSystemMetrics(0), GetSystemMetrics(1)
    index = 0
    index2 = 0
    x = width
    y = height
    for i in range(count):
        if int(width_scr/width) == index: index = 0; y = height; index2 += 1
        if int(height_scr/height) == index2: index = 0; index2 = 0  
        x_new, y_new = index*x, index2*y
        yield (x_new, y_new)
        index += 1

