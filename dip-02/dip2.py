# -*- coding: utf-8 -*-
"""DIP2.ipynb

Automatically generated by Colaboratory.

"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
from google.colab.patches import cv2_imshow

# Loading image
img = cv2.imread("3-2-1_dog.png", 0)
(x, y) = img.shape
cv2_imshow(img)

# Generating the histogram
plt.hist(img)

# Generating a probability distribution
p = np.zeros(256)
for i in range(x):
  for j in range(y):
    z = img[i, j]
    p[z] = p[z] + 1

for z in range(256):
  p[z] = p[z] / float(x * y)

# Generating cumulative distribution function
P = np.zeros(256)
P[0] = p[0]
for z in range(1, 256):
  P[z] = P[z - 1] + p[z]

newimg = img.copy()
for i in range(x):
  for j in range(y):
    z = img[i, j]
    newimg[i, j] = P[z] * 255.0
cv2_imshow(newimg)

plt.hist(newimg)
