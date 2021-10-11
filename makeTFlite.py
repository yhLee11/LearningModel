import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
TENS_TFLITE_FOLDER = THIS_FOLDER+('/tensorflow-yolov4-tflite')
WEIGHTS_FOLDER = THIS_FOLDER+('/backup')#custom-yolov4-tiny-detector_best.weights

def copy_weights_file():
