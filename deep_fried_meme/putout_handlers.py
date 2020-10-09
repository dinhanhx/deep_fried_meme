import cv2

def file_maker(img_obj, file_name = 'deeply fried img', file_type = 'jpg'):
    cv2.imwrite(file_name+'.'+file_type, img_obj)

def response_data_maker(img_obj):
    # Should return the thing that Flask, Django can handle
    return cv2.imencode('.jpg', img_obj)[1].tostring()
