 #-*- coding: utf-8 -*-
import os
import json
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
BUILDINGINFO_JSON = THIS_FOLDER+'/buildingInfo.json'
"""
1018 dev note
1.buildingInfo.json 파싱
2.image 폴더에 저장 및 네이밍
3.augmentation.py에 전달
"""
with open(BUILDINGINFO_JSON,'rt',encoding='UTF-8') as f:
    json_file=json.load(f)
    print(json_file)
