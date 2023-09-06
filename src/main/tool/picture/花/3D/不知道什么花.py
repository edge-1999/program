import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

fig = plt.figure()
ax = fig.add_subplot(projection='3d')  # fig.gca(projection='3d')
# 将相位向后移动了6*pi
# [x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 20 * np.pi + 4 * np.pi)
[x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 17 * np.pi - 2 * np.pi)
p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
# 添加边缘扰动 花瓣圆润
change = np.sin(15 * t) / 150  # np.sin(15 * t) / 150  # np.sin(15 * t) / 200  # np.sin(20 * t) / 50
# 将t的参数减少，使花瓣的角度变大
u = 1 - (1 - np.mod(3.3 * t, 2 * np.pi) / np.pi) ** 4 / 2 + change
y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p))
# r = u * (x * np.sin(p) + y * np.cos(p)) * 1.5
h = u * (x * np.cos(p) - y * np.sin(p))
c = cm.get_cmap('plasma')  # Blues Reds magma Purples spring
surf = ax.plot_surface(
    r * np.cos(t), r * np.sin(t), h, rstride=1, cstride=1, cmap=c, linewidth=0, antialiased=True)
# surf = ax.plot_surface(
#     r * np.cos(t), r * np.sin(t), u * (x * np.cos(p) - y * np.sin(p)), rstride=1, cstride=1,
#     cmap=cm.gist_rainbow_r, linewidth=0, antialiased=True)

plt.show()
