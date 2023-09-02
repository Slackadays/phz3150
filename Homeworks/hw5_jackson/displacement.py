def displacement(v0: float, t: float, a: float) -> float:
    """Returns the displacement of an object given its initial velocity, time, and acceleration."""
    return (v0 * t) + (0.5 * a * (t ** 2))