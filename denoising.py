#Filters work by convolution with a moving window called a kernel.
#Convolution is nothing but multiplication of two arrays of different sizes. 
#The image will be of one size and the kernel with be of a different size, 
#usually much smaller than image
#The input pixel is at the centre of the kernel. 
#The convolution is performed by sliding the kernel over the image, 
#usually from top left of image.
#Linear filters and non-linear filters are what I have tried to use.
#Gaussian is an example of linear filter. 
#Non-linear filters preserve edges. 
#Median filter is an example of non-linear filter. 
#NLM: https://scikit-image.org/docs/dev/auto_examples/filters/plot_nonlocal_means.htm

from skimage.restoration import denoise_nl_means, estimate_sigma
#to install skimage, pip install scikit-image. 
#to import the package you need to use import skimage.
#scikit image is an image processing library that includes alforithms for segmentation, geometric transformation, color space manipulation, analysis, filtering,
#feature detection, and more.

from skimage import img_as_ubyte, img_as_float
#avoid using astype as it violates assumptions about dtype range.
#for example float should range from 0 to 1 (or -1 to 1) but if you use 
#astype to convert to float, the values do not lie between 0 and 1. 

from matplotlib import pyplot as plt
#Matplotlib is a plotting library for the Python programming language.
#Pyplot is a Matplotlib module which provides a MATLAB-like interface.
#Pyplot is commonly used not just to generate plots and graphs but also to visualize images
#because visualizing images is nothing but plotting data in 2D. 
#to install matplotlib, pip install matplotlib.
#to import the package you need to use import matplotlib

from skimage import io
import numpy as np

img = img_as_float(io.imread("noisy_image.jpg"))
#Need to convert to float as we will be doing math on the array

from scipy import ndimage as nd
gaussian_img = nd.gaussian_filter(img, sigma=5)
plt.imsave("gaussian.jpg", gaussian_img)
#The output image is clearer but at the same time is completely blurred and we are losing information because of that,
#the edges are not preserved.


median_img = nd.median_filter(img, size=5)
plt.imsave("median.jpg", median_img)
#The output image did improve but still is not ideal.


#NLM

sigma_est = np.mean(estimate_sigma(img, multichannel=True))

patch_kw = dict(patch_size=5,      
                patch_distance=3,  
                multichannel=True)

denoise_img = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=False,
                               patch_size=5, patch_distance=3, multichannel=True)

denoise_img_as_8byte = img_as_ubyte(denoise_img)

plt.imshow(denoise_img)
#plt.imshow(denoise_img_as_8byte, cmap=plt.cm.gray, interpolation='nearest')

plt.imsave("NLM.jpg",denoise_img)
