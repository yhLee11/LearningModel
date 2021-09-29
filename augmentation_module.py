def create_folder(directory):#폴더생성
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('ERROR creating driectory: '+directory)
        
def check_original_pixel_coordinate(pixel_txt_path):
    try:
        with open(pixel_txt_path,'r') as f:
            #cls_num,xtop,ytop,xbottom,ybottom
            origin_bbox=list(map(int,f.read().split()))

    except:
        print('[FAIL]pixel txt file is not open'+pixel_txt_path)

    #if pixel coordinate are out of range in [0,415], fix it
    fix_bbox=copy.deepcopy(origin_bbox)
    if 0>origin_bbox[1]: fix_bbox[1]=0
    if 0>origin_bbox[2]: fix_bbox[2]=0
    if 415<origin_bbox[3]: fix_bbox[3]=415
    if 415<origin_bbox[4]: fix_bbox[4]=415

    if fix_bbox!=origin_bbox:
        try:
            with open(pixel_txt_path,'w') as f:
                fix_bbox=' '.join(map(str,fix_bbox))
                f.write(fix_bbox)
        except:
            print('[FAIL]change original pixel txt file: '+pixel_txt_path)
            with open(pixel_txt_path,'w') as f:
                f.write(origin_bbox)

def load_pixel_coordinate(pixel_txt_path):
    try:
        with open(pixel_txt_path,'r') as f:
            #cls_num,xtop,ytop,xbottom,ybottom
            bbox=list(map(int,f.read().split()))
            cls_num=bbox[0]
            xtop=bbox[1]
            ytop=bbox[2]
            xbottom=bbox[3]
            ybottom=bbox[4]
    except:
        print('[FAIL]pixel txt file is not open'+pixel_txt_path)

    return cls_num,xtop,ytop,xbottom,ybottom

def check_aug_pixel_coordinate(aug_bbox):
    xtop=aug_bbox[0].x1
    ytop=aug_bbox[0].y1
    xbottom=aug_bbox[0].x2
    ybottom=aug_bbox[0].y2

    if xtop<0: xtop=0.0
    if ytop<0: ytop=0.0
    if xbottom>415: xbottom=415.0
    if ybottom>415: ybottom=415.0
    if xtop>xbottom: xtop,xbottom=xbottom,xtop
    if ytop>ybottom: ytop,ybottom=ybottom,ytop

    bbox=[xtop,ytop,xbottom,ybottom]

    print(bbox)
    return bbox

def pixel_to_yolo(cls_num,bbox_aug):
    dw=1./IMAGE_SIZE
    dh=1./IMAGE_SIZE
    xcenter=(bbox_aug[0]+bbox_aug[2])/2.0-1
    ycenter=(bbox_aug[1]+bbox_aug[3])/2.0-1
    width=bbox_aug[2]-bbox_aug[1]#xbottom-xtop
    height=bbox_aug[3]-bbox_aug[0]#ybottom-ytop
    xcenter*=dw
    width*=dw
    ycenter*=dh
    height*=dh

    #case) out of range in (0.0 to 1.0]
    if xcenter+(width/2)>1.0:
        temp=2*(xcenter+(width/2)-1.0)+0.0001
        width-=temp
    if ycenter+(height/2)>1.0:
        temp=2*(ycenter+(height/2)-1.0)+0.0001
        height-=temp
    if xcenter-(width/2)<=0.0:
        temp=2*abs(xcenter-(width/2))+0.0001
        width-=temp
    if ycenter-(height/2)<=0.0:
        temp=2*abs(ycenter-(height/2))+0.0001
        height-=temp

    return [cls_num,xcenter,ycenter,width,height]

def save_label_pixel_to_yolo(yolo_format,save_path):
    yolo_str=' '.join(map(str,yolo_format))
    try:
        with open(save_path+'.txt','w') as f:
            f.write(yolo_str)
            print(save_path,yolo_str)
    except:
        print('[FAIL]writing yolo format coordinate at '+save_path+', yolo_str: '+yolo_str)
