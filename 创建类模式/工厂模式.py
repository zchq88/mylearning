# 定义一个用于创建对象的接口，让子类决定实例化哪一个类。工厂方法使一个类的实例化延迟到其子类。
# 抽象人类
class Human():
    color = ""
    sex = ""

    def talk(self):
        print(self.color + self.sex + "在说话")

    @classmethod  # 装饰器实现类方法
    def classTalk(self):
        print(self.color + self.sex + "在说话class")


# 白种人类
class WhiteHuman(Human):
    color = "White"


# 黄种人类
class YellowHuman(Human):
    color = "Yellow"


# 抽象工厂
class AbstractHumanFactory:
    def createHuman(self):
        raise Exception("createHuman未定义")


# 普通工厂实类
class HumanFactory(AbstractHumanFactory):
    @staticmethod  # 装饰器实现静态方法
    def createHuman(Human):
        return Human()


# 扩展男人工厂（完全重载函数方法）
class MaleFactory(HumanFactory):
    def createHuman(self, Human):
        __Human = Human()
        __Human.sex = "Male"
        return __Human


# 扩展女人工厂（扩展方法）
class FemaleFactory(HumanFactory):
    def createHuman(self, Human):
        __Human = HumanFactory.createHuman(Human)
        __Human.sex = "Female"
        return __Human


if __name__ == "__main__":
    YinYangLu = HumanFactory()
    whiteHuman = YinYangLu.createHuman(WhiteHuman)
    yellowHuman = YinYangLu.createHuman(YellowHuman)
    whiteHuman.talk()
    whiteHuman.classTalk()
    yellowHuman.talk()
    yellowHuman.classTalk()
    MaleYinYangLu = MaleFactory()
    whiteHuman = MaleYinYangLu.createHuman(WhiteHuman)
    yellowHuman = MaleYinYangLu.createHuman(YellowHuman)
    whiteHuman.talk()
    whiteHuman.classTalk()
    yellowHuman.talk()
    yellowHuman.classTalk()
    FemaleYinYangLu = FemaleFactory()
    whiteHuman = FemaleYinYangLu.createHuman(WhiteHuman)
    yellowHuman = FemaleYinYangLu.createHuman(YellowHuman)
    whiteHuman.talk()
    whiteHuman.classTalk()
    yellowHuman.talk()
    yellowHuman.classTalk()

    # 扩展1：缩小为简单工厂模式，静态工厂，取消抽象工厂类
    # 扩展2：升级为多个工厂，如果初始化逻辑复杂，创建不同工厂如创建男人工厂，女人工厂
    # 扩展3：替代单例模式，工厂返回单例
    # 扩展4：延迟初始化
