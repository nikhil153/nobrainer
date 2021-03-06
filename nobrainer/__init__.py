from distutils.version import LooseVersion

import tensorflow as tf

# For tensorflow<2.0
tf.enable_v2_behavior()

if LooseVersion(tf.__version__) < LooseVersion("1.13.1"):
    raise ValueError(
        "tensorflow>=1.13.1 must be installed but found version {}"
        .format(tf.__version__))
del LooseVersion, tf

from nobrainer._version import get_versions
__version__ = get_versions()['version']
del get_versions

import nobrainer.io
import nobrainer.layers
import nobrainer.losses
import nobrainer.metrics
import nobrainer.models
import nobrainer.prediction
import nobrainer.training
import nobrainer.transform
import nobrainer.utils
import nobrainer.volume
