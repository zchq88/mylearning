# 将一个请求封装成一个对象，从而让你使用不同的请求把客户端参数化，对请求排队或者记录请求日志，可以提供命令的撤销和恢复功能。

# 需求组（执行者1）
class RG:
    def find(self):
        print("找到需求组")

    def delete(self):
        print("删除一个需求")

    def plan(self):
        print("项目计划变更")


# 美工组（执行者1）
class PG:
    def find(self):
        print("找到美工组")

    def delete(self):
        print("删除一个页面")

    def plan(self):
        print("设计计划变更")


# 抽象命令类
class Command:
    _rg = RG()
    _pg = PG()

    def execute(self):
        raise Exception("execute未定义")


# 删除一个页面命令（具体命令1）
class deletePG(Command):
    def execute(self):
        print("客户要求删除一个页面")
        self._pg.find()
        self._pg.delete()
        self._pg.plan()


# 删除一个需求命令（具体命令1）
class deleteRG(Command):
    def execute(self):
        print("客户要求删除一个需求")
        self._rg.find()
        self._pg.find()
        self._pg.delete()
        self._pg.plan()
        self._rg.delete()
        self._rg.plan()


# 负责人
class Invoker:
    command = None

    def setCommand(self, c):
        self.commands = (c)
        return self

    def action(self):
        self.commands.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.setCommand(deletePG()).action()
    invoker.setCommand(deleteRG()).action()

    # 要点1：调用者角色与接收者角色之间没有任何依赖关系，调用者实现功能时只须调用Command抽象类的execute方法就可以，不需要了解到底是哪个接收者执行。
    # 要点2：命令扩展容易
    # 要点3：可以配合其他，如责任链模式实现命令簇解析任务等
    # 要点4：命令子类容易膨胀，可以增加模板模式来解决这个问题
    # 要点5：使用场景：触发-反馈机制的系统，都可以使用命令模式思想。如基于管道结构的命令系统（如SHELL），可以直接套用命令模式；此外，GUI系统中的操作反馈（如点击、键入等），也可以使用命令模式思想。
    # 要点6：线程池中的线程就是命令模式。每一个线程创建就是一个命令，然后线程池处理命令
