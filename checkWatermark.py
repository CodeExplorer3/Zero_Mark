import numpy as np
from keras.preprocessing import image
from keras.models import load_model

# Load the model
model = load_model('./rollingAvgModel.keras')

# Load image
# img_path = './RollingAverage/plainImage.jpg'
img_path = './RollingAverage/markedImage.jpg'
img = image.load_img(img_path, target_size=(28, 28))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255. 

# Make predictions
predictions = model.predict(img_array)

print(predictions)

class_labels = ['marked', 'unmarked']  # Class Labels
decoded_predictions = [class_labels[idx] for idx in np.argmax(predictions, axis=1)]

# Print the predicted class
print(decoded_predictions)