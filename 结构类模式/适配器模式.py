# 将一个类的接口变换成客户端所期待的另一种接口，从而使原本因接口不匹配而无法在一起工作的两个类能够在一起工作。

class A:
    _name = ""

    def __init__(self, name):
        self._name = name

    def getName(self):
        print(self._name)


class B:
    _name = ""

    def __init__(self, name):
        self._name = name

    def get_name(self):
        print(self._name)


class C:
    _b = ""

    def __init__(self, b):
        self._b = b

    def getName(self):
        self._b.get_name()


if __name__ == "__main__":
    a = A("A")
    b = B("B")
    c = C(b)
    a.getName()
    c.getName()
    # 要点1：方便不同设计的统一，让两个类在同一个系统中运行
    # 要点2：提高了类的复用性，原角色可以再原有系统中继续运行，并适应新的系统
    # 要点3：最好再详细设计阶段不要考虑，一定要遵循依赖倒置和里式替换才能更好的满足适配器的模式
    # 场景1：系统扩展，增加新的属性而不破坏原来的运行环境。