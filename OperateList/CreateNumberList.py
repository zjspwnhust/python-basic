for value in range(1, 5):
    print(value)  # 1,2,3,4

# 使用range()创建数字列表
numbers = list(range(2, 11, 2))
for number in numbers:
    print(number)  # 2,4,6,8,10

# 对数字列表进行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
