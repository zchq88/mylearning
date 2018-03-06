# 在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。这样以后就可将该对象恢复到原先保存的状态。


# 发起人类
class Originator(object):

    def __init__(self, state):
        self.state = state

    def create_memento(self):
        return Memento(self.state)

    def set_memento(self, memento):
        self.state = memento.state

    def show(self):
        print("当前状态 ", self.state)


# 备忘录类
class Memento(object):

    def __init__(self, state):
        self.state = state


# 管理者类
class Caretaker(object):
    def __init__(self, memento):
        self.memento = memento


if __name__ == "__main__":
    # 初始状态
    originator = Originator(state='On')
    originator.show()
    # 备忘录
    caretaker = Caretaker(originator.create_memento())
    # 修改状态
    originator.state = 'Off'
    originator.show()
    # 复原状态
    originator.set_memento(caretaker.memento)
    originator.show()
    # 要点1：要主动管理备忘录的生命周期，在任务结束后记得删除备忘录。
    # 要点2：尽量不要频繁建立备忘录，比如一个for循环中建立，可以再循环外建立，不然备忘录的数量难以控制。
    # 要点3：可以尝试使用clone来创建备忘录，不过要考虑深浅拷贝。还有高耦合对象的深拷贝容易出错最好自己管理备份数据。
    # 要点4：有必要可以采用多状态备份和多备份的备忘录，不过会对性能带来影响需要思考架构合理性。
    # 要点5：备份的应用一定要注意封装完整性，避免污染备份而使得备份失去意义。
    # 场景1：需要回滚操作的类，如数据库的事务管理