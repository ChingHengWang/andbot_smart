import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img1 = mpimg.imread('stinkbug.png')
plt.figure(1)
imgplot1 = plt.imshow(img1)

img2 = mpimg.imread('pikachiu.png')
plt.figure(2)
imgplot2 = plt.imshow(img2)

#lum_img=img[:,:,0]
#plt.imshow(lum_img)
#plt.imshow(lum_img, cmap="hot")

#imgplot = plt.imshow(lum_img)
#imgplot.set_cmap('spectral')