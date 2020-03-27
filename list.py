# 创建一个列表
names = ['1', '2', '3']
cars = ['bmw', 'benz', 'toyota', 'rose']

# 修改列表中的元素
names[0] = 'z'

# 在列表中添加元素
    # 在末尾添加元素
names.append('4')
names.append(1)  # python里面没有数据类型，列表里可以添加任何元素
    # 在列表中插入元素
names.insert(0, '0')

#在列表中删除元素
    #使用del语句
del names[0]
    #使用pop()方法
poped_name = names.pop()
        #使用pop()弹出任意位置的元素
names.pop(0)
    #根据值删除元素
names.remove('3')

print(names)

#组织列表
    #使用sort()对列表进行永久排序
cars.sort()
cars.sort(reverse=True)
    #使用函数sorted()对列表进行临时排序
print(sorted(cars))
    #倒着打印列表
cars.reverse()

print(cars)
