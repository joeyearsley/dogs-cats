import keras
from Utils.firebase import save_output

#Saves the latest metrics from this run into the database.
class Metrics(keras.callbacks.Callback):
    '''Callback that records events
    into Firebase
    '''
    def on_epoch_end(self, epoch, logs={}):
        save_output(logs)
