# 批处理人脸视频
import cv2
import os
import numpy as np
import time



# 1.属性定义

# 设置视频属性
# mov , mp4 , m4v 按照自己截取录制的视频格式进行修改
video_type = 'mov'
# 需要获取的视频前多少帧数
frame_count = 2000
# 帧数之间的间隔
frame_delay = 4
# 定义视频所在文件夹
video_dir = "/Volumes/develop/python/metriclearning/dataset/videos1"
# 定义保存视频帧的位置
video_save_dir = './images'
# 获取所有视频
videos = os.listdir(video_dir)
print( '*********共载入 %d 对视频********' %(len(videos)-1))
#print(videos)
videos = filter(lambda x:x.endswith(video_type),videos)


# 2.对视频进行处理


#花费总时间
# 对视频进行处理

#花费总时间
start_time_t = time.time()
video_count = 0
# 未能处理的视频
error_video = list()
for index,each_video in enumerate(videos) :
    # 计算运算时间
    start_time = time.time()
    end_time = 0;
    print(' 正在处理视频 %s ============>',each_video)
    c = 1 
    i = 1
    rval = True
    # 获取绝对地址
    video_src = os.path.join(video_dir,each_video)
    print( video_src)
    # 获取文件名
    each_video_name, _ = each_video.split('.')
    # 创建文件名文件
    os.mkdir(video_save_dir + '/' + each_video_name)
    # 获取文件名文件绝对路径
    each_video_save = os.path.join(video_save_dir, each_video_name) + '/'
    
    cap = cv2.VideoCapture(video_src)
    if(cap.isOpened()):
        while( rval ):
            rval , frame = cap.read()
            if(c <  frame_count ) :
                # 先保存图片 
                cv2.imwrite( each_video_save + str(i) + '.jpg' ,frame)
                i +=1
                c += 4
            else :
                end_time = time.time()
                break
         video_count +=1
    else : 
        print("\033[0;30;47***********错误信息***********\033[0m")
        print('**********未能打开 %s 视频'%each_video)
        error_video.append(each_video)
    print( ' 视频处理完成============>',each_video)
    print( ' ================花费 %d 秒 ===============' %(end_time - start_time))
    print( '\n')
    print('------------------------------------------')
    print( '\n')

    cap.release()
   

print('******所有视频处理完成，共处理 %d 个视频，总共花费 %d 秒*******' %(video_count,end_time - start_time_t))
print(' ****** 未能处理的视频有 *******')
for i in error_video:
    print(i)