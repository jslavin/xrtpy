from xrtpy.image_correction import xrt_deconvolve, xrt_remove_lightleak

__all__ = [
    "xrt_deconvolve",
    "xrt_remove_lightleak",
]

_SSW_MIRRORS = [
    "https://sohoftp.nascom.nasa.gov/solarsoft/",
    "https://hesperia.gsfc.nasa.gov/ssw/",
]
