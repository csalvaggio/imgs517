import numpy as np

from numpy.typing import ArrayLike
from pydantic import BaseModel, Field, ConfigDict
from typing import ClassVar

class Blackbody(BaseModel):
    absolute_temperature: float = Field(
        ge=0,
        description="Absolute temperature in Kelvin [K]"
    )

    model_config = ConfigDict(frozen=True)

    _c1: ClassVar[float] = 3.74151e08   # [W / m^2 / micron]
    _c2: ClassVar[float] = 1.43879e04   # [micron K]

    def exitance(self, wavelength: ArrayLike) -> float | np.ndarray:
        """Spectral exitance [W/m^2/um] for wavelength(s) in microns"""
        w = np.asarray(wavelength, dtype=np.float64)
        if np.any(w <= 0):
            raise ValueError("Wavelength(s) must be > 0 [microns]")
        exitance = (
            self._c1 / w**5 /
            (np.exp(self._c2 / (w * self.absolute_temperature)) - 1.0)
        )
        return exitance.item() if exitance.ndim == 0 else exitance

    def radiance(self, wavelength: ArrayLike) -> float | np.ndarray:
        return self.exitance(wavelength) / np.pi

class Graybody(Blackbody):
    emissivity: float = Field(ge=0.0, le=1.0)

    model_config = ConfigDict(frozen=True)

    def exitance(self, wavelength: ArrayLike) -> float | np.ndarray:
        return self.emissivity * super().exitance(wavelength)

if __name__ == "__main__":
    wavelength = 10
    g = Graybody(absolute_temperature=300, emissivity=0.6)
    print(f"Temperature = {g.absolute_temperature}")
    print(type(g.absolute_temperature))
    print(f"Emissivity = {g.emissivity}")
    print(type(g.emissivity))
    print(g)
    print(g.radiance(wavelength))
    print(type(g.radiance(wavelength)))

    g = Graybody(absolute_temperature=280, emissivity=0.75)
    print(f"Temperature = {g.absolute_temperature}")
    print(type(g.absolute_temperature))
    print(f"Emissivity = {g.emissivity}")
    print(type(g.emissivity))
    print(g)
    print(g.radiance(wavelength))
    print(type(g.radiance(wavelength)))

    wavelengths = np.linspace(8, 14, 7)
    print(wavelengths)
    print(g.radiance(wavelengths))
    print(type(g.radiance(wavelengths)))
    print(g.radiance(wavelengths).dtype)
