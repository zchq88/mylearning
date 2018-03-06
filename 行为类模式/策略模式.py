# 定义一组算法，将每个算法都封装起来，并且使它们之间可以互换。


# 抽象策略类
class Strategy:
    def exec(self):
        pass


# 具体封装类
class Context:
    def addStrategy(self, fun):
        if hasattr(self, fun.__name__):
            raise Exception("已经拥有该名称策略，不能添加相同名称策略")
        else:
            strategy = Strategy()
            setattr(strategy, "exec", fun)
            setattr(self, fun.__name__, strategy)


def add(obj):
    return obj.a + obj.b


def sub(obj):
    return obj.a - obj.b


class Obj:
    a = 1
    b = 2


if __name__ == "__main__":
    cal = Context()
    cal.addStrategy(add)
    cal.addStrategy(sub)
    obj = Obj()
    # cal.addStrategy(add)
    print(cal.add.exec(obj))
    print(cal.sub.exec(obj))

    # 要点1：策略暴露，并不符合最少知道原则
    # 要点2：策略选择逻辑外移，由调用者写if else来选择何种策略
    # 要点3：符合开闭原则，实现策略逻辑对象化，策略逻辑的扩展性良好
    # 要点4：策略逻辑超过一定数量需要考虑使用混合模式减少策略膨胀问题
    # 场景1：算法的选择由使用者决定，算法规则生命周期难以衡量的项目
