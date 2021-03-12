"""
A testsuite for the yandexgeocoder package.
"""

import yandexgeocoder.yandexgeocoder as yg


def test_form_a_direct_request():
    """Test how direct geocoding request is formed."""
    request_params = yg._form_a_direct_request('Россия, Псковская область, '
                                              'Невельский район, '
                                              'деревня Бойдолово')
    assert request_params == {
        'url': 'https://geocode-maps.yandex.ru/1.x',
        'params': {
            'apikey': '4adfaebf-c18c-4857-9ddc-69241c9d55b9',
            'format': 'json',
            'geocode': ('Россия, Псковская область, Невельский район, '
                        'деревня Бойдолово'),
            'results': 1
        }
    }


def test_form_a_request():
    """Test how request dictionary is formed."""
    request_params = yg._form_a_reverse_request(30.00000, 50.00000)
    assert request_params == {
        'url': 'https://geocode-maps.yandex.ru/1.x',
        'params': {
            'apikey': '4adfaebf-c18c-4857-9ddc-69241c9d55b9',
            'format': 'json',
            'geocode': '30.00000, 50.00000',
            'kind': 'locality',
            'results': 1
        }
    }


def test_xy_to_address():
    """Test basic use case for xy_to_address."""
    addr = yg.xy_to_address(30.05370, 56.03425)
    assert addr == ('Россия, Псковская область, Невельский район, '
                    'деревня Бойдолово')


def test_address_to_xy():
    """Test basic use case for xy_to_address."""
    x, y = yg.address_to_xy('Россия, Псковская область, Невельский район, '
                            'деревня Бойдолово')
    assert x == 30.054665
    assert y == 56.034974

# TODO: mock external requests
