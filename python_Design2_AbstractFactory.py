# coding=utf-8
#  抽象工厂（AbstractFactory）
# 定义：
#       提供一个创建一系列相关或相互依赖对象的接口。而无需制定他们具体的类
# 适用性：
#       一个系统要独立于他的产品的创建，组合和表示时
#       一个系统要由多个产品系列中的一个来配置时
#       当你要强调一系列相关的产品对象的设计以便进行开联合使用时
#       当你提供一个产品类库，只想显示他们的接口而不是实现时

import random

class PetShop:
    '''一个宠物商店'''
    def __init__(self, animal_factory=None):
        '''pet_factory就是我们的抽象工厂，我们可以随意设置'''
        self.pet_factory = animal_factory


    def show_pet(self):
        '''用它来创建和展示一个宠物抽象工厂'''
        pet = self.pet_factory.get_pet()
        print("This is a lovely", str(pet))
        print("It says", pet.speak())
        print("It eats", self.pet_factory.get_food())

# 抽象工厂生产东西
class Dog:
    def speak(self):
        return "Woof"

    def __str__(self):
        return "Dog"


class Cat:
    def speak(self):
        return "Meow"

    def __str__(self):
        return "Cat"


# 工厂级别

class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food"


class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "Cat Food"


# Create the proper family
def get_factory():
    """Let's be dynamic!"""
    return random.choice([DogFactory, CatFactory])()


# Show pets with various factories,用各式各样的工厂展示宠物
if __name__ == "__main__":
    shop = PetShop()
    for i in range(3):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("=" * 20)
