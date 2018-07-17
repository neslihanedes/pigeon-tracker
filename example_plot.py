import json

import numpy as np
from matplotlib import pyplot as plt

with open('result.json') as f:
    result_json = f.read()
result = json.loads(result_json)

x = []
y = []


for point in result['movements']:
    x.append(point[0])
    y.append(point[1])
plt.plot(x, y)
plt.savefig('plot.png')

plt.show()

# # Create data
# np_x = np.asarray(x)
# np_y = np.asarray(y)
#
# # x = np.random.randn(4096)
# # y = np.random.randn(4096)
#
# # Create heatmap
# heatmap, xedges, yedges = np.histogram2d(x, y, bins=(10, 10))
# extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
#
# # Plot heatmap
# plt.clf()
# plt.title('Heatmap')
# plt.ylabel('y')
# plt.xlabel('x')
# plt.imshow(heatmap, extent=extent)
# plt.show()
