# =========================
# tests/test_blackbody_core.py
# =========================
from __future__ import annotations

import math

import numpy as np
import pytest


def test_blackbody_construct_valid_temperature(Blackbody):
    b = Blackbody(absolute_temperature=300.0)
    assert b.absolute_temperature == 300.0


@pytest.mark.parametrize("T", [-1.0, -0.0001])
def test_blackbody_construct_invalid_temperature_raises(Blackbody, T):
    with pytest.raises(Exception):
        Blackbody(absolute_temperature=T)


def test_blackbody_model_is_frozen(Blackbody):
    b = Blackbody(absolute_temperature=300.0)
    with pytest.raises(Exception):
        b.absolute_temperature = 280.0


def test_blackbody_class_constants_exist_and_are_float(Blackbody):
    assert isinstance(Blackbody._c1, float)
    assert isinstance(Blackbody._c2, float)
    assert Blackbody._c1 > 0.0
    assert Blackbody._c2 > 0.0


def test_blackbody_exitance_scalar_returns_python_float(Blackbody):
    b = Blackbody(absolute_temperature=300.0)
    y = b.exitance(10.0)
    assert isinstance(y, float)
    assert math.isfinite(y)
    assert y > 0.0


def test_blackbody_exitance_vector_returns_ndarray_float64(Blackbody):
    b = Blackbody(absolute_temperature=300.0)
    w = np.linspace(8.0, 14.0, 7)
    y = b.exitance(w)
    assert isinstance(y, np.ndarray)
    assert y.shape == w.shape
    assert y.dtype == np.float64
    assert np.all(np.isfinite(y))
    assert np.all(y > 0.0)


@pytest.mark.parametrize(
    "bad_w",
    [
        0.0,
        -1.0,
        np.array([8.0, 0.0, 10.0]),
        np.array([-8.0, 10.0]),
    ],
)
def test_blackbody_exitance_raises_on_nonpositive_wavelength(Blackbody, bad_w):
    b = Blackbody(absolute_temperature=300.0)
    with pytest.raises(ValueError, match=r"Wavelength\(s\) must be > 0"):
        b.exitance(bad_w)


def test_blackbody_exitance_matches_closed_form_scalar(Blackbody):
    b = Blackbody(absolute_temperature=300.0)
    w = 10.0
    expected = (b._c1 / w**5) / (math.exp(b._c2 / (w * b.absolute_temperature)) - 1.0)
    got = b.exitance(w)
    assert got == pytest.approx(expected, rel=1e-12, abs=0.0)


def test_blackbody_exitance_matches_closed_form_vector(Blackbody):
    b = Blackbody(absolute_temperature=300.0)
    w = np.array([8.0, 10.0, 12.0], dtype=np.float64)
    expected = (b._c1 / w**5) / (np.exp(b._c2 / (w * b.absolute_temperature)) - 1.0)
    got = b.exitance(w)
    assert isinstance(got, np.ndarray)
    assert np.allclose(got, expected, rtol=1e-12, atol=0.0)


def test_blackbody_radiance_is_exitance_over_pi_scalar(Blackbody):
    b = Blackbody(absolute_temperature=300.0)
    w = 10.0
    rad = b.radiance(w)
    ex = b.exitance(w)
    assert isinstance(rad, float)
    assert rad == pytest.approx(ex / math.pi, rel=1e-15, abs=0.0)


def test_blackbody_radiance_is_exitance_over_pi_vector(Blackbody):
    b = Blackbody(absolute_temperature=300.0)
    w = np.linspace(8.0, 14.0, 7)
    rad = b.radiance(w)
    ex = b.exitance(w)
    assert isinstance(rad, np.ndarray)
    assert rad.dtype == np.float64
    assert np.allclose(rad, ex / np.pi, rtol=1e-15, atol=0.0)
