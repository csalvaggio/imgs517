class Graybody:
    def __init__(self, absolute_temperature, emissivity):
        self.absolute_temperature = absolute_temperature
        self.emissivity = emissivity

    def __repr__(self):
        return (f"Graybody with an emissivity of {self.emissivity} at "
                f"an absolute temperature of {self.absolute_temperature} [K]")

    def __eq__(self, other):
        if not isinstance(other, Graybody):
            return NotImplemented
        return (self.absolute_temperature == other.absolute_temperature and
                self.emissivity == other.emissivity)

    def get_absolute_temperature(self):
        return self.absolute_temperature

    def set_absolute_temperature(self, absolute_temperature):
        self.absolute_temperature = absolute_temperature

    def get_emissivity(self):
        return self.emissivity

    def set_emissivity(self, emissivity):
        self.emissivity = emissivity


if __name__ == "__main__":
    g = Graybody(300, 0.6)
    print(f"Absolute temperature = {g.get_absolute_temperature()} [K]")
    print(f"Emissivity = {g.get_emissivity()}")

    g.set_absolute_temperature(280)
    g.set_emissivity(0.75)
    print(f"Absolute temperature = {g.get_absolute_temperature()} [K]")
    print(f"Emissivity = {g.get_emissivity()}")
