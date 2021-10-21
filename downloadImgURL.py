import os
import json
import sys
import io
from urllib import request
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
BUILDINGINFO_JSON = THIS_FOLDER+'/buildingInfo.json'
IMAGE_FOLDER = THIS_FOLDER+'/image'

"""
1018 dev note
1.buildingInfo.json 파싱
2.image 폴더에 저장 및 네이밍
3.augmentation.py에 전달
"""

def create_folder(directory):#폴더생성
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('ERROR creating driectory: '+directory)

def json_parser(json_path):#json파싱
    json_file=dict()
    with open(json_path,'r',encoding='UTF-8') as f:
        json_file=json.load(f)
    # json_str=json.dumps(json_file,ensure_ascii=False,indent=4)#str type#ensure_ascii=False:한글로출력
    # print(json_str)#json내용출력
    return json_file

def download_image_from_url(json_file):#이미지 다운로드
    for key,value in json_file.items():
        img_url_list=json_file[key]['img_url']
        save_path=IMAGE_FOLDER+'/'+key
        create_folder(save_path)
        for img_url in img_url_list:
            save_name=img_url.split('let-s-take-a-walk-76161.appspot.com/o/')[1].split('?')[0]
            request.urlretrieve(img_url,save_path+'/'+save_name)
            print('save image:',save_path+'/'+save_name)

##main##
json_file=json_parser(BUILDINGINFO_JSON)
download_image_from_url(json_file)
