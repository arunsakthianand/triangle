import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # appropriate import to draw 3d polygons
from matplotlib import style

fig = plt.figure('triangle',figsize=(10,5))
custom=plt.subplot(121,projection='3d')
x1=np.array([2,1,3])
y1=np.array([-1,-3,-4])
z1=np.array([1,-5,-4])
custom.scatter(x1,y1,z1)
A=np.array([2,-1,1])
B=np.array([1,-3,-5])
C=np.array([3,-4,-4])
# 1. create vertices from points
verts = [list(zip(x1, y1, z1))]
# 2. create 3d polygons and specify parameters
srf = Poly3DCollection(verts, alpha=.25, facecolor='#800000')
# 3. add polygon to the figure (current axes)
plt.gca().add_collection3d(srf)
custom.set_xlabel('X')
custom.set_ylabel('Y')
custom.set_zlabel('Z')

ax = fig.gca(projection='3d')
ax.text(2,-1,1, "A", color='red')
ax.text(1,-3,-5, "B", color='red')
ax.text(3,-4,-4, "C", color='red')

plt.show()
