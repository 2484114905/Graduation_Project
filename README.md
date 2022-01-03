# Graduation_Project
该项目主要是用于目标检测和语义分割：  
1，首先利用yolo从高清大图中检测出目标；  
2，利用openCV将检测出来的目标截取出来；  
3，利用DeepLab对截取出来的目标图片进行语义分割。
  
项目的用户界面是基于Qt for python开发的，官方文档https://doc.qt.io/qtforpython-5/。  
项目环境使用的是python虚拟环境，主要的环境如下：  
python3.6  
opencv-python==4  
tensorflow==1.15  
pymysql  
pyside2
  
可使用pycharm或conda(python包管理器)创建，具体步骤查阅anaconda（内含conda）文档和conda文档：  
https://docs.anaconda.com/anaconda/  
https://docs.conda.io/en/latest/
  
数据库表可使用sql脚本创建（project.sql）

项目用到的数据集  
链接：https://pan.baidu.com/s/1R-f15i4cXq-ilDBZ6x5UMg   
提取码：ghge   
内含：原始数据集、yolo VOC数据集、deeplab训练数据集tfrecord

最后是本人开发过程中用到的一些资源  
#YOLO VOC数据集制作博客  
https://blog.csdn.net/fovever_/article/details/102860122?spm=1001.2014.3001.5501  
https://blog.csdn.net/fovever_/article/details/102815346?spm=1001.2014.3001.5501  
https://download.csdn.net/download/fovever_/12475160?spm=1001.2014.3001.5501  
https://zongxp.blog.csdn.net/article/details/80395079
  
#YOLO python 博客  
https://towardsdatascience.com/yolo-object-detection-with-opencv-and-python-21e50ac599e9  

#DeepLab  
https://github.com/MLearing/Pytorch-DeepLab-v3-plus  

https://blog.csdn.net/ling620/article/details/105635780?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161830023216780357243970%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=161830023216780357243970&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-2-105635780.first_rank_v2_pc_rank_v29&utm_term=%E5%88%B6%E4%BD%9Cdeeplabv3%2B++%E8%AF%AD%E4%B9%89%E5%88%86%E5%89%B2%E6%95%B0%E6%8D%AE%E9%9B%86  
https://blog.csdn.net/u011974639/article/details/80948990  

https://blog.csdn.net/l641208111/article/details/105291117/?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-8&spm=1001.2101.3001.4242  
https://blog.csdn.net/PianGe_zyl/article/details/108155349  
https://github.com/tensorflow/models/tree/master/research/deeplab
  
 
#labelMe  
https://github.com/wkentaro/labelme


