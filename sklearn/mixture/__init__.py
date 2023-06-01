"""
The :mod:`sklearn.mixture` module implements mixture modeling algorithms.
"""

from ._gaussian_mixture import GaussianMixture
from ._bayesian_mixture import BayesianGaussianMixture
from ._gaussian_mixture_reg import LapRegGaussianMixture

__all__ = ["GaussianMixture", "BayesianGaussianMixture", "LapRegGaussianMixture"]
