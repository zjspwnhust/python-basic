#切片
names = ['1', '2', '3', '4']
print(names[1:3]) #['2', '3']
print(names[:3]) #['1', '2', '3']
print(names[1:]) #['2', '3', '4']
print(names[-3:]) #['2', '3', '4']

#遍历切片
for name in names[:3]:
    print(name) #1,2,3

#复制列表
    #创建一个副本
names2 = names[:]
names2.append('6')
print(names2)
    #引用原来的切片
names3 = names
names3.append('5')
print(names3)
