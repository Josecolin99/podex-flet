# screen_adapter.py

import tkinter as tk

def _get_screen_resolution():
    """
    The function `_get_screen_resolution` returns the width and height of the
    screen resolution.
    :return: the screen resolution as a tuple of the width and height.
    """
    root = tk.Tk()
    root.withdraw()
    return root.winfo_screenwidth(), root.winfo_screenheight()

_SCREEN_WIDTH, _SCREEN_HEIGHT = _get_screen_resolution()

BASE_WIDTH, BASE_HEIGHT = 720, 1280

# Obteniendo factores de escala
SCALE_FACTOR_X = BASE_WIDTH / _SCREEN_WIDTH
SCALE_FACTOR_Y = BASE_HEIGHT / _SCREEN_HEIGHT

def adapt_size(original_size, orientation='x'):
    """
    The function `adapt_size` takes an original size and an orientation, and
    returns the adapted size based on the orientation using predefined scale
    factors.
    
    :param original_size: The original size of the object that needs to be adapted
    :param orientation: The orientation parameter specifies the direction in which
    the size should be adapted. It can have two possible values: 'x' or 'y',
    defaults to x (optional)
    :return: the adapted size of the original size based on the orientation. If the
    orientation is 'x', it returns the adapted size using the SCALE_FACTOR_X. If
    the orientation is 'y', it returns the adapted size using the SCALE_FACTOR_Y.
    """
    if orientation == 'x':
        return int(original_size * SCALE_FACTOR_X)
    else:  # orientation 'y'
        return int(original_size * SCALE_FACTOR_Y)
