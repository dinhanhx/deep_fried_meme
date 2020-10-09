try:
    from .deep_fried_engine import RGB_deep_fry
    from .putin_handlers import putin_handler
    from .putout_handlers import file_maker, response_data_maker
except ImportError:
    from deep_fried_engine import RGB_deep_fry
    from putin_handlers import putin_handler
    from putout_handlers import file_maker, response_data_maker

def deep_frier(putin, config = None, putout_scheme = ['file', 'deep fried img', 'jpg']):
    # putin : url or file path
    # config : none or [(1, 0), (7,7), 1, 'gauss']
    # putout_scheme : ['file', 'deep fried img', 'jpg'] or ['response_data']
    img_obj = putin_handler(putin)
    if img_obj is None:
        return None
    else:
        proc_img_obj = None

        if config is None:
            proc_img_obj = RGB_deep_fry(img_obj)
        else:
            proc_img_obj = RGB_deep_fry(img_obj, config[0], congig[1], config[2], config[3])

        if putout_scheme[0] == 'file' :
            file_maker(proc_img_obj, putout_scheme[1], putout_scheme[2])
            return True
        elif putout_scheme[0] == 'response data':
            return response_data_maker(proc_img_obj)
        else:
            return None

if __name__ == '__main__':
    print(deep_frier('Hilbert.png', config = None, putout_scheme = ['file', 'proc Hilbert 1', 'jpg']))
    print('===')
    print(deep_frier('Hilbert.png', config = None, putout_scheme = ['response data']))
    print('===')
    print(deep_frier('https://upload.wikimedia.org/wikipedia/commons/2/24/Hilbert_Curve.256x256%2C16-bit_greyscale.png', config = None, putout_scheme = ['file', 'proc Hilber 2', 'jpg']))
    print('===')
    print(deep_frier('https://upload.wikimedia.org/wikipedia/commons/2/24/Hilbert_Curve.256x256%2C16-bit_greyscale.png', config = None, putout_scheme = ['response data']))
