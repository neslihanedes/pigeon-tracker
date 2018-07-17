import json

from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm

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
plt.hist2d(x, y, 20, norm=LogNorm())
plt.colorbar()

plt.savefig('histo.png')
plt.show()
