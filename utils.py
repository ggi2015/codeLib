'''
获取当前工程的路径及当前文件名
'''
import os

file_path = os.path.abspath(__file__)   #当前文件绝对路径
root_path = os.path.dirname(file_path)  #当前文件夹绝对路径
model_name = os.path.basename(file_path).split(".")[0]  #当前文件名，无后缀

print(file_path,root_path,model_name)