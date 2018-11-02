import json
import os

from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm


def plot_json(input_file, output_name):
    with open(input_file, ) as f:
        result_json = f.read()
    result = json.loads(result_json)
    x = []
    y = []
    for point in result['movements']:
        x.append(point[0])
        y.append(point[1])
    plt.plot(x, y)
    plt.savefig(output_name + '.plot.png')
    plt.hist2d(x, y, 20, norm=LogNorm())
    plt.colorbar()
    plt.savefig(output_name + '.histo.png')
    plt.show()


json_dir = "/home/kiview/Development/Pigeons/pigeon-tracker/"
json_in_dir = [x for x in os.listdir(json_dir) if x.endswith(".json")]

for json_file in json_in_dir:
    plot_json(json_dir + json_file, json_file)

