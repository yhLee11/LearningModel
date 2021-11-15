import os
from tensorflow_yolov4_tflite import save_model
from tensorflow_yolov4_tflite import test
from tensorflow_yolov4_tflite import convert_tflite
from shutil import copyfile
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
DARKNET_FOLDER=THIS_FOLDER+'/darknet'
TFLITE_FOLDER = THIS_FOLDER+('/tensorflow_yolov4_tflite')
WEIGHTS_FOLDER = THIS_FOLDER+('/backup')#custom-yolov4-tiny-detector_best.weights

def copy_obj_names():
    try:
        copyfile(DARKNET_FOLDER+'/data/obj.names',TFLITE_FOLDER+'/data/obj.names')
    except:
        print('[FAIL]copy obj.names file to TFLite folder')

###############main################
copy_obj_names()
save_model.app.run(save_model.main)
