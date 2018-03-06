# 定义一个操作中的算法的框架，而将一些步骤延迟到子类中。使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。
class Car:
    # 扩展行为增加分支，默认值
    isAlarm = True

    def run(self):
        self.start()
        self.engineBoom()
        if self.isAlarm:
            self.alarm()
        self.stop()
        print("------------------")


class BMW(Car):
    def start(self):
        print("BMW" + "发动")

    def stop(self):
        print("BMW" + "停止")

    def alarm(self):
        print("BMW" + "鸣笛")

    def engineBoom(self):
        print("BMW" + "引擎")


# 扩展Benz默认不鸣笛
class Benz(Car):
    isAlarm = False

    def start(self):
        print("Benz" + "发动")

    def stop(self):
        print("Benz" + "停止")

    def alarm(self):
        print("Benz" + "鸣笛")

    def engineBoom(self):
        print("Benz" + "引擎")


if __name__ == "__main__":
    BMW1 = BMW()
    BMW1.run()
    Benz1 = Benz()
    Benz1.run()
    Benz2 = Benz()
    Benz2.isAlarm = True
    Benz2.run()
    # 要点1：提取公共部分代码到父类。
    # 要点2：父类控制行为，子类实现功能。
