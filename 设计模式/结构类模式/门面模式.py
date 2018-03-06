# 要求一个子系统的外部与其内部的通信必须通过一个统一的对象进行。门面模式提供一个高层次的接口，使得子系统更易于使用。

class AlarmSensor:
    def run(self):
        print("Alarm Ring...")


class WaterSprinker:
    def run(self):
        print("Spray Water...")


class EmergencyDialer:
    def run(self):
        print("Dial 119...")


class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor = AlarmSensor()
        self.water_sprinker = WaterSprinker()
        self.emergency_dialer = EmergencyDialer()

    def runAll(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()


if __name__ == "__main__":
    emergency_facade = EmergencyFacade()
    emergency_facade.runAll()
    # 要点1：减少依赖，使依赖只依赖门面于子系统无关。
    # 要点2：提高灵活性，子系统变化不影响门面对象
    # 要点3：提高安全性，门面对象不开放的业务你就不能访问，其实get、set也是门面模式的一种
    # 要点4：门面对象不符合开闭原则。后期修改门面对象逻辑对所有调用者有风险。
    # 要点5：门面模式也可以理解为公共函数，私有函数就是子系统。
    # 要点6：门面模式尽量不包含子系统内业务逻辑，不然违反了单一职责原则。
    # 场景1：很多类库其实就是门面模式做最后一层封装的。
    # 场景2：分工明确，门面逻辑更加抽象。

