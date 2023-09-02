# note: I used type hints here to help ensure that logical stuff gets inputted
def acceleration(u1: float, u2: float, t1: float, t2: float) -> float:
        """Return the acceleration of an object given its initial velocity, final velocity, initial time, and final time."""
        return (u2 - u1) / (t2 - t1)
        # divide the change in velocity by the change in time to get the acceleration