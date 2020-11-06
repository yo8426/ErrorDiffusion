import numpy as np
import cv2
import matplotlib.pyplot as plt

#input
im1 = cv2.imread('newborn.tif')
plt.subplot(2,2,1)
plt.imshow(im1)
im1=im1.astype(np.double)
#rgb2gray
im1=(im1[:,:,0]+im1[:,:,1]+im1[:,:,2])/3
###############################################################################
#Floyd-Steinberg

im2=np.zeros((im1.shape[0],im1.shape[1]),dtype=int)
err=np.zeros((im1.shape[0]+2,im1.shape[1]+2),dtype=int)
err[1:im1.shape[0]+1,1:im1.shape[1]+1]=im1

#ij->ji_python
for i in range(1,im1.shape[0]):
    for j in range(1,im1.shape[1]):
        if err[i,j]<128:
            im2[i-1,j-1]=0
            e=err[i,j]
        else:
            im2[i-1,j-1]=255
            e=err[i,j]-255
        #err_effect_im2
        err[i,j+1]=err[i,j+1]+7*e/16
        err[i+1,j-1]=err[i+1,j-1]+3*e/16
        err[i+1,j]=err[i+1,j]+5*e/16
        err[i+1,j+1]=err[i+1,j+1]+e/16

plt.subplot(2,2,2)
plt.imshow(im2)

cv2.imwrite('newborn2.tif',im2)
###############################################################################
#Jarvis-Jidice-Ninke

im2=np.zeros((im1.shape[0],im1.shape[1]),dtype=int)
err=np.zeros((im1.shape[0]+4,im1.shape[1]+4),dtype=int)
err[2:im1.shape[0]+2,2:im1.shape[1]+2]=im1

for i in range(2,im1.shape[0]+2):
    for j in range(2,im1.shape[1]+2):
        if err[i,j]<128:
            im2[i-2,j-2]=0
            e=err[i,j]
        else:
            im2[i-2,j-2]=255
            e=err[i,j]-255
        err[i,j+1]=err[i,j+1]+7*e/48
        err[i,j+2]=err[i,j+2]+5*e/48
        err[i+1,j-2]=err[i+1,j-2]+3*e/48
        err[i+1,j-1]=err[i+1,j-1]+5*e/48
        err[i+1,j]=err[i+1,j]+7*e/48
        err[i+1,j+1]=err[i+1,j+1]+5*e/48
        err[i+1,j+2]=err[i+1,j+2]+3*e/48
        err[i+2,j-2]=err[i+2,j-2]+1*e/48
        err[i+2,j-1]=err[i+2,j-1]+3*e/48
        err[i+2,j]=err[i+2,j]+5*e/48
        err[i+2,j+1]=err[i+2,j+1]+3*e/48
        err[i+2,j+2]=err[i+2,j+2]+1*e/48

plt.subplot(2,2,2)
plt.imshow(im2)

cv2.imwrite('newborn3.tif',im2)
###############################################################################
#Stucki

im2=np.zeros((im1.shape[0],im1.shape[1]),dtype=int)
err=np.zeros((im1.shape[0]+4,im1.shape[1]+4),dtype=int)
err[2:im1.shape[0]+2,2:im1.shape[1]+2]=im1

for i in range(2,im1.shape[0]+2):
    for j in range(2,im1.shape[1]+2):
        if err[i,j]<128:
            im2[i-2,j-2]=0
            e=err[i,j]
        else:
            im2[i-2,j-2]=255
            e=err[i,j]-255
        err[i,j+1]=err[i,j+1]+8*e/42
        err[i,j+2]=err[i,j+2]+4*e/42
        err[i+1,j-2]=err[i+1,j-2]+2*e/42
        err[i+1,j-1]=err[i+1,j-1]+4*e/42
        err[i+1,j]=err[i+1,j]+8*e/42
        err[i+1,j+1]=err[i+1,j+1]+4*e/42
        err[i+1,j+2]=err[i+1,j+2]+2*e/42
        err[i+2,j-2]=err[i+2,j-2]+1*e/42
        err[i+2,j-1]=err[i+2,j-1]+2*e/42
        err[i+2,j]=err[i+2,j]+4*e/42
        err[i+2,j+1]=err[i+2,j+1]+2*e/42
        err[i+2,j+2]=err[i+2,j+2]+1*e/42

plt.subplot(2,2,2)
plt.imshow(im2)

cv2.imwrite('newborn4.tif',im2)
###############################################################################
