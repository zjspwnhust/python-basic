favorite_language = {
    'zjs': 'java',
    'li': 'c',
    'zx': 'c',
}

# 遍历字典
for name, language in favorite_language.items():
    print(name + " " + language)

#遍历所有的键
for name in favorite_language.keys():
    print(name)

#按顺序遍历字典中的键
for name in sorted(favorite_language.keys()):
    print(name)

#遍历所有的值
for language in favorite_language.values():
    print(language)
    #遍历时删除重复的元素
for language in set(favorite_language.values()):
    print(language)