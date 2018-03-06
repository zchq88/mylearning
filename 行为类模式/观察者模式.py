# 定义对象间一种一对多的依赖关系，使得每当一个对象改变状态，则所有依赖于它的对象都会得到通知并被自动更新。

# 观察者
class Observer:
    def update(self,*args, **kw):
        raise NotImplementedError()


# 被观察者
class Observable:
    def __init__(self):
        self.obs = []

    def addObserver(self, ob):
        self.obs.append(ob)

    def delObserver(self, ob):
        self.obs.remove(ob)

    def notifyAll(self, info):
        for ob in self.obs:
            ob.update(info)


class AlarmSensor(Observer, Observable):
    def update(self, action):
        print("警铃观察到: %s" % action)
        print("警铃响起通知喷水")
        self.notifyAll("需要喷水")


class WaterSprinker(Observer):
    pass
    def update(self, action):
        print("喷水观察到: %s" % action)
        print("喷水启动")
class phoneSensor(Observer):
    pass
    def update(self, action):
        print("警报观察到: %s" % action)
        print("拨打警报电话")

if __name__ == '__main__':
    alarm = AlarmSensor()
    phone = phoneSensor()
    sprinker = WaterSprinker()
    smoke_sensor = Observable()
    smoke_sensor.addObserver(alarm)
    smoke_sensor.addObserver(phone)
    alarm.addObserver(sprinker)
    print("工厂着火了通知警铃")
    smoke_sensor.notifyAll("着火了")
    # 要点1：被观察和观察者之间有接口的耦合，可以尝试单例写消息队列来完成观察者模式解耦
    # 要点2：可以完成触发连，多级消息触发
    # 要点3：广播连不适合太多，不然调试难，链约复杂可维护性就会下降
    # 要点4：性能问题，可以考虑使用多线程异步处理消息
