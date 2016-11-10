## plot_ellipse.py
### An easy-to-use function for plotting 2D ellipses in Python 2.7 with matplotlib.
For example:
```python
from plot_ellipse import plot_ellipse
import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()
plot_ellipse(x_cent=0, y_cent=0, semimaj=2, semimin=1, phi=np.pi/4, ax=ax)
plt.show()
```

#### Installation
To install, simply clone this repo to a directory in your PYTHONPATH
