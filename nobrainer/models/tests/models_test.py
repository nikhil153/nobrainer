import numpy as np
import pytest
import tensorflow as tf

from nobrainer.models.highresnet import highresnet
from nobrainer.models.meshnet import meshnet
from nobrainer.models.meshnet import meshnet_vwn
from nobrainer.models.unet import unet


def model_test(model_cls, n_classes, input_shape, kwds={}):
    """Tests for models."""
    x = 10 * np.random.random(input_shape)
    y = np.random.choice([True, False], input_shape)

    # Assume every model class has n_classes and input_shape arguments.
    model = model_cls(n_classes=n_classes, input_shape=input_shape[1:], **kwds)
    model.compile(tf.train.AdamOptimizer(), 'binary_crossentropy')
    model.fit(x, y)

    actual_output = model.predict(x)
    assert actual_output.shape == x.shape[:-1] + (n_classes,)


def test_highresnet():
    model_test(highresnet, n_classes=1, input_shape=(1, 32, 32, 32, 1))


def test_meshnet():
    model_test(meshnet, n_classes=1, input_shape=(1, 32, 32, 32, 1), kwds={'receptive_field': 37})
    model_test(meshnet, n_classes=1, input_shape=(1, 32, 32, 32, 1), kwds={'receptive_field': 67})
    model_test(meshnet, n_classes=1, input_shape=(1, 32, 32, 32, 1), kwds={'receptive_field': 129})
    with pytest.raises(ValueError):
        model_test(meshnet, n_classes=1, input_shape=(1, 32, 32, 32, 1), kwds={'receptive_field': 50})


@pytest.mark.skip("this overloads memory on travis ci")
def test_meshnet_vwn():
    model_test(meshnet_vwn, n_classes=1, input_shape=(1, 32, 32, 32, 1), kwds={'receptive_field': 37})
    model_test(meshnet_vwn, n_classes=1, input_shape=(1, 32, 32, 32, 1), kwds={'receptive_field': 67})
    model_test(meshnet_vwn, n_classes=1, input_shape=(1, 32, 32, 32, 1), kwds={'receptive_field': 129})
    with pytest.raises(ValueError):
        model_test(meshnet, n_classes=1, input_shape=(1, 32, 32, 32, 1), kwds={'receptive_field': 50})


def test_unet():
    model_test(unet, n_classes=1, input_shape=(1, 32, 32, 32, 1))
