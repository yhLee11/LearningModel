# Learning Server
## Sequence
### [Seq1] Run main.py
### [Seq2] Run augmentation.py
- image augmentation from 'org_image' folder 
- save augmented images to 'aug_image' folder
### [Seq3] Run learningModel.py
- start training the model
- save model weights file
### [Seq4] Run makeTFlite.py
- make TFLite file for mobile app(android)

1. Augmentation
- image augmentation code
2. LearningModel
- train YOLOv4-tiny model with augmented images
3. MakeTFlite
- make .tflite file 
