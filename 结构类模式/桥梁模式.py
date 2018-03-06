# 将抽象和实现解耦，使得两者可以独立地变化。

# 抽象化角色
class Shape:
    name = ""
    param = ""

    def __init__(self, *param):
        pass

    def getName(self):
        return self.name

    def getParam(self):
        return self.name, self.param


# 抽象实现角色
class Pen:
    shape = ""
    type = ""

    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        pass


# 修正化角色1
class Rectangle(Shape):
    def __init__(self, long, width):
        self.name = "Rectangle"
        self.param = "Long:%s Width:%s" % (long, width)
        print("Create a rectangle:%s" % self.param)


# 修正化角色2
class Circle(Shape):
    def __init__(self, radius):
        self.name = "Circle"
        self.param = "Radius:%s" % radius
        print("Create a circle:%s" % self.param)


# 具体实现化角色2
class NormalPen(Pen):
    def __init__(self, shape):
        Pen.__init__(self, shape)
        self.type = "Normal Line"

    def draw(self):
        print("DRAWING %s:%s----PARAMS:%s" % (self.type, self.shape.getName(), self.shape.getParam()))


# 具体实现化角色1
class BrushPen(Pen):
    def __init__(self, shape):
        Pen.__init__(self, shape)
        self.type = "Brush Line"

    def draw(self):
        print("DRAWING %s:%s----PARAMS:%s" % (self.type, self.shape.getName(), self.shape.getParam()))


# 孙类
class Brush1Pen(BrushPen):
    def __init__(self, shape):
        BrushPen.__init__(self, shape)
        self.shape.name += "孙类"
        self.type += "孙类"

    def draw(self):
        print("DRAWING %s:%s----PARAMS:%s" % (self.type, self.shape.getName(), self.shape.getParam()))


if __name__ == "__main__":
    rectangle = Rectangle("20cm", "10cm")
    circle = Circle("15cm")
    normal_pen = NormalPen(rectangle)
    brush_pen = BrushPen(circle)
    normal_pen.draw()
    brush_pen.draw()
    NormalPen(circle).draw()
    Brush1Pen(rectangle).draw()
    Brush1Pen(circle).draw()

    # 要点1：抽象和实现分离，解决继承缺点。实现不在受到抽象的约束
    # 要点2：客户实现不用关心袭击，由抽象层的不同聚合来完成扩展
    # 要点3：该模式使用需要考虑细化逻辑颗粒度，对于一些经常变化的逻辑给予更高的扩展性
    # 要点4：多层继承中，父A函数，子不需要A函数，孙需要A函数的情况桥接比较容易解耦
    # 场景1：继承造成耦合严重的场景
    # 场景2：高重用性场景，设计颗粒度变细带来的好处。
