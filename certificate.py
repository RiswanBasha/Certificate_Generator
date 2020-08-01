
from PIL import ImageFont, ImageDraw, Image  
from cv2 import cv2  
import numpy as np  
import os
import csv

f = open("names.txt","r")
names_list = f.read().split("\n")
#print(names_list)



flag=True

for i in range(len(names_list)):


    name_to_print = names_list[i]
    date_to_print = "01/08/2020"   #Change this date as per requirement

    # Load image in OpenCV  
    image = cv2.imread("kct.jpg")  

    # Convert the image to RGB (OpenCV uses BGR)  
    cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  

    # Pass the image to PIL  
    pil_im = Image.fromarray(cv2_im_rgb)  

    draw = ImageDraw.Draw(pil_im)  
    # use a truetype font  
    font = ImageFont.truetype("./fonts/times.ttf", 29)      #You can change fonts from list given bottom
    font1 = ImageFont.truetype("./fonts/copperplate gothic font.ttf", 14) 

    # Draw the text 
    draw.text((450,520), name_to_print, font=font , fill='dimgrey')
    draw.text((50,350), date_to_print , font=font1, fill='white')
    
    # Get back the image to OpenCV  
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)  
    
    if flag:
        cv2.imshow('Certificate', cv2_im_processed) #Shows sample image
        flag=False
    path = ''
    cv2.imwrite('./output/'+name_to_print+'.jpg',cv2_im_processed)
    #os.startfile('output.png')
    cv2.waitKey(0)  

    cv2.destroyAllWindows()
    

'''
Other vareity of FONTS (Make sure you give proper path)

MLSJN.TTF
Lato-Black.ttf
MATURASC.TTF
OLDENGL.TTF
VIVALDII.TTF
copperplate gothic font.ttf


'''



