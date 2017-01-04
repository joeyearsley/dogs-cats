'''
 Simple Functional Model for a CNN
    variables link in the functional model - easier for multi-model/obj.
'''
from keras.models import Model
from keras.layers import Input, Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D

def get_model(img_width, img_height):
    inp = Input(shape=(32,))
    conv = Convolution2D(32, 3, 3, border_mode='same')(inp)
    act_1 = Activation('relu')(conv)
    conv_1 = Convolution2D(32, 3, 3)(act_1)
    act_2 = Activation('relu')(conv_1)
    max_1 = MaxPooling2D(pool_size=(2, 2))(act_2)
    drop_1 = Dropout(0.25)(max_1)

    conv_2 = Convolution2D(32, 3, 3, border_mode='same')(drop_1))
    act_3 = Activation('relu')(conv_2)
    conv_3 = Convolution2D(32, 3, 3)(act_3)
    act_4 = Activation('relu')(conv_3)
    max_2 = MaxPooling2D(pool_size=(2, 2))(act_4)
    drop_2 = Dropout(0.25)(max_2)

    flat = Flatten()(drop_2)
    dense_1 = Dense(512)(flat)
    act_5 = Activation('relu')(dense_1)
    drop_3 = Dropout(0.5)(act_5)
    dense_2 = Dense(1)(drop_3)
    act_6 = Activation('softmax')(dense_2)

    model = Model(input=[inp], output=[act_6])

    return model
