# 在列表中存储字典
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    print(alien)

# 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
for topping in pizza['toppings']:
    print(topping)

# 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username,info in users.items():
    print(username + ": " + info['first'] + ' ' + info['last'])
