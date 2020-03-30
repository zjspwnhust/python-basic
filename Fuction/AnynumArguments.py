# 传递任意数量的参数
def make_pizza(*toppings):
    print(toppings)


make_pizza('mushrooms', 'tomato', 'melon')  # ('mushrooms', 'tomato', 'melon')


# 传递任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {'firstname': first, 'lastname': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('zhang', 'jiesheng', location='yichun', field='math')
print(user_profile)  # {'firstname': 'zhang', 'lastname': 'jiesheng', 'location': 'yichun', 'field': 'math'}
