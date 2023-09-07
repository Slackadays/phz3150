def kepler_3rd(period: float):
    """Returns the orbital distance of a planet to the Sun in AU given its orbital period in Earth days."""
    return (period / 365.25) ** (2 / 3)