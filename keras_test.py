from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, TensorBoard

'''
    Load the model file you require, then compile with the options you want.
'''

from Models import sequential_simple_cnn as simple
from Options import *
from firebase import *

model = simple.get_model(img_width, img_height)

model.compile(loss='binary_crossentropy',
              optimizer='nadam',
              metrics=['accuracy','fbeta_score','recall'])

callbacks_list = [ModelCheckpoint(mdl["ckpt_filepath"], **mdl["ckpt_kwargs"]),
                     TensorBoard(mdl["tensorboard_logpath"], **mdl["tensorboard_kwargs"])]

# Saves the params before running the file
save_config(MODEL_NAME, mdl)

train_datagen = ImageDataGenerator(**mdl["train_image_kwargs"])

test_datagen = ImageDataGenerator(**mdl["test_image_kwargs"])

train_generator = train_datagen.flow_from_directory(
                            train_data_dir, **mdl["train_kwargs"])

validation_generator = test_datagen.flow_from_directory(
                            validation_data_dir, **mdl["test_kwargs"])

model.fit_generator(
        train_generator,
        samples_per_epoch=nb_train_samples,
        nb_epoch=nb_epoch,
        validation_data=validation_generator,
        nb_val_samples=nb_validation_samples,
        callbacks=callbacks_list)
        
