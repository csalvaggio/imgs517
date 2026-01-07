import math
import numpy as np
import pytest
from pydantic import ValidationError

from graybody import Graybody


# ----------------------------
# Construction / validation
# ----------------------------

def test_construct_valid_and_coerces_types():
    g = Graybody(absolute_temperature=300, emissivity=0.6)  # int -> float
    assert isinstance(g.absolute_temperature, float)
    assert isinstance(g.emissivity, float)
    assert g.absolute_temperature == 300.0
    assert g.emissivity == 0.6


@pytest.mark.parametrize("temp", [-1, -0.0001])
def test_temperature_must_be_ge_zero(temp):
    with pytest.raises(ValidationError) as exc:
        Graybody(absolute_temperature=temp, emissivity=0.5)
    msg = str(exc.value)
    assert "absolute_temperature" in msg
    assert "greater than or equal to 0" in msg


@pytest.mark.parametrize("eps", [-0.1, -1.0])
def test_emissivity_must_be_ge_zero(eps):
    with pytest.raises(ValidationError) as exc:
        Graybody(absolute_temperature=300, emissivity=eps)
    msg = str(exc.value)
    assert "emissivity" in msg
    assert "greater than or equal to 0" in msg


@pytest.mark.parametrize("eps", [1.000001, 2.0])
def test_emissivity_must_be_le_one(eps):
    with pytest.raises(ValidationError) as exc:
        Graybody(absolute_temperature=300, emissivity=eps)
    msg = str(exc.value)
    assert "emissivity" in msg
    assert "less than or equal to 1" in msg


def test_model_is_frozen():
    g = Graybody(absolute_temperature=300, emissivity=0.6)
    # Pydantic v2 raises ValidationError for frozen models on assignment
    with pytest.raises(ValidationError) as exc:
        g.emissivity = 0.7
    assert "frozen" in str(exc.value).lower()
    assert "frozen_instance" in str(exc.value)


def test_config_is_frozen():
    assert Graybody.model_config.get("frozen") is True


# ----------------------------
# exitance() behavior
# ----------------------------

def test_exitance_scalar_returns_python_float():
    g = Graybody(absolute_temperature=300, emissivity=0.6)
    y = g.exitance(10)  # scalar in microns
    assert isinstance(y, float)
    assert y > 0.0


def test_exitance_array_returns_numpy_array_float64():
    g = Graybody(absolute_temperature=300, emissivity=0.6)
    w = np.linspace(8, 14, 7)
    y = g.exitance(w)
    assert isinstance(y, np.ndarray)
    assert y.shape == w.shape
    assert y.dtype == np.float64
    assert np.all(y > 0.0)


@pytest.mark.parametrize(
    "bad_wavelength",
    [0, -1, -0.001, [10, 0, 12], np.array([8.0, -9.0])]
)
def test_exitance_rejects_nonpositive_wavelengths(bad_wavelength):
    g = Graybody(absolute_temperature=300, emissivity=0.6)
    with pytest.raises(ValueError, match=r"Wavelength\(s\) must be > 0"):
        g.exitance(bad_wavelength)


def test_exitance_scales_linearly_with_emissivity():
    w = np.array([8.0, 10.0, 12.0], dtype=np.float64)
    g1 = Graybody(absolute_temperature=300, emissivity=0.2)
    g2 = Graybody(absolute_temperature=300, emissivity=0.8)

    y1 = g1.exitance(w)
    y2 = g2.exitance(w)

    np.testing.assert_allclose(y2 / y1, 4.0, rtol=1e-12, atol=0.0)


def test_exitance_increases_with_temperature_at_fixed_wavelength():
    w = 10.0
    g_cool = Graybody(absolute_temperature=280, emissivity=0.6)
    g_warm = Graybody(absolute_temperature=300, emissivity=0.6)
    assert g_warm.exitance(w) > g_cool.exitance(w)


def test_exitance_matches_internal_planck_constants():
    """
    Spec test: verifies exitance matches the implemented formula using _c1/_c2.
    Will fail if you change constants or equation form.
    """
    g = Graybody(absolute_temperature=300, emissivity=0.6)
    w = np.array([8.0, 10.0, 12.0], dtype=np.float64)

    expected = (
        g.emissivity * g._c1 / w**5 /
        (np.exp(g._c2 / (w * g.absolute_temperature)) - 1.0)
    )
    np.testing.assert_allclose(g.exitance(w), expected, rtol=0.0, atol=0.0)


# ----------------------------
# radiance() behavior
# ----------------------------

def test_radiance_is_exitance_over_pi_scalar():
    g = Graybody(absolute_temperature=300, emissivity=0.6)
    w = 10.0
    assert math.isclose(g.radiance(w), g.exitance(w) / math.pi, rel_tol=0.0, abs_tol=0.0)


def test_radiance_is_exitance_over_pi_array():
    g = Graybody(absolute_temperature=300, emissivity=0.6)
    w = np.linspace(8, 14, 7)
    np.testing.assert_allclose(g.radiance(w), g.exitance(w) / np.pi, rtol=0.0, atol=0.0)


def test_radiance_scalar_type_is_python_float():
    g = Graybody(absolute_temperature=300, emissivity=0.6)
    y = g.radiance(10)
    assert isinstance(y, float)
    assert y > 0.0
