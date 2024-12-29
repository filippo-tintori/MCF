import numpy
import ctypes

URL = '/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E11/serie/serie'


_libserie = numpy.ctypeslib.load_library('libserie.so', URL)
_libserie.fibonacci.argtypes = [ctypes.c_int]
_libserie.fibonacci.restype  = ctypes.c_double

def fibonacci(n):
    return _libserie.fibonacci(int(n))