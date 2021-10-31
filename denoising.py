from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_ubyte, img_as_float
from matplotlib import pyplot as plt

from skimage import io
import numpy as np

img = img_as_float(io.imread("test_data/noisy_image.jpg"))

from scipy import ndimage as nd
gaussian_img = nd.gaussian_filter(img, sigma=5)
plt.imsave("gaussian.jpg", gaussian_img)


median_img = nd.median_filter(img, size=5)
plt.imsave("median.jpg", median_img)


sigma_est = np.mean(estimate_sigma(img, multichannel=True))

patch_kw = dict(patch_size=5,      
                patch_distance=3,  
                multichannel=True)

denoise_img = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=False,
                               patch_size=5, patch_distance=3, multichannel=True)

denoise_img_as_8byte = img_as_ubyte(denoise_img)

plt.imshow(denoise_img)

plt.imsave("NLM.jpg",denoise_img)
