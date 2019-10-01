import matplotlib.pyplot as plt
import numpy as np
from imageio import imread
from bilinear_interp import bilinear_interp

# Load input image, choose subpixel location.
I  = imread('../billboard/peppers_grey.png')
print(type(I))
pt = np.array([[142.45, 286.73]]).T  # (x, y), where x is first row.

b = bilinear_interp(I, pt)
print(b)