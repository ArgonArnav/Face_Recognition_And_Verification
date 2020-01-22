#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:47:34 2020

@author: toshitt
"""


import os
from scipy import signal
import cv2
import numpy as np


os.chdir("/home/toshitt/Desktop/images")

im1=cv2.imread("jp1.png",flags=cv2.IMREAD_COLOR) #(300,300,3) images
im2=cv2.imread("jp2.png",flags=cv2.IMREAD_COLOR)
pix1=im1.flatten()   # flattening to 27000,1
pix2=im2.flatten()

pix1=pix1.reshape(900,300)  #reshaping into a 2D matrix
pix2=pix2.reshape(900,300)


#cor = signal.correlate2d (pix1,pix2) --> extremely time consuming .You can try it since your computer has a gpu :)
#print(cor)
cor1 = np.corrcoef(pix1,pix2)  #Extremely fast but didn't give the same result as signal.correlate2d()

print(cor1)
 

