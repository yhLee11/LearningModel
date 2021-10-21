#main routine
"""
/image download
downloadImageURL.py
augmentatin.py
/seperate dataset train,valid
learning_model.py --> ./darknet.exe train
/darknet/backup/weights file
makeTFlite.py
/tflite_result/.tflite
"""
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
os.system('python augmentation.py')
os.system('python learning_model.py')
os.system('python makeTFlite.py')
