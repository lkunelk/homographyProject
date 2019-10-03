import matplotlib.pyplot as plt
from imageio import imread
from histogram_eq import histogram_eq

I = imread("../billboard/uoft_soldiers_tower_dark.png")
J = histogram_eq(I)

fig=plt.figure(figsize=(8, 8))
columns = 2
rows = 1
fig.add_subplot(rows, columns, 1)
plt.imshow(I, cmap='gray')
fig.add_subplot(rows, columns, 2)
plt.imshow(J, cmap='gray')
plt.show()
