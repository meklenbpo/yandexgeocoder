"""
yandexgeocoder - Yandex Geocoder
================================

A Python module that provides two tools to access two basic Yandex
Geocoding API functions:
    - get an address from a pair of X/Y coordinates
    - get a pair of X/Y coordinates from an address in Russia.
"""

import json

import requests

import credentials as secret


URL = 'https://geocode-maps.yandex.ru/1.x'


def _form_a_direct_request(address: str) -> dict:
    """Prepare a dictionary of parameters for a direct geocoding
    request.

    Return a dictionary that can be unpacked into the requests.get().
    """
    return {
        'url': URL,
        'params': {
            'geocode': address,
            'apikey': secret.APIKEY,
            'format': 'json',
            'results': 1
        }
    }


def _form_a_reverse_request(long_x: float, lat_y: float) -> dict:
    """Prepare a dictionary of parameters for a reverse geocoding
    request.

    Return a dictionary that can be unpacked into the requests.get().
    """
    coord_str = f'{long_x:.5f}, {lat_y:.5f}'
    return {
        'url': URL,
        'params': {
            'geocode': coord_str,
            'apikey': secret.APIKEY,
            'format': 'json',
            'results': 1
        }
    }


def xy_to_address(long_x: float, lat_y: float) -> tuple:
    """Query Yandex for an address given a pair of XY coordinates.

    Returns a tuple of strings representing the geocoding results:
    1. address in Russia as a string,
    2. description of the found object (house, street, area, etc)
    3. geocoding precision level
    """
    request_params = _form_a_reverse_request(long_x, lat_y)
    r = requests.get(**request_params)
    try:
        response = r.json()
    except json.decoder.JSONDecodeError:
        return 'error'
    try:
        result = (
            response['response']['GeoObjectCollection']['featureMember']
            [0]['GeoObject']['metaDataProperty']['GeocoderMetaData']
        )
    except IndexError:
        return 'no address'
    except KeyError:
        return 'no address'
    return result['text'], result['kind'], result['precision']


def address_to_xy(address: str) -> tuple:
    """Query Yandex for coordinates of an address (in Russia).

    Return a tuple of floats, first being X (Longitude) and second
    being Y (Latitude).
    """
    request_params = _form_a_direct_request(address)
    r = requests.get(**request_params)
    try:
        response = r.json()
    except json.decoder.JSONDecodeError:
        return 'error'
    try:
        coords = (
            response['response']['GeoObjectCollection']['featureMember']
            [0]['GeoObject']['Point']['pos']
        )
    except IndexError:
        return 'not found'
    except KeyError:
        return 'not found'
    x_str, y_str = coords.split(' ')
    try:
        x = float(x_str)
        y = float(y_str)
    except ValueError:
        return 'error'
    return x, y
