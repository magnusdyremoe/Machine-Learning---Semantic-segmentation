import cv2
import numpy as np
import matplotlib.pyplot as plt

# For 3D plotting
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

turkey = cv2.imread('./images/0,30,roadmap.png')
turkey_rgb = cv2.cvtColor(turkey, cv2.COLOR_BGR2RGB)



# Blue color RGB channel used in Google road maps.
lower_range = np.array([170,218,255]) 
upper_range = np.array([170,218,255])

mask = cv2.inRange(turkey_rgb, lower_range, upper_range) #For some reason needs to be converted

cv2.imshow('rgb', turkey)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Run this part of the code to get a 3D color chart.
"""
r, g, b = cv2.split(turkey_rgb)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")

pixel_colors = turkey_rgb.reshape((np.shape(turkey_rgb)[0]*np.shape(turkey_rgb)[1], 3))
norm = colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()
axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
plt.show()
"""

