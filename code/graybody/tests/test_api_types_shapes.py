# =========================
# tests/test_api_types_shapes.py
# =========================
from __future__ import annotations

import numpy as np
import pytest


@pytest.mark.parametrize(
    "wavelengths",
    [
        [8.0, 10.0, 12.0],                         # list
        (8.0, 10.0, 12.0),                         # tuple
        np.array([8.0, 10.0, 12.0], dtype=float),   # ndarray float
        np.array([8, 10, 12], dtype=int),           # ndarray int
    ],
)
def test_blackbody_accepts_arraylike_inputs(Blackbody, wavelengths):
    b = Blackbody(absolute_temperature=300.0)
    y = b.exitance(wavelengths)
    assert isinstance(y, np.ndarray)
    assert y.shape == (3,)
    assert np.all(np.isfinite(y))
    assert np.all(y > 0.0)


def test_graybody_scalar_return_type_is_python_float(Graybody):
    g = Graybody(absolute_temperature=300.0, emissivity=0.6)
    y = g.radiance(10.0)
    assert isinstance(y, float)


def test_graybody_vector_return_type_is_ndarray_float64(Graybody):
    g = Graybody(absolute_temperature=300.0, emissivity=0.6)
    w = np.linspace(8.0, 14.0, 7)
    y = g.radiance(w)
    assert isinstance(y, np.ndarray)
    assert y.dtype == np.float64


def test_vector_matches_scalar_per_element(Graybody):
    """
    Ensure that the vector call is consistent with repeated scalar calls
    (common source of mistakes when special-casing scalars).
    """
    g = Graybody(absolute_temperature=280.0, emissivity=0.75)
    w = np.linspace(8.0, 14.0, 7)

    y_vec = g.radiance(w)
    y_sca = np.array([g.radiance(float(wi)) for wi in w], dtype=np.float64)

    assert isinstance(y_vec, np.ndarray)
    assert np.allclose(y_vec, y_sca, rtol=1e-15, atol=0.0)
