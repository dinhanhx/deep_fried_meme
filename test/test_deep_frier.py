import sys
import warnings
import os.path
try:
    sys.path.append('../deep_fried_meme')
    from deep_frier import deep_frier
except ImportError:
    sys.path.append('../')
    from deep_fried_meme import deep_frier


url = 'https://www.blackswandesign.com.au/wp-content/uploads/2017/07/Splash-Creative-Dark-Slider-Background-256x256.jpg'

fpath = ''

file_expectedOutput = True
if os.path.isfile('img.jpg'):
    fpath = 'img.jpg'
elif os.path.isfile('test/img.jpg'):
    fpath = 'test/img.jpg'
else:
    warnings.warn('Test subject is not found')
    file_expectedOutput = None

def test_deep_frier_ff():
    assert deep_frier(fpath, config=None, putout_scheme=['file', 'proc img', '.jpg']) == file_expectedOutput

def test_deep_frier_fu():
    assert isinstance(deep_frier(fpath, config=None, putout_scheme=['response data']), bytes) == True

def test_deep_frier_uf():
    assert deep_frier(url, config=None, putout_scheme=['file', 'proc img', '.jpg']) == file_expectedOutput

def test_deep_frier_uu():
    assert isinstance(deep_frier(url, config=None, putout_scheme=['response data']), bytes) == True
