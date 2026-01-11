# =========================
# tests/conftest.py
# =========================
from __future__ import annotations

import importlib

import pytest


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Adjust this to match your module name / import path.
MODULE_UNDER_TEST = "graybody"  # e.g. "graybody" if graybody.py
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@pytest.fixture(scope="session")
def mod():
    """Import the module under test once for the session."""
    return importlib.import_module(MODULE_UNDER_TEST)


@pytest.fixture()
def Blackbody(mod):
    return mod.Blackbody


@pytest.fixture()
def Graybody(mod):
    return mod.Graybody
