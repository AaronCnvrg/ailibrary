"""
All rights reserved to cnvrg.io

     http://www.cnvrg.io

predict.py
==============================================================================
"""
import json
import argparse
import numpy as np

from keras.engine.saving import load_model
from keras.preprocessing.image import load_img, img_to_array

parser = argparse.ArgumentParser()
parser.add_argument('--path', action='store', dest='path', required=True, help='path to image the user wants to predict.')
parser.add_argument('--height', action='store', dest='h', required=True, help='image height.')
parser.add_argument('--width', action='store', dest='w', required=True, help='image width.')
args = parser.parse_args()

image_height, image_width = int(args.h), int(args.w)
model = load_model('model.h5')

image_path = args.path

def predict(*args):
	path = args[0]
	img = load_img(path, target_size = (image_width, image_height))
	img = img_to_array(img)
	img = np.expand_dims(img, axis = 0)

	predictions_array = model.predict(img)[0]
	print(predictions_array)
	max_value_ind = np.argmax(predictions_array)

	with open('labels_dict.json') as file:
		labels_dict = json.load(file)

	predicted_value = [(key, value) for (key, value) in labels_dict.items() if value == max_value_ind][0][0]

	print("Predicted Value: ", predicted_value)
	print("Probability: ", predictions_array[max_value_ind])



