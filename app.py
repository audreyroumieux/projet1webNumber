from __future__ import division, print_function
# coding=utf-8
import os
import numpy as np
#from PIL import Image

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from gevent.wsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'models/cnn_model.h5'

# Load your trained model
model = load_model(MODEL_PATH)
model._make_predict_function()          # Necessary
print('Model loaded. Start serving...')

## You can also use pretrained model from Keras
## Check https://keras.io/applications/
#from keras.applications.resnet50 import ResNet50
#model = ResNet50(weights='imagenet')
#print('Model loaded. Check http://127.0.0.1:5000/')

#Fonction de prediction de l'image
def model_predict(img_path, model):
    img = image.load_img(img_path, grayscale = True) #grayscale transforme l'image en noir et blanc
    # Preprocessing the image
    image_mono_color = image.img_to_array(img)
    image_mono_color = image_mono_color.reshape((1, 28, 28, 1))
    #image_mono_color = np.expand_dims(image_mono_color, axis=1) #1,28,28,1
    
    preds = model.predict(image_mono_color)
    return preds


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        our_file = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(our_file.filename))
        our_file.save(file_path)
        
        # Make prediction
        preds = model_predict(file_path, model)

        # Process your result for human
        pred_class = np.argmax(preds, axis = 1)         
        return str(pred_class[0])
    return None


if __name__ == '__main__':
    # app.run(port=5002, debug=True)
    # Serve the app with gevent
    http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()