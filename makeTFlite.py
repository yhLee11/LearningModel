import os
from tensorflow_yolov4_tflite import save_model
from tensorflow_yolov4_tflite import convert_tflite
from shutil import copyfile
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
DARKNET_FOLDER=THIS_FOLDER+'/darknet'
TFLITE_FOLDER = THIS_FOLDER+('/tensorflow_yolov4_tflite')
WEIGHTS_FOLDER = THIS_FOLDER+('/backup')#custom-yolov4-tiny-detector_best.weights
#1012다크넷 폴더 수정하기
def copy_obj_names():
    try:
        copyfile(DARKNET_FOLDER+'/obj.names',TFLITE_FOLDER+'/obj.names')
    except:
        print('[FAIL]copy obj.names file to TFLite folder')

#core/config.py -> coco.names:obj.names hardcoding함

#외부에서
def convert_weight_to_preTFLite():
    execfile('save_model.py')
    print('EXECUTE save_model.py')

def convert_preTFLite_to_TFLite():
    execfile('convert_tflite.py')
    print('EXECUTE convert_tflite.py')

copy_obj_names()
convert_weight_to_preTFLite()
convert_preTFLite_to_TFLite()
