#-*- encoding: utf-8 -*-
import os
import json
"""고유id,한글이름,영어이름"""
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
json_data=dict()
with open(THIS_FOLDER+'/buildingInfo.json',encoding="UTF-8") as f:
    json_data=json.load(f)
    # json_data=json.dumps(json_data,ensure_ascii=False)#str type
for i,v in json_data.items():
    print(i,v)
    
