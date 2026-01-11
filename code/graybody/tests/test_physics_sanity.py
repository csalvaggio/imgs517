# =========================
# tests/test_physics_sanity.py
# =========================
from __future__ import annotations

import numpy as np
import pytest


def test_blackbody_exitance_unimodal_and_peak_near_wien(Blackbody):
    """
    Over 8–14 µm at 300 K, the curve increases up to the Wien peak (~9.66 µm)
    and decreases after. This is a physics sanity check (not a strict unit test).
    """
    b = Blackbody(absolute_temperature=300.0)
    w = np.linspace(8.0, 14.0, 2000)
    y = b.exitance(w)

    i_peak = int(np.argmax(y))
    w_peak = float(w[i_peak])

    # Wien displacement for spectral radiance/exitance vs wavelength:
    # lambda_max [micron] ≈ 2897.771955 / T[K]
    wien_umK = 2897.771955
    w_expected = wien_umK / b.absolute_temperature

    # Tolerance is mostly sampling + floating error.
    assert w_peak == pytest.approx(w_expected, abs=0.10)

    dy = np.diff(y)
    left = dy[:i_peak]
    right = dy[i_peak:]

    # Permit tiny numerical wiggles; the overall behavior should hold strongly.
    assert np.mean(left >= 0.0) > 0.98
    assert np.mean(right <= 0.0) > 0.98


def test_peak_moves_to_shorter_wavelength_for_higher_temperature(Blackbody):
    """
    Another physics sanity check: increasing temperature shifts the peak to shorter wavelength.
    """
    b1 = Blackbody(absolute_temperature=280.0)
    b2 = Blackbody(absolute_temperature=320.0)

    w = np.linspace(6.0, 20.0, 5000)
    y1 = b1.exitance(w)
    y2 = b2.exitance(w)

    w_peak1 = float(w[int(np.argmax(y1))])
    w_peak2 = float(w[int(np.argmax(y2))])

    assert w_peak2 < w_peak1

