import numpy as np
from skimage.measure import label, regionprops
import matplotlib.pyplot as plt

points = [[], [], [], [], [], []]

img = np.load("./out/h_0.npy")
img = regionprops(label(img))

points[0].append(img[0].bbox[0])
points[1].append(img[0].bbox[1])
points[2].append(img[1].bbox[0])
points[3].append(img[1].bbox[1])
points[4].append(img[2].bbox[0])
points[5].append(img[2].bbox[1])

for i in range(1, 100):
    img = np.load(f"./out/h_{i}.npy")
    img = regionprops(label(img))

    x = []
    y = []

    for l in img:
        cord = l.bbox
        x.append(cord[0])
        y.append(cord[1])

    for l in range(0, len(points), 2):
        min_x = []
        min_y = []
        for z in range(len(x)):
            min_x.append(abs(x[z] - points[l][-1]))
            min_y.append(abs(y[z] - points[l + 1][-1]))

        min2_x = min_x[0]
        min2_y = min_y[0]
        number = 0

        for z in range(1, len(min_x)):
            if (min_x[z] < min2_x or min_y[z] < min2_y) and min_x[z] < 50 and min_y[z] < 50:
                min2_x = min_x[z]
                min2_y = min_y[z]
                number = z

        points[l].append(x[number])
        points[l + 1].append(y[number])

plt.plot(points[0], points[1], label="track 1")
plt.plot(points[2], points[3], label="track 2")
plt.plot(points[4], points[5], label="track 3")
plt.legend()
plt.show()
