# -*- coding: utf-8 -*-

# Class factory
def Primary(lmax=2, nwav=1, multi=False):
    if (nwav == 1) and (not multi):
        from . import _starry_mono_64

        return _starry_mono_64.kepler.Primary(lmax, nwav)
    elif (nwav == 1) and (multi):
        from . import _starry_mono_128

        return _starry_mono_128.kepler.Primary(lmax, nwav)
    elif (nwav > 1) and (not multi):
        from . import _starry_spectral_64

        return _starry_spectral_64.kepler.Primary(lmax, nwav)
    elif (nwav > 1) and (multi):
        from . import _starry_spectral_128

        return _starry_spectral_128.kepler.Primary(lmax, nwav)
    else:
        raise ValueError("Invalid argument(s) to `Primary`.")


# Class factory
def Secondary(lmax=2, nwav=1, multi=False):
    if (nwav == 1) and (not multi):
        from . import _starry_mono_64

        return _starry_mono_64.kepler.Secondary(lmax, nwav)
    elif (nwav == 1) and (multi):
        from . import _starry_mono_128

        return _starry_mono_128.kepler.Secondary(lmax, nwav)
    elif (nwav > 1) and (not multi):
        from . import _starry_spectral_64

        return _starry_spectral_64.kepler.Secondary(lmax, nwav)
    elif (nwav > 1) and (multi):
        from . import _starry_spectral_128

        return _starry_spectral_128.kepler.Secondary(lmax, nwav)
    else:
        raise ValueError("Invalid argument(s) to `Secondary`.")


# Class factory
def System(primary, *secondaries):
    if (primary.nwav == 1) and (not primary.multi):
        from . import _starry_mono_64

        return _starry_mono_64.kepler.System(primary, secondaries)
    elif (primary.nwav == 1) and (primary.multi):
        from . import _starry_mono_128

        return _starry_mono_128.kepler.System(primary, secondaries)
    elif (primary.nwav > 1) and (not primary.multi):
        from . import _starry_spectral_64

        return _starry_spectral_64.kepler.System(primary, secondaries)
    elif (primary.nwav > 1) and (primary.multi):
        from . import _starry_spectral_64

        return _starry_spectral_128.kepler.System(primary, secondaries)
    else:
        raise ValueError("Invalid argument(s) to `System`.")
