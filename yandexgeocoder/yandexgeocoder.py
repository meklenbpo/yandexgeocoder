"""
yandexgeocoder - Yandex Geocoder
================================

A Python module that provides two tools to access two basic Yandex
Geocoding API functions:
    - get an address from a pair of X/Y coordinates
    - get a pair of X/Y coordinates from an address in Russia.
"""


def xy_to_address(x: float, y: float) -> str:
    """Query Yandex for an address given a pair of XY coordinates.

    Return an address in Russia as a string.
    """
    ...


def address_to_xy(address: str) -> tuple:
    """Query Yandex for coordinates of an address (in Russia).

    Return a tuple of floats, first being X (Longitude) and second
    being Y (Latitude).
    """
    ...
