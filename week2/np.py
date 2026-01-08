import numpy as np

a = np.arange(32).reshape(4,1,8)


b = np.arange(48).reshape(1,6,8)

print((a*b).shape)