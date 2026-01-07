class Graybody:
    def __init__(self, absolute_temperature, emissivity):
        self._absolute_temperature = absolute_temperature
        self._emissivity = emissivity

    def __repr__(self):
        return (f"Graybody with an emissivity of {self._emissivity} at "
                f"an absolute temperature of {self._absolute_temperature} [K]")

    def __eq__(self, other):
        if not isinstance(other, Graybody):
            return NotImplemented
        return (self._absolute_temperature == other._absolute_temperature and
                self._emissivity == other._emissivity)

    def absolute_temperature(self):
        return self._absolute_temperature

    def absolute_temperature(self, absolute_temperature):
        self._absolute_temperature = absolute_temperature

    def emissivity(self):
        return self._emissivity

    def emissivity(self, emissivity):
        self._emissivity = emissivity


if __name__ == "__main__":
    g = Graybody(300, 0.6)
    print(f"Absolute temperature = {g.absolute_temperature} [K]")
    print(f"Emissivity = {g.emissivity}")

    g.absolute_temperature = 280
    g.emissivity = 0.75
    print(f"Absolute temperature = {g.absolute_temperature} [K]")
    print(f"Emissivity = {g.emissivity}")
