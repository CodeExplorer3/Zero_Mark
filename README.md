# Zero_Mark
Open Zero-Watermarking Approach to Prevent the Unauthorized Use of Images

## Usage
 - To use a pretrained model, run [checkWatermark.py](https://github.com/ZeroMark0/ZeroMark/blob/main/checkWatermark.py) with the path to the model file and the path to the image respectively.  
 - To mark images, run [prepData.py](https://github.com/ZeroMark0/ZeroMark/blob/main/prepData.py) with the desired watermarking algorithm.  To change the watermarking algorithm, to change the watermarking algorithm, edit the function called in the _markFunk_ function.
 - To train a model, run [mnistFolderKeras.pu](https://github.com/ZeroMark0/ZeroMark/blob/main/mnistFolderKeras.py). (Requires [prepData.py](https://github.com/ZeroMark0/ZeroMark/blob/main/prepData.py) to have been run)
To mark 

## Dependencies
 - Conda (Python 3.11.4)

 - TensorFlow version 2.14.0

 - Matplotlib version 3.7.1

 - scikit-learn version 1.3.0
