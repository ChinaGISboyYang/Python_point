# coding=utf-8

'''
只是有关python设计模式的一篇文章
python的设计模式大概可分为
创建型
1. Factory Method（工厂方法）
2. Abstract Factory（抽象工厂）
3. Builder（建造者）
4. Prototype（原型）
5. Singleton（单例）

结构型
6. Adapter Class/Object（适配器）
7. Bridge（桥接）
8. Composite（组合）
9. Decorator（装饰）
10. Facade（外观）
11. Flyweight（享元）
12. Proxy（代理）
行为型

13. Interpreter（解释器）
14. Template Method（模板方法）
15. Chain of Responsibility（责任链）
16. Command（命令）
17. Iterator（迭代器）
18. Mediator（中介者）
19. Memento（备忘录）
20. Observer（观察者）
21. State（状态）
22. Strategy（策略）
23. Visitor（访问者）
'''

# Factory Method(工厂方法)
# 定义一个用于创建对象的接口，让子类决定实例化哪一个类。它使一个类的实例化延迟到其子类
# 适用性：
#    当一个类不知道她所必需创建的对象的类的时候
#    当一个类希望它的子类来指定它所创建的对象的时候
#    当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候
# 实现：
'''ExampleCode 1:
class ChinaGetter:
    A simple localizer a la gettext,一个初始对象（定位器
    def __init__(self):
        self.trans = dict(dog=u"小狗", cat=u"小猫")

    def get(self, msgid):
    We'll punt if we don't have a translation
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)

class EnglishGetter:
    """Simply echoes the msg ids"""
    def get(self,msgid):
        return str(msgid)


def get_localizer(language = "English"):
    工厂模式
    languages = dict(English = EnglishGetter, China = ChinaGetter)
    return languages[language]()


# 创建我们的localizer
e, g = get_localizer("English"), get_localizer("China")

for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))
'''
# ExampleCode 2

'''
class ShapeFactory(object):
    工厂类
    def getShape(self):
        return self.shape_name

class Circle(ShapeFactory):

    def __init__(self):
        self.shape_name = "Circle"
    def draw(self):
        print('draw circle')

class Rectangle(ShapeFactory):
    def __init__(self):
        self.shape_name = "Retangle"

    def draw(self):
        print('draw Rectangle')


class ShapeInterfaceFactory(object):
    接口基类
    def create(self):
    把要创建的工厂对象装配进来
        raise  NotImplementedError

class ShapeCircle(ShapeInterfaceFactory):
    def create(self):
        return Circle()


class ShapeRectangle(ShapeInterfaceFactory):
    def create(self):
        return Rectangle()


shape_interface = ShapeCircle()
obj = shape_interface.create()
obj.getShape()
obj.draw()

shape_interface2 = ShapeRectangle()
obj2 = shape_interface2.create()
obj2.draw()
'''

'''
工厂方法模式是简单工厂模式的衍生，解决了许多简单工厂模式的问题。
首先完全实现‘开－闭 原则’，实现了可扩展。其次更复杂的层次结构，可以应用于产品结果复杂的场合。 　　
工厂方法模式的对简单工厂模式进行了抽象。有一个抽象的Factory类（可以是抽象类和接口），这个类将不在负责具体的产品生产，而是只制定一些规范，具体的生产工作由其子类去完成。在这个模式中，工厂类和产品类往往可以依次对应。即一个抽象工厂对应一个抽象产品，一个具体工厂对应一个具体产品，这个具体的工厂就负责生产对应的产品。 　　
工厂方法模式(Factory Method pattern)是最典型的模板方法模式(Templete Method pattern)应用。


'''


class AbstractSchool(object):
    name = ''
    addr = ''
    principal = ''

    def enroll(self, name, course):
        pass

    def info(self):
        pass


class AbstractCourse(object):
    def __init__(self, name, time_range, study_type, fee):
        self.name = name
        self.time_range = time_range
        self.study_type = study_type
        self.fee = fee

    def enroll_test(self):
        '''
        参加这门课程前需要进行的测试
        :return:
        '''
        print("课程[%s]测试中..." % self.name)

    def print_course_outline(self):
        '''打印课程大纲'''
        pass


class LinuxOPSCourse(AbstractCourse):
    '''
    运维课程
    '''

    def print_course_outline(self):
        outline = '''
        Linux 基础
        Linux 基本服务使用
        Linux 高级服务篇
        Linux Shell编程
        '''
        print(outline)

    def enroll_test(self):
        print("不用测试,是个人就能学...")


class PythonCourse(AbstractCourse):
    '''python自动化开发课程'''

    def  print_course_outline(self):
        outline = '''
        python 介绍
        python 基础语法
        python 函数式编程
        python 面向对象
        python 网络编程
        python web开发基础
        '''
        print(outline)

    def enroll_test(self):
        print("-------python入学测试-------")
        print("-------500道题答完了-------")
        print("-------通过了-------")


class BJSchool(AbstractSchool):
    name = "老男孩北京校区"

    def create_course(self, course_type):
        if course_type == 'py_ops':
            course = PythonCourse("Python自动化开发",
                                  7, '面授', 11000)
        elif course_type == 'linux':
            course = LinuxOPSCourse("Linux运维课程",
                                    5, '面授', 12800)
        return course

    def enroll(self, name, course):
        print("开始为新学员[%s]办入学手续... " % name)
        print("帮学员[%s]注册课程[%s]..." % (name, course))
        course.enroll_test()

    def info(self):
        print("------[%s]-----" % self.name)


class SHSchool(AbstractSchool):
    name = "老男孩上海分校"

    def create_course(self, course_type):
        if course_type == 'py_ops':
            course = PythonCourse("Python自动化开发",
                                  8, '在线', 6500)
        elif course_type == 'linux':
            course = LinuxOPSCourse("Linux运维课程",
                                    6, '在线', 8000)
        return course

    def enroll(self, name, course):
        print("开始为新学员[%s]办入学手续... " % name)
        print("帮学员[%s]注册课程[%s]..." % (name, course))
        # course.level_test()

    def info(self):
        print("--------[%s]-----" % self.name)


school1 = BJSchool()
school2 = SHSchool()

school1.info()
c1 = school1.create_course("py_ops")
school1.enroll("张三", c1)

school2.info()
c2 = school1.create_course("py_ops")
school2.enroll("李四", c2)
