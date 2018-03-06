# 用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
from copy import copy, deepcopy


class Human:
    name = ""
    # __task = ["起床", "上班", "回家"]
    # _task = ["起床", "上班", "回家"]
    task = ["起床", "上班", "回家"]
    print(id(task))

    def setTask(self, _task):
        # self.__task[0] = _task
        # self._task[0] = _task
        self.task[0] = _task

    def Do(self):
        print(id(self.task))
        print(self.name + str(self.task))

    @classmethod  # 装饰器实现类方法
    def classDo(self):
        print(self.name
              + str(self.__task)
              + str(self._task)
              + str(self.task))

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    people1 = Human()
    people1.name = "黄种人"
    # people1.task[0] = "起床1"  # 这样写task继承父类task
    people1.task = ["起床1", "上班", "回家"]  # 这样写task开辟新内存影响深度拷贝结果
    people2 = people1.clone()
    people3 = people1.deep_clone()
    people2.task[0] = "起床2"
    # people2.task = ["起床2", "上班", "回家"]  # 这样写task开辟新不修改people1的task
    people3.task[0] = "起床3"
    people1.Do()
    people2.Do()
    people3.Do()

    # 要点1：内存复制比NEW效率高
    # 要点2：不执行__init__函数
    # 要点3：注意深浅拷贝问题
    # 要点4：deep_clone拷贝子类数组内存
    # 场景1：类初始化需要消化非常多的资源，这个资源包括数据、硬件资源等。
    # 场景2：实际使用可配合工厂模式
