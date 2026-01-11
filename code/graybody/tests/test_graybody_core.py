# =========================
# tests/test_graybody_core.py
# =========================
from __future__ import annotations

import numpy as np
import pytest


@pytest.mark.parametrize("eps", [0.0, 0.2, 1.0])
def test_graybody_construct_valid_emissivity(Graybody, eps):
    g = Graybody(absolute_temperature=300.0, emissivity=eps)
    assert g.emissivity == eps


@pytest.mark.parametrize("eps", [-1e-6, -0.1, 1.000001, 1.1])
def test_graybody_construct_invalid_emissivity_raises(Graybody, eps):
    with pytest.raises(Exception):
        Graybody(absolute_temperature=300.0, emissivity=eps)


def test_graybody_model_is_frozen(Graybody):
    g = Graybody(absolute_temperature=300.0, emissivity=0.6)
    with pytest.raises(Exception):
        g.emissivity = 0.7
    with pytest.raises(Exception):
        g.absolute_temperature = 280.0


def test_graybody_exitance_is_emissivity_times_blackbody_exitance(Blackbody, Graybody):
    T = 300.0
    eps = 0.6

    b = Blackbody(absolute_temperature=T)
    g = Graybody(absolute_temperature=T, emissivity=eps)

    # scalar
    assert g.exitance(10.0) == pytest.approx(eps * b.exitance(10.0), rel=1e-15, abs=0.0)

    # vector
    w = np.linspace(8.0, 14.0, 7)
    assert np.allclose(g.exitance(w), eps * b.exitance(w), rtol=1e-15, atol=0.0)


def test_graybody_radiance_uses_overridden_exitance(Blackbody, Graybody):
    """
    radiance() is inherited from Blackbody, but it calls self.exitance().
    So for Graybody it should automatically incorporate emissivity via override.
    """
    T = 280.0
    eps = 0.75

    b = Blackbody(absolute_temperature=T)
    g = Graybody(absolute_temperature=T, emissivity=eps)

    w = np.array([8.0, 10.0, 12.0], dtype=np.float64)
    expected = (eps * b.exitance(w)) / np.pi
    got = g.radiance(w)

    assert isinstance(got, np.ndarray)
    assert np.allclose(got, expected, rtol=1e-15, atol=0.0)


@pytest.mark.parametrize("eps", [0.0, 1.0])
def test_graybody_emissivity_edge_cases(Blackbody, Graybody, eps):
    """
    eps=0 => should produce 0 radiance/exitance for all wavelengths
    eps=1 => should match Blackbody
    """
    T = 300.0
    w = np.linspace(8.0, 14.0, 11)

    b = Blackbody(absolute_temperature=T)
    g = Graybody(absolute_temperature=T, emissivity=eps)

    if eps == 0.0:
        assert g.exitance(10.0) == pytest.approx(0.0, abs=0.0)
        assert np.allclose(g.exitance(w), 0.0, rtol=0.0, atol=0.0)
        assert np.allclose(g.radiance(w), 0.0, rtol=0.0, atol=0.0)
    else:
        assert g.exitance(10.0) == pytest.approx(b.exitance(10.0), rel=1e-15, abs=0.0)
        assert np.allclose(g.exitance(w), b.exitance(w), rtol=1e-15, atol=0.0)
        assert np.allclose(g.radiance(w), b.radiance(w), rtol=1e-15, atol=0.0)
