"""
test suite for plot_ellipse
"""
from plot_ellipse import plot_ellipse
import numpy as np
import pytest
import matplotlib
try:
    matplotlib.use('Agg')
    use_matplot = True
    from matplotlib import pyplot as plt
except:
    use_matplot = False


def test_plot():
    # no plotting, just getting plotting samples from covariance
    cov = np.array([[9., 0.], [0., 4.]])
    data1 = plot_ellipse(cov=cov, mass_level=0.68, return_data=True, theta_num=100)

    # compare against known semimaj and semimin
    mult = np.sqrt(2.279)
    data2 = plot_ellipse(semimaj=3*mult, semimin=2*mult, return_data=True, theta_num=100)

    assert np.isclose(data1, data2, atol=1e-8).all()

    # try changing theta_num
    data3 = plot_ellipse(semimaj=3*mult, semimin=2*mult, return_data=True, theta_num=200)
    assert data2.shape == (2, 100)
    assert data3.shape == (2, 200)

    # try plotting
    if use_matplot:
        # try feeding figure
        fig, ax = plt.subplots()
        plot_ellipse(ax=ax, cov=cov, mass_level=0.68, return_data=False, theta_num=1000)
        assert len(ax.lines) == 1

        # now try with semimaj and semimin and plot kwargs
        plot_ellipse(ax=ax, semimaj=3*mult, semimin=2*mult, phi=np.pi/4, return_data=False,
                     theta_num=1000, plot_kwargs=dict(ls='--', c='r', lw=3))
        assert len(ax.lines) == 2
        plt.close()

        # now try fill
        fig, ax = plt.subplots()
        plot_ellipse(ax=ax, cov=cov, mass_level=0.95, return_data=False, theta_num=1000,
                     fill=True, fill_kwargs=dict(c='b', alpha=0.5))
        plot_ellipse(ax=ax, cov=cov, mass_level=0.68, return_data=False, theta_num=1000,
                     fill=True, fill_kwargs=dict(c='b', alpha=0.75))
        assert len(ax.patches) == 2
        plt.close()

        # try generating figure
        fig = plot_ellipse(cov=cov, mass_level=0.68, return_data=False, theta_num=1000)
        assert isinstance(fig, matplotlib.figure.Figure)
        assert len(fig.axes[0].lines) > 0
        plt.close()
