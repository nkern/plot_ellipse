## plot_ellipse | Easily plot 2D ellipses with matplotlib

![Run Tests](https://github.com/nkern/plot_ellipse/workflows/Run%20Tests/badge.svg)

### v1.0.1

#### Examples:
```python
#!/usr/bin/env python
from plot_ellipse import plot_ellipse
import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()
plot_ellipse(x_cent=0, y_cent=0, semimaj=2, semimin=1, phi=np.pi/4, ax=ax)
plt.show()
```
<img src="data/fig1.png" width=300px />

or

```python
#!/usr/bin/env python
from plot_ellipse import plot_ellipse
import matplotlib.pyplot as plt
import numpy as np

C = np.array([[2, 1],[1, 4]])

fig,ax = plt.subplots()
ax.grid(True, color='k', alpha=0.5)
plot_ellipse(x_cent=0, y_cent=0, cov=C, mass_level=0.95, fill=True, ax=ax, fill_kwargs={'alpha':0.1,'c':'b'})
plot_ellipse(x_cent=0, y_cent=0, cov=C, mass_level=0.68, fill=True, ax=ax, fill_kwargs={'alpha':0.3,'c':'b'})
plt.show()
```
<img src="data/fig2.png" width=300px />


#### Features
- It can interface with plt.fill()
- It can directly take a 2x2 covariance matrix (numpy ndarray) and will plot probability contours

#### Installation
To install, simply clone this repo and run the `setup.py` script
```bash
python setup.py install
```

#### Dependencies
numpy, scipy, and matplotlib

