import cv2
import numpy as np

def RGB_mod_bright(img_obj, coeff = (1, 0)):
    a = coeff[0]
    b = coeff[1]
    def trunc(val):
        if val <= 0:
            return 0
        if val >= 255:
            return 255

        return val

    return np.dstack([[[trunc(e * a + b) for e in l] for l in img_obj[:,:,0]], [[trunc(e * a + b) for e in l] for l in img_obj[:,:,1]], [[trunc(e * a + b) for e in l] for l in img_obj[:,:,2]]])

def noisy(image, noise_typ):
  if noise_typ == "gauss":
    row,col,ch= image.shape
    mean = 0
    var = 0.1
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy
  elif noise_typ == "s&p":
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    out[coords] = 1
    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    out[coords] = 0
    return out
  elif noise_typ == "poisson":
    vals = len(np.unique(image))
    vals = 2 ** np.ceil(np.log2(vals))
    noisy = np.random.poisson(image * vals) / float(vals)
    return noisy
  elif noise_typ =="speckle":
    row,col,ch = image.shape
    gauss = np.random.randn(row,col,ch)
    gauss = gauss.reshape(row,col,ch)
    noisy = image + image * gauss
    return noisy

def RGB_mod_saturation(img_obj, satuartion_mod):
    img_obj = cv2.cvtColor(img_obj, cv2.COLOR_RGB2HSV).astype('float32')
    (h, s, v) = cv2.split(img_obj)
    s = s * satuartion_mod
    s = np.clip(s,0,255)
    img_obj = cv2.merge([h,s,v])
    img_obj = cv2.cvtColor(img_obj.astype('uint8'), cv2.COLOR_HSV2RGB)
    return img_obj

def RGB_deep_fry(img_obj, bright_coeff = (1, 0), gaussian_blur = (7, 7), satuartion_mod = 1, noise_type = 'gauss'):
    # img_obj : opencv format for image
    # brightness coeff : a = bright_coeff[0]; b = bright_coeff[1]; read RGB_mod_bright()
    # gaussian_blur : kernel size
    # satuartion_mod : satuartion multiply
    # noise_type : gauss, poisson, s&p, speckle

    # Change brightness
    img_obj_ = RGB_mod_bright(img_obj, bright_coeff)

    # Add blur
    img_obj_ = cv2.GaussianBlur(img_obj, gaussian_blur, 0)

    # Add satuartion
    img_obj_ = RGB_mod_saturation(img_obj_, satuartion_mod)

    # Add noise
    img_obj_ = img_obj_.astype('float')
    img_obj_ = np.multiply(img_obj_, 1/255)
    img_obj_ = noisy(img_obj_, noise_type)
    img_obj_ = np.multiply(img_obj_, 255)
    img_obj_ = img_obj_.astype('int')
    return img_obj_
