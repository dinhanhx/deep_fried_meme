import deep_fried_meme as dfm
import cv2
from matplotlib import pyplot as plt
import numpy as np

img_obj = cv2.imread('thonk.jpg')
img_obj = cv2.cvtColor(img_obj, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.imshow(img_obj)

plt.subplot(122)
plt.imshow(dfm.RGB_deep_fry(img_obj, bright_coeff = (2, 0), gaussian_blur = (3, 3), satuartion_mod = 5, noise_type = 'gauss'))
plt.show()
