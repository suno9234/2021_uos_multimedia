import numpy as np
import os
from os import listdir
from os.path import isfile,join
from PIL import Image

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

data_datagen = ImageDataGenerator(
    rescale =1./255,
    rotation_range = 45,
    width_shift_range = 0.1,
    height_shift_range = 0.1,
    shear_range=0.5,
    horizontal_flip=False,
    vertical_flip = False,
    fill_mode = 'nearest'
    )

filename_in_dir = []
for root, dirs,files in os.walk('data\imgs\\nine'):
    for fname in files:
        full_fname = os.path.join(root,fname)
        filename_in_dir.append(full_fname)

for file_image in filename_in_dir:
    print (file_image)
    img  = load_img(file_image)
    x = img_to_array(img)
    x = x.reshape((1,)+x.shape)
    i=0
    for batch in data_datagen.flow(x,save_to_dir = 'data\imgs\img_copy\\nine',save_prefix='img_copy',save_format='png'):
        i+=1
        if i>6:
            break

    
