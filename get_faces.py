import os
import cv2
import time
import face_recognition

#文件夹目录
img_dir = '/Volumes/develop/python/metriclearning/dataset/test'
# 获取文件夹中的文件
mat = {}

dirs = os.listdir(img_dir)
start_time = time.time()
for dir in dirs :
    face = []
    dir_path = os.path.join(img_dir,dir)
    if(os.path.isdir(dir_path)):
        imgs = os.listdir(dir_path)
        imgs = filter(lambda x:x.endswith('jpg'),imgs)
        for index,img in enumerate(imgs):
            img_path = os.path.join(dir_path,img)
            img_recognition = face_recognition.load_image_file(img_path)
            locations = face_recognition.face_locations(img_recognition)
            if(len(locations) == 0):
            	print('**********为从图片 %s 中找到人脸，自动删除照片*******' %img_path)
            	os.remove(img_path)
            else :
            	face.append(locations[0])
            print('正在处理 %s ' %(img_path))
    mat[dir] = face
    print('********处理文件 %s 完成'%dir)
end_time = time.time()
print('**********全部视频处理完成，共花费 %d 秒'%(end_time-start_time))
print('**********最终获取***********',mat)
