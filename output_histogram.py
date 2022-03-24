import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

def output_histogram(source_path='./output_pictures/round_0/queen_0_modified.jpg', target_path='./output_pictures/histo_round_0/'):
    img = cv2.imread(source_path)
    original_hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    temp_hist = original_hist/np.float32(img.size)
    plt.bar(x=list(range(256)), height=temp_hist, label='ratio', color='steelblue', alpha=0.8)
    path_new_0 = source_path.split('/')
    path_new_1 = path_new_0[len(path_new_0) - 1].split('.')
    plt.title("Histo of " + path_new_1[0] + '.' + path_new_1[1])
    plt.xlabel("Value")
    plt.ylabel("Num")
    target_path_temp = target_path + path_new_1[0] + '_histo.' + path_new_1[1]
    plt.savefig(target_path_temp)
    #plt.show()
    print("output histo successful at {}".format(target_path_temp))


source_dir_name = './test_pictures/'
target_dir_name = './test_pictures_histogram/'

picture_list = os.listdir(source_dir_name)
print(picture_list)

for i in range(len(picture_list)):
    source_p = source_dir_name + picture_list[i]
    target_p = target_dir_name
    output_histogram(source_p, target_p)


