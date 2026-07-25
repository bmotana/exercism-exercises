from typing import Union, Callable

def round_return(decimals: int = 2) -> Callable:
    """
    Decorator to round the return value of a function to a specified number of decimal places.

    Args:
        decimals (int): Number of decimal places to round to. Defaults to 2.

    Returns:
        Callable: Decorated function that rounds its return value.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Union[int, float]:
            result = func(*args, **kwargs)
            if isinstance(result, (int, float)):
                return round(result, decimals)
            return result
        return wrapper
    return decorator


class SpaceAge:
    """
    A class to calculate a person's age on different planets based on seconds lived.
    """

    # Orbital periods of planets in Earth years
    ORBITAL_PERIODS = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }

    def __init__(self, seconds: float):
        """
        Initialize the SpaceAge object with the number of seconds lived.

        Args:
            seconds (float): The number of seconds lived.
        """
        self.seconds = seconds
        self.earth_years = seconds / 31557600  # Seconds in an Earth year

    def _calculate_age(self, planet: str) -> float:
        """
        Calculate age on a given planet.

        Args:
            planet (str): Name of the planet.

        Returns:
            float: Age on the specified planet.
        """
        return self.earth_years / self.ORBITAL_PERIODS[planet]

    @round_return()
    def on_mercury(self) -> float:
        """Calculate age on Mercury."""
        return self._calculate_age('mercury')

    @round_return()
    def on_venus(self) -> float:
        """Calculate age on Venus."""
        return self._calculate_age('venus')

    @round_return()
    def on_earth(self) -> float:
        """Calculate age on Earth."""
        return self._calculate_age('earth')

    @round_return()
    def on_mars(self) -> float:
        """Calculate age on Mars."""
        return self._calculate_age('mars')

    @round_return()
    def on_jupiter(self) -> float:
        """Calculate age on Jupiter."""
        return self._calculate_age('jupiter')

    @round_return()
    def on_saturn(self) -> float:
        """Calculate age on Saturn."""
        return self._calculate_age('saturn')

    @round_return()
    def on_uranus(self) -> float:
        """Calculate age on Uranus."""
        return self._calculate_age('uranus')

    @round_return()
    def on_neptune(self) -> float:
        """Calculate age on Neptune."""
        return self._calculate_age('neptune')