# Learning Server
## Sequence
### [Seq1] Run main.py
- import augmentation, learningModel, makeTFlite
### [Seq2] Run augmentation.py
- image augmentation from 'org_image' folder 
- save augmented images to 'aug_image' folder
### [Seq3] Run learningModel.py
- start training the model
- save model weights file
### [Seq4] Run makeTFlite.py
- make TFLite file for mobile app(android)

## Main Program
1. Augmentation.py: image augmentation
- With augmentation_module.py
  - (func) check_original_pixel_coordinate
    - check pixel coordinates of original image
    - if coordinates range in [0,415] : pass
    - else coordinates range not in [0,415] : fix them and resave
  - (func) load_images_from_folder
    - load original image using cv2
    - return image arrays
  - (func) pixel_to_yolo 
    - convert pixel format coordinates range in [0,415] to yolo darknet format coordinates range in [0.0,1.0]
    - check converted coordinates
    - if coordinates range in [0.0,1.0] : pass
    - else coordinates range not in [0.0,1.0] : fix them  
    - return class number and darknet format coordinates
  - (func) convert_original_txt_pixel_to_yolo
     - save yolo darknet format coordinates to txt file

2. LearningModel.py
- train YOLOv4-tiny model with augmented images
3. MakeTFlite.py
- make .tflite file 

## Open Source 
1. darknet
2. tensorflow-yolov4-tflite

## Etc
