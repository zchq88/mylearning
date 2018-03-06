# 将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。（注重构建过程的解耦分离）
# 抽象产品
class Car:
    # 顺序队列
    sequence = []

    def run(self):
        for todo in self.sequence:
            if hasattr(self, todo):
                _attr = getattr(self, todo)
                _attr()
        print("------------------")


# 产品1
class BMW(Car):
    def start(self):
        print("BMW" + "发动")

    def stop(self):
        print("BMW" + "停止")

    def alarm(self):
        print("BMW" + "鸣笛")

    def engineBoom(self):
        print("BMW" + "引擎")


# 产品2
class Benz(Car):
    isAlarm = False

    def start(self):
        print("Benz" + "发动")

    def stop(self):
        print("Benz" + "停止")

    def alarm(self):
        if self.isAlarm:
            print("Benz" + "鸣笛")

    def engineBoom(self):
        print("Benz" + "引擎")


# 抽象建造者
class CarBulider(Car):
    def set_sequence(self, _set_sequence):
        self.sequence = _set_sequence

    def BuliderCar(self):
        pass


# 具体建造者1
class BMWBulider(CarBulider):
    def BuliderCar(self):
        Product = BMW()
        Product.sequence = self.sequence
        return Product


# 具体建造者2
class BenzBulider(CarBulider):
    def BuliderCar(self):
        Product = Benz()
        Product.sequence = self.sequence
        return Product


# 导演类
class Director:
    _BMWBulider = BMWBulider()
    _BenzBulider = BenzBulider()
    _sequence1 = ["start", "alarm", "engineBoom", "stop"]
    _sequence2 = ["start", "stop"]

    def getBMW1(self):
        self._BMWBulider.set_sequence(self._sequence1)
        return self._BMWBulider.BuliderCar()

    def getBMW2(self):
        self._BMWBulider.set_sequence(self._sequence2)
        return self._BMWBulider.BuliderCar()

    def getBenz1(self):
        self._BenzBulider.set_sequence(self._sequence1)
        return self._BenzBulider.BuliderCar()

    def getBenz2(self):
        self._BenzBulider.set_sequence(self._sequence2)
        return self._BenzBulider.BuliderCar()


if __name__ == "__main__":
    director = Director()
    BMW1 = director.getBMW1()
    BMW1.run()
    BMW2 = director.getBMW2()
    BMW2.run()
    Benz1 = director.getBenz1()
    # Benz.isAlarm = True
    Benz1.run()
    Benz2 = director.getBenz2()
    Benz2.run()

    # 要点1：建造者模式使场景类不关心组成过程。
    # 要点2：扩展建造过程不对模块产生影响（建造过程封装解耦）
    # 要点3：适用于相同方法不同执行顺序效能不同的场景。
    # 要点4：多品类合成方法不同效能不同的场景
