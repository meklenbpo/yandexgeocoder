# Yandex Geocoder Interface

This is a Python module that will implement two basic functions to be used with
Yandex Geocoder:
- get a formalized address by X/Y coordinate pair
- get a coordinate pair by an address string

## Yandex Geocoder API key

A valid Yandex Geocoder API key is required to operate the `yandexgeocoder`
module.  

Add a new file called `credentials.py` to the root of the module with the
following sample content:

```Python

"""Secret Yandex Geocoder API key."""

APIKEY = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
```

This will import into the package and provide access to all the functionality.

