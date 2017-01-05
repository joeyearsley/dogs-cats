import pickle
import keras

def load_dataset_vars(root_path):
	# Load these from dataset location.
	train_data_dir = root_path+'/train'
	validation_data_dir = root_path+'/validation'

	with open(root_path+'/vars.pickle', 'rb') as f:
		img_width, img_height, nb_train_samples, nb_validation_samples = pickle.load(f)

	return img_width, img_height, nb_train_samples, nb_validation_samples, train_data_dir, validation_data_dir 
# Downloads the file if not found in path. Otherwise returns the path.
#def dogs_cats():
