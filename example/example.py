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
