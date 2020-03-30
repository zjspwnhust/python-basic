# 处理除数为0的异常
while True:
    first_number = input('please give me first number: ')
    if first_number == 'q':
        break
    second_number = input('please give me second number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("you can't divide by 0!")
    else:
        print(answer)
