import os.path
import imghdr
import urllib3
import cv2
import numpy as np

HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44'}
# User-Agent headers
# This HEADERS can be achived by going to this link
# https://www.whatismybrowser.com/detect/what-is-my-user-agent
# If you are smart and have time, https://developers.whatismybrowser.com/api/

def response_handler(response_data):
    # Should return an object that opencv can process
    data = np.array(bytearray(response_data), dtype='uint8')
    return cv2.imdecode(data, 1)

def file_handler(putin):
    # Should return an object that opencv can process
    return cv2.imread(putin, 1)

def putin_handler(putin):
    # Should check putin is file path or a direct url to an image
    # Should return an object that opencv can process
    if putin.startswith('https://'):
        http = urllib3.PoolManager()
        response = http.request('GET', putin, headers = HEADERS)
        if response.status == 200 and response.headers['Content-Type'].split('/')[0] == 'image':
            return response_handler(response.data)
        else:
            return None

    elif os.path.isfile(putin) and imghdr.what(putin) is not None:
        return file_handler(putin)

    else:
        return None
