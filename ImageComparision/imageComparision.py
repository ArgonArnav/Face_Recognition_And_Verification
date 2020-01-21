#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:40:31 2020

@author: toshitt
"""
from skimage import measure
import matplotlib.pyplot as plt 
import numpy as np
import os
import cv2


os.chdir("/home/toshitt/Desktop/ImageComparision")

def mse(imageA,imageB):
    #the function mse(mean square error)
    #sum of squared differences between two images
    #note the image must have same dimensions
    
    err = np.sum((imageA - imageB) ** 2)
    err/= (imageA.shape[0] * imageA.shape[1])
    
    
    return err


def check_orignality(imageA,imageB):
    ssim=measure.compare__ssim(imageA,imageB)
    s=ssim
    if s!=1.00 and mse!=0.00:
        
        return True
    else:
        return False
    

def compare_images(imageA,imageB,title):
    
    #computer mse and structural complexity
    
    m=mse(imageA,imageB)
    ssim = measure.compare_ssim(imageA,imageB)
    s=ssim
    
    fig=plt.figure(title)
    plt.suptitle("MSE: %.2f,SSIM: %.2f"%(m,s))
    
    #show first image
    
    ax = fig.add_subplot(1,2,1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")
    
    ax = fig.add_subplot(1,2,2)
    plt.imshow(imageB,cmap = plt.cm.gray)
    plt.imshow("off")
    
    plt.show()
    
    
front = cv2.imread("ToshittImages/toshitt1.jpeg")
tilted1 = cv2.imread("ToshittImages/toshitt2.jpeg")
tilted2 = cv2.imread("ToshittImages/toshitt3.jpeg")


front = cv2.cvtColor(front, cv2.COLOR_BGR2GRAY)
tilted1 = cv2.cvtColor(tilted1, cv2.COLOR_BGR2GRAY)
tilted2 = cv2.cvtColor(tilted2, cv2.COLOR_BGR2GRAY)


# initialize the figure
fig = plt.figure("Images")
images = ("Front", front), ("Tilted1", tilted1), ("Tilted2", tilted2)
 
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
 
# show the figure
plt.show()
 
# compare the images
compare_images(tilted1, tilted2, "Tilted2 vs Tilted2")

print(check_orignality(tilted1,tilted2))

#compare_images(tilted1, tilted2, "Tilted1 vs. Tilted2")
#compare_images(front, tilted2, "Front vs. Tilted")

