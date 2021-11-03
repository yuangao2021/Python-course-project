# Python-course-project

This is a repository to denoise cell pictures from microscopy.

My research project requires the detection of the roundness of certain biological targets, and that demends a sharpen peripheral as well as less green liitle dots among cells when you zoom in the image. So, that's the aim of what I want to do, to denoise. Take cell nuclei for example, you can see in the input image, the nuclei is quite blurred together with the cytoplasm. So I have tried several filters to achieve a sharper nuclei peripheral. First, I use Gaussian. Gaussian is a linear filter. It is the first output image that does reduce those little green dots among the cells, but the nuclei peripheral is completely blurred, and I am losing information because of that, edges are not preserved. So, next I tried Median. Median is a non-linear filter, non-linear filters preserve edges, the algorithm selects the median value of all the pixels in the selected window. In the second image, edges are preserved, and the image is denoised. But it is still not ideal. So, I tried non-local means (NLM)filter. https://scikit-image.org/docs/dev/auto_examples/filters/plot_nonlocal_means.html. This time the last output image is an ideal one (at least for a stranger who never use python before...), it conatins the edges and gets rid of the little green dots among cells in the input image.

## Packages

scikit-image v0.18.0

matplotlib v3.3.2

scipy v1.7.1

## How to run

python denoising.py

## Input image

![image](https://github.com/yuangao2021/Python-course-project/blob/main/test_data/noisy_image.jpg)

## Output image

![image](https://github.com/yuangao2021/Python-course-project/blob/main/test_data/gaussian.jpg)

![image](https://github.com/yuangao2021/Python-course-project/blob/main/test_data/median.jpg)

![image](https://github.com/yuangao2021/Python-course-project/blob/main/test_data/NLM.jpg)
