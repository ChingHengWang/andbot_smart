import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('stinkbug.png')
imgplot = plt.imshow(img)

lum_img=img[:,:,0]
#plt.imshow(lum_img)
#plt.imshow(lum_img, cmap="hot")

imgplot = plt.imshow(lum_img)
#imgplot.set_cmap('spectral')