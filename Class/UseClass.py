class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + ' is now sitting')

    def roll_over(self):
        print('my dog is sitting')


my_dog = Dog('dl', 31)
print("my dog's name is " + my_dog.name)
my_dog.sit()
my_dog.roll_over()