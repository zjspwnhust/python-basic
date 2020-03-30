filepath = 'E:/ProPython/python-basic/write.txt'
with open(filepath, 'w') as file_object:
    file_object.write('I am learning\n')

# 添加到行尾
with open(filepath, 'a') as file_object:
    file_object.write('i love programing')
