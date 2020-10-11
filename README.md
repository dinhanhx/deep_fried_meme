[![Build Status](https://travis-ci.org/dinhanhx/deep_fried_meme.svg?branch=master)](https://travis-ci.org/dinhanhx/deep_fried_meme)
# Deep fried meme

A Python package to make deep fried memes.

## What are deep fried memes?

Deep fried memes are memes that have had their visual properties exaggerated and blown out for artistic effect. Some properties commonly adjusted are saturation, brightness, contrast, color balance, vibrancy, sharpness, and noise. [Ref](https://www.vice.com/en_us/article/zmm885/how-to-deep-fry-a-meme)

## Installation

Python 3

Modules:
  - opencv
  - numpy
  - urllib3

The last parameter is a dot (`.`)
```
pip install -r req.txt .
```

## Usage

```Python
from deep_fried_meme import deep_frier
```

```Python
def deep_frier(putin, config = None, putout_scheme = ['file', 'deep fried img', 'jpg']):
    # putin : url or file path
    # config : none or [(1, 0), (7,7), 1, 'gauss']
    # putout_scheme : ['file', 'deep fried img', 'jpg'] or ['response_data']

    # Will export image if putout_scheme is about file
    # Will return response data string if putout_scheme is about response data
```

## Example

`example.py`

```Python
from deep_fried_meme import deep_frier

print(deep_frier('Hilbert.png', config = None, putout_scheme = ['file', 'proc Hilbert 1', 'jpg']))
# Process an image in machine then export in machine
print('===')
print(deep_frier('Hilbert.png', config = None, putout_scheme = ['response data']))
# Process an image in machine then return response data that Flask, Django can handle
print('===')
print(deep_frier('https://upload.wikimedia.org/wikipedia/commons/2/24/Hilbert_Curve.256x256%2C16-bit_greyscale.png', config = None, putout_scheme = ['file', 'proc Hilbert 2', 'jpg']))
# Process an image from direct url then export in machine
print('===')
print(deep_frier('https://upload.wikimedia.org/wikipedia/commons/2/24/Hilbert_Curve.256x256%2C16-bit_greyscale.png', config = None, putout_scheme = ['response data']))
# Process an image from direct url then return response data that Flask, Django can handle

```
