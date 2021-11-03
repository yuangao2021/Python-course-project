# Python-course-project

This is a repository to denoise cell pictures from microscopy.
Gaussian is a linear filter. 
Median is a non-linear filter, non-linear filters preserve edges, the algorithm selects the median value of all the pixels in the selected window.


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
