import numpy as np
from keras.preprocessing import image
from keras.models import load_model
import sys

"""
This Script Allows a user to submit a 28x28x3 mnist image to a 
trained model for watermark detection.  The first argument is the model path
The second is the image path.
"""

if (len(sys.argv) < 2):
    print("Not Enough Arguments")
else:
    modelPath = sys.argv[1]
    imgPath = sys.argv[2]
    
    # Load the model
    model = load_model(modelPath)
    
    # Load the image
    img = image.load_img(imgPath, target_size=(28, 28))
    imgArray = image.img_to_array(img)
    imgArray = np.expand_dims(imgArray, axis=0)
    imgArray = imgArray / 255. 
    
    # Make predictions
    predictions = model.predict(imgArray)
    
    print(f"Unmarked: {(predictions[0][0]):.4f} \n  Marked: {(1 - predictions[0][0]):.4f}")
