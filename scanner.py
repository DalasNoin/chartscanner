from PIL import Image
import numpy as np

nameofchart = "1v8khz"

colorfields = [(50,130,-188),(-170,100,95)]

import math
sign = lambda x: np.array([math.copysign(1,c) for c in x])
identity = lambda x : x

def comparecolor(field, color):
    x = tuple(sign(field)*color-field)
    return 0>x[0] and 0>x[1] and 0>x[2]
    
def load(path):
    return Image.open(path)

img = Image.open(nameofchart +".png")

def getchannel(img, i):
    a = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if(comparecolor(colorfields[i],img.getpixel((x,y))[:-1])):
                a.append((x,y))
    tmp = np.transpose(np.array(a))
    return tmp.astype("float64")

channelblue = getchannel(img,0)
channelred = getchannel(img,1)
def transform(array, zero = 0.6, height = 1.6, invert = True):
    array/=img.size[1]/height
    array -= zero
    if invert:
        array = -array+height
    
    return array

def save(x, name):
    np.savetxt(name,np.transpose(x.astype("float16")),fmt="%.5g", delimiter = ',',newline='\n')
    
transform(channelblue[1])    
transform(channelred[1],invert=False)

save(channelred,name=(nameofchart+"red.csv"))
save(channelblue, name=(nameofchart+"blue.csv"))
