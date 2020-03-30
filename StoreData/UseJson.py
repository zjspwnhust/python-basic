import json

numbers = [1, 3, 5, 7, 9]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    num = json.load(f_obj)

print(num)
