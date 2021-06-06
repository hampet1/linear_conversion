import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns




class Point:

    def __init__(self):
        self.x = random.randint(0, 100)
        self.y = random.randint(0, 100)
        self.z = random.randint(0, 100)


points_x = []
points_y = []
points_z = []

points = Point()
for i in range(100):
    planet = Point()
    points_x.append(planet.x)
    points_y.append(planet.y)
    points_z.append(planet.z)

df = pd.DataFrame({'x_coordinates': points_x, 'y_coordinates': points_y, 'z_coordinates': points_z})

new_range_x = [((i - 0) * 5000) / 100 + 0 for i in points_x]
new_range_y = [((i - 0) * 5000) / 100 + 0 for i in points_y]
new_range_z = [((i - 0) * 5000) / 100 + 0 for i in points_z]

df_new_range = pd.DataFrame({'x_coordinates': new_range_x, 'y_coordinates': new_range_y, 'z_coordinates': new_range_z})
sns.set(style="darkgrid")

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(121, projection='3d')
ax_2 = fig.add_subplot(122, projection='3d')

x = df['x_coordinates']
y = df['y_coordinates']
z = df['z_coordinates']

x_new_range = df_new_range['x_coordinates']
y_new_range = df_new_range['y_coordinates']
z_new_range = df_new_range['z_coordinates']

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax_2.set_xlabel("X")
ax_2.set_ylabel("Y")
ax_2.set_zlabel("Z")

ax.scatter(x, y, z)
ax_2.scatter(x_new_range, y_new_range, z_new_range)


fig.suptitle("rescaling the range (0-100) to the range (0-5000) - general formula: "
             "NewVal = (((OldValue - OldMin)*NewRange) / OldRange + NewMin)", fontsize=12)
plt.show()