import numpy as np

cpath = '/opt/shared/PyCharmProjects/mv-region-embedding/data/'
file = cpath + 'poi_simi.npy'
data = np.load(file)
print(data.shape)
print(data[:10])