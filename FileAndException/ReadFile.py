# 读取整个文件
filepath = 'E:/ProPython/python-basic/123.txt'
with open(filepath) as file_object:
    content = file_object.read()
    print(content.rstrip())

#逐行读取
filepath = 'E:/ProPython/python-basic/123.txt'
with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())

#将文件内容存在一个列表中
filepath = 'E:/ProPython/python-basic/123.txt'
with open(filepath) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())