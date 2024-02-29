# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set

class Pet():

    def __init__(self, name):
        self.name = name

    def hello(self):
        return f'{self.name} says meow'


class Cat(Pet):
    def __init__(self, name, age, typo):
        super().__init__(name)
        self.age = age
        self.typo = typo

    def eating(self):
        return f'{self.name}I\'m eating feed'


cat_1 = Pet('Bonya','seven', 'scottish')
print(cat_1.name)





# class Cat(Pet):


#
#     def __init__(self, name, age, typo, sex):
#         super().__init__(name)
#         self.age = age
#         self.typo = typo
#         self.sex = sex
#
#     def eating(self):
#         return f'{self.name}I\'m eating feed'
#
#     def drinking(self):
#         return f'{self.name} I\'m drinking water'
#
