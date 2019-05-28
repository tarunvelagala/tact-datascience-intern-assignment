import numpy as np 

### Horizontally stack arrays 
a = np.arange(10).reshape(2, -1)

b = np.repeat(1, 10).reshape(2, -1)

np.concatenate([a, b], axis=1)

np.hstack([a, b])
