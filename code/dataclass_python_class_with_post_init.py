from dataclasses import dataclass

@dataclass(frozen=True)
class Graybody:
    absolute_temperature: float
    emissivity: float

    def __post_init__(self):
        if not isinstance(self.absolute_temperature, (int, float)):
            raise TypeError("Absolute temperature must be an int or float")
        if not isinstance(self.emissivity, (int, float)):
            raise TypeError("Emissivity must be an int or float")
        if self.absolute_temperature < 0:
            raise ValueError("Absolute temperature must be >= 0 [K]")
        if self.emissivity < 0 or self.emissivity > 1:
            raise ValueError("Emissivity must be between 0 and 1")
        object.__setattr__(self, "absolute_temperature",
                                 float(self.absolute_temperature))
        object.__setattr__(self, "emissivity", float(self.emissivity))

if __name__ == "__main__":
    g = Graybody(300, 0.6)
    print(f"Temperature = {g.absolute_temperature}")
    print(f"Emissivity = {g.emissivity}")

    g = Graybody(280, 0.75)
    print(f"Temperature = {g.absolute_temperature}")
    print(f"Emissivity = {g.emissivity}")
