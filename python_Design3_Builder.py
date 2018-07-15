# coding=utf-8
# 建造者模式（builder）
# 定义：
#       将一个复杂对象的构造与他的表示分离，使得同样的构造过程可以闯进啊不同的表示
# 适用性：
#      当创建复杂对象的算法应该独立于该对象的组成部分以及他们的装配方式
#      当构造过程必须允许被构造的对象有不同的表示时


# Director
class Director(object):
    def __init__(self):
        self.builder = None

    def construct_builder(self):
        self.builder.new_building()
        self.builder.buil_floor()
        self.builder.buil_size()

    def get_buildering(self):
        return self.builder.building


# 抽象建造者
class Builder(object):
    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()


# 实例化建筑者
class BuilderHouse(Builder):
    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'


class BuilderFlat(Builder):
    def build_floor(self):
        self.building.floor = 'More than One'

    def build_size(self):
        self.building.size = 'Small'


