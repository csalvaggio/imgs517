from dataclasses import dataclass

@dataclass(frozen=True)
class Graybody:
    absolute_temperature: float
    emissivity: float

if __name__ == "__main__":
    g = Graybody(300.0, 0.6)
    print(f"Temperature = {g.absolute_temperature}")
    print(f"Emissivity = {g.emissivity}")

    g = Graybody(280.0, 0.75)
    print(f"Temperature = {g.absolute_temperature}")
    print(f"Emissivity = {g.emissivity}")
