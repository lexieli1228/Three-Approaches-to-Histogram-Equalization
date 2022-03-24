import numpy as np
import cv2
import os
import math

def my_histo_0(source_path='./test_pictures/queen_0.jpg', target_path='./output_pictures/round_0/'):
    img = cv2.imread(source_path)
    img_1 = img
    shape = img.shape
    original_hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    temp_hist = original_hist.cumsum()/np.float32(img.size)
    new_hist = (np.clip(temp_hist*255, 0, 255)).astype('uint8')

    for i in range(shape[0]):
        for j in range(shape[1]):
            img_1[i][j] = new_hist[img_1[i][j]]

    path_new_0 = source_path.split('/')
    path_new_1 = path_new_0[2].split('.')
    target_path_temp = target_path + path_new_1[0] + '_modified.' + path_new_1[1]
    cv2.imwrite(target_path_temp, img_1)
    print("output picture successful at {}".format(target_path_temp))

def my_histo_1(source_path='./test_pictures/queen_0.jpg', target_path='./output_pictures/round_0/'):
    img = cv2.imread(source_path)
    img_1 = img
    shape = img.shape
    original_hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    total = 0
    for j in range(len(original_hist)):
        original_hist[j] = math.sqrt((original_hist[j]))
        total += original_hist[j]

    temp_hist = original_hist.cumsum()/np.float32(total)
    new_hist = (np.clip(temp_hist*255, 0, 255)).astype('uint8')

    for i in range(shape[0]):
        for j in range(shape[1]):
            img_1[i][j] = new_hist[img_1[i][j]]

    path_new_0 = source_path.split('/')
    path_new_1 = path_new_0[2].split('.')
    target_path_temp = target_path + path_new_1[0] + '_modified.' + path_new_1[1]
    cv2.imwrite(target_path_temp, img_1)
    print("output picture successful at {}".format(target_path_temp))

def my_histo_2(source_path='./test_pictures/queen_0.jpg', target_path='./output_pictures/round_0/'):
    img = cv2.imread(source_path)
    img_1 = img
    shape = img.shape
    original_hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    total = 0
    for j in range(len(original_hist)):
        original_hist[j] = pow(original_hist[j], 2)
        total += original_hist[j]

    temp_hist = original_hist.cumsum()/np.float32(total)
    new_hist = (np.clip(temp_hist*255, 0, 255)).astype('uint8')

    for i in range(shape[0]):
        for j in range(shape[1]):
            img_1[i][j] = new_hist[img_1[i][j]]

    path_new_0 = source_path.split('/')
    path_new_1 = path_new_0[2].split('.')
    target_path_temp = target_path + path_new_1[0] + '_modified.' + path_new_1[1]
    cv2.imwrite(target_path_temp, img_1)
    print("output picture successful at {}".format(target_path_temp))

source_dir_name = './test_pictures/'
target_dir_name = './output_pictures/round_2/'

picture_list = os.listdir(source_dir_name)
print(picture_list)

for i in range(len(picture_list)):
    source_p = source_dir_name + picture_list[i]
    target_p = target_dir_name
    my_histo_1(source_p, target_p)


