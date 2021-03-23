# -*- coding: utf-8 -*-
__version__ = "0.3.0"
from . import kepler


# Class factory
def Map(lmax=2, nwav=1, multi=False):
    if (nwav == 1) and (not multi):
        from . import _starry_mono_64

        return _starry_mono_64.Map(lmax, nwav)
    elif (nwav == 1) and (multi):
        from . import _starry_mono_128

        return _starry_mono_128.Map(lmax, nwav)
    elif (nwav > 1) and (not multi):
        from . import _starry_spectral_64

        return _starry_spectral_64.Map(lmax, nwav)
    elif (nwav > 1) and (multi):
        from . import _starry_spectral_128

        return _starry_spectral_128.Map(lmax, nwav)
    else:
        raise ValueError("Invalid argument(s) to `Map`.")
