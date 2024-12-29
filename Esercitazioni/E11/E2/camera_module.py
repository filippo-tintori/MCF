import ctypes
import numpy as np
import matplotlib.pyplot as plt

URL = '/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E11/E2'

def read_camera():
    mycamera = np.ctypeslib.load_library('libmycamera.so', URL)
    width = 1536
    height = 1024
    buffer_size = width * height * 2  

    buffer = ctypes.create_string_buffer(buffer_size)

    # funzione C
    result = mycamera.read_camera(buffer)
    if result != 0:
        raise RuntimeError("Errore nella lettura dalla fotocamera")

    raw_data = np.frombuffer(buffer, dtype=np.uint8)
    image = np.zeros((height, width), dtype=np.uint16)
    for i in range(0, len(raw_data), 2):
        pixel_value = raw_data[i] + (raw_data[i + 1] << 8)
        y = (i // 2) // width
        x = (i // 2) % width
        image[y, x] = pixel_value

    return image