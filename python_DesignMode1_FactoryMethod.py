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

class ChinaGetter:
    '''A simple localizer a la gettext,一个初始对象（定位器）'''
    def __init__(self):
        self.trans = dict(dog=u"小狗", cat=u"小猫")

    def get(self, msgid):
        '''We'll punt if we don't have a translation'''
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)

class EnglishGetter:
    """Simply echoes the msg ids"""
    def get(self,msgid):
        return str(msgid)


def get_localizer(language = "English"):
    '''工厂模式'''
    languages = dict(English = EnglishGetter, China = ChinaGetter)
    return languages[language]()


# 创建我们的localizer
e, g = get_localizer("English"), get_localizer("China")

for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))



































