# 当一个对象内在状态改变时允许其改变行为，这个对象看起来像改变了其类。

class LiftState:
    def open(self):
        print(self._state + ":开门操作失败")
        return self

    def close(self):
        print(self._state + ":关门操作失败")
        return self

    def run(self):
        print(self._state + ":启动操作失败")
        return self

    def stop(self):
        print(self._state + ":停止操作失败")
        return self


class OpenState(LiftState):
    _state = "开门状态"

    def close(self):
        print(self._state + ":开始关门")
        return StopState()


class StopState(LiftState):
    _state = "停止状态"

    def open(self):
        print(self._state + ":开始开门")
        return OpenState()

    def run(self):
        print(self._state + ":开始启动")
        return RunState()


class RunState(LiftState):
    _state = "运行状态"

    def stop(self):
        print(self._state + ":开始停止")
        return StopState()


# 扩展一个维修异常状态
class SuspendedState(LiftState):
    _state = "维修状态"


class Lift:
    _lift_state = None

    def __init__(self):
        self._lift_state = OpenState()

    def setState(self, lift_state):
        self._lift_state = lift_state

    def open(self):
        self._lift_state = self._lift_state.open()

    def close(self):
        self._lift_state = self._lift_state.close()

    def run(self):
        self._lift_state = self._lift_state.run()

    def stop(self):
        self._lift_state = self._lift_state.stop()


if __name__ == "__main__":
    lift = Lift()

    lift.open()
    lift.run()
    lift.stop()
    lift.close()

    lift.open()
    lift.close()
    lift.close()
    lift.stop()
    lift.run()

    lift.open()
    lift.close()
    lift.run()
    lift.stop()
    print("————维修电梯，设置成维修状态————")
    lift.setState(SuspendedState())
    lift.open()
    lift.close()
    lift.run()
    lift.stop()
    lift.setState(OpenState())
    print("————维修完成，设置成开门状态————")
    lift.close()
    lift.run()
    lift.stop()
    # 要点1：状态模式逻辑更加清晰，避免了过多的if
    # 要点2：符合单一职责原则，不同状态的逻辑分离，修改状态只需要修改子类
    # 要点3：封装的很好，状态变化并不需要外部类知道
    # 要点4：解耦后的不可避免的问题，就是状态太多会造成类的膨胀
    # 场景1：行为逻辑需要根据状态做改变的场景
