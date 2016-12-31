from pifacedigitalio import PiFaceDigital
from threading import local

_active = local()


def get_piface():
    if not hasattr(_active, 'piface'):
        _active.piface = PiFaceDigital()
    return _active.piface
