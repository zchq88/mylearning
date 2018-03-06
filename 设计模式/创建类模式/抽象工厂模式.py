# 为创建一组相关或相互依赖的对象提供一个接口，而且无需指定它们的具体类。
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
    def createWhiteHuman(self):
        raise Exception("createWhiteHuman未定义")

    def createYellowHuman(self):
        raise Exception("createYellowHuman未定义")


# 男人工厂
class MaleFactory(AbstractHumanFactory):
    countWhite = 0
    countYellow = 0

    def createWhiteHuman(self):
        # 抽象工厂增加逻辑控制产品生产——互相影响的产品线（也叫做产品族）
        if self.countWhite < self.countYellow:
            self.countWhite += 1
            __Human = WhiteHuman()
            __Human.sex = "Male"
            return __Human
        else:
            print("白种人不能创建的黄种人多")
            __Human = Human()
            __Human.sex = "Male"
            return __Human

    def createYellowHuman(self):
        self.countYellow += 1
        __Human = YellowHuman()
        __Human.sex = "Male"
        return __Human


# 女人工厂（扩展产品线）
class FemaleFactory(AbstractHumanFactory):
    countWhite = 0
    countYellow = 0

    def createWhiteHuman(self):
        self.countWhite += 1
        __Human = WhiteHuman()
        __Human.sex = "Female"
        return __Human

    def createYellowHuman(self):
        self.countYellow += 1
        __Human = YellowHuman()
        __Human.sex = "Female"
        return __Human


if __name__ == "__main__":
    MaleYinYangLu = MaleFactory()
    whiteHuman = MaleYinYangLu.createWhiteHuman()
    whiteHuman.talk()
    whiteHuman.classTalk()
    yellowHuman = MaleYinYangLu.createYellowHuman()
    whiteHuman = MaleYinYangLu.createWhiteHuman()
    whiteHuman.talk()
    whiteHuman.classTalk()
    yellowHuman.talk()
    yellowHuman.classTalk()
    FemaleYinYangLu = FemaleFactory()
    whiteHuman = FemaleYinYangLu.createWhiteHuman()
    yellowHuman = FemaleYinYangLu.createYellowHuman()
    whiteHuman.talk()
    whiteHuman.classTalk()
    yellowHuman.talk()
    yellowHuman.classTalk()

    # 要点1：场景不关心产品类，只关心抽象工厂。
    # 要点2：场景不关心产品线（也叫做产品族）的约束，只调用抽象工厂接口。
    # 要点3：产品扩展非常困难，需要增加黑人，就要修改场景，修改抽象工厂。不符合开闭原则
