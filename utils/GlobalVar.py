import os
import re
import sys
import pymysql

# 全局变量
# 摄像头ID
# CAMERA_ID = 1
CAMERA_ID = 0
# 默认采集人脸数量
COLLENCT_FACE_NUM_DEFAULT = 12

# 多少次循环保存一帧图像
LOOP_FRAME = 20

# 初始化循环次数，比如统计20帧中人脸的数量，取最大值进行考勤
FR_LOOP_NUM = 20

# 将execute文件所在目录添加到根目录
def add_path_to_sys():
    # rootdir = "D:/Github/Face-Recognition-Class-Attendance-System/"
    rootdir = "."
    # rootdir = os.getcwd()
    sys.path.append(rootdir)

    return rootdir

# 连接数据库操作
def connect_to_sql():
    db = pymysql.connect(host="localhost", user="root", password="@lostprobe", database="facerecognition")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    return db, cursor

# 遍历人脸数据文件夹，并统计各人脸的图片数量
def statical_facedata_nums():
    # 人脸数据文件夹根目录
    files_dir = "./face_dataset/"

    dirs = os.listdir(files_dir)
    # 初始化字典
    files_num_dict = dict(zip(dirs, [0] * len(dirs)))

    for dir in dirs:
        for file in os.listdir(files_dir + dir):
            # 检测 jpg 或 png 文件
            if file.endswith('.jpg') or file.endswith('.png'):
                files_num_dict[dir] += 1

    return files_num_dict


if __name__ == '__main__':
    print(os.path.basename(__file__))
    files = statical_facedata_nums()
    print(files)