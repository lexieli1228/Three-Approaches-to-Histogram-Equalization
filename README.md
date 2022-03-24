# Three-Approaches-to-Histogram-Equalization
Three Approaches to Histogram Equalization
* 笔者实现了三种方法，分别为test_x.py中的三个函数
* my_histo_0, my_histo_1, my_histo_2函数分别为三种方法，均以图片文件路径和输出路径为输入
* output_histogram.py中的output_histogram函数用于输出给定图片的直方图，以图片文件路径和输出路径为输入
* 测试图片路径：./test_pictures/
* 测试图片的原始直方图路径: ./test_pictures_histogram/
* 输出图片：./output_pictures/
  * 其中的round_0, round_1, round_2文件夹分别代表my_histo_0, my_histo_1, my_histo_2的处理结果
  * 其中的histo_round_0, histo_round_1, histo_round_2文件夹分别代表输出图片的直方图
* 运行命令：python test_x.py
* 需要提前安装：numpy, matplotlib, os, opencv, math
