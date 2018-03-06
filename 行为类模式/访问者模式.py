# 封装一些作用于某种数据结构中的各元素的操作，它可以在不改变数据结构的前提下定义作用于这些元素的新的操作。

# 被访问元素1
class Employee:
    salar = None
    name = None

    def __init__(self, name, salar):
        self.name = name
        self.salar = salar

    def accept(self, visitor):
        visitor.visit(self)


# 被访问元素2
class Manage:
    job = None
    name = None

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def accept(self, visitor):
        visitor.visit(self)


# 访问者1
class Visitor1:
    _name = None
    _sum = 0

    def __init__(self, name):
        self._name = name

    def sum(self):
        print("员工工资总额：%s" % self._sum)

    def visit(self, employee):
        if type(employee) == Employee:
            self._sum += employee.salar
            print("访问者 %s 查看了员工 %s. 的工资:%s " % (self._name, employee.name, employee.salar))
        else:
            print("访问者 %s 查看了管理人 %s. 的工作:%s " % (self._name, employee.name, employee.job))


# 访问者2
class Visitor2:
    _name = ""

    def __init__(self, name):
        self._name = name

    def visit(self, employee):
        if type(employee) == Employee:
            print("2号访问者 %s 查看了员工 %s. 的工资:%s " % (self._name, employee.name, employee.salar))
        else:
            print("2号访问者 %s 查看了管理人 %s. 的工作:%s " % (self._name, employee.name, employee.job))


# 结构对象
class ObjectStruture:
    _employees = []

    def add(self, employee):
        self._employees.append(employee)

    def visit(self, visitor):
        for x in self._employees:
            x.accept(visitor)


if __name__ == '__main__':
    objectStruture = ObjectStruture()
    objectStruture.add(Employee("a", 1000))
    objectStruture.add(Employee("b", 2000))
    objectStruture.add(Employee("c", 3000))
    objectStruture.add(Manage("d", "管理1"))
    objectStruture.add(Manage("e", "管理2"))
    v1 = Visitor1("老板1")
    objectStruture.visit(v1)
    v1.sum()
    objectStruture.visit(Visitor2("老板2"))

    # 要点1：python不支持静态分派，因为python不是支持多态函数所以使用type(employee) == Employee来实现多态的区分。
    # 要点2：访问者吧，数据报表和数据源存储的职责分开了，符合单一职责原则。
    # 要点3：扩展数据报表变得更加容易，增加访问者就可以。
    # 要点4：灵活性高，可以看到访问者对于数据的统计功能也分离出来。
    # 要点5：访问者模式并不符合最少知道原则。
    # 要点6：数据源变更对于整个程序的影响比较大，修改一个数据源就有可能要修改所有的访问者。
    # 要点7：访问者依赖数据源实体，违背了依赖倒置原则。
    # 场景1：一个对象包含很多不同的接口，业务规则要求便利多个不同的对象。访问者模式是对迭代器的一个扩展可以访问统计不同对象数据。
