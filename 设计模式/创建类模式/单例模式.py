# 确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例。
import threading
import time


# 这里使用方法__new__来实现单例模式
class Singleton(object):  # 抽象单例
    lock = threading.RLock()

    def __new__(cls, *args, **kw):
        cls.lock.acquire()
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
            time.sleep(0.5)
        cls.lock.release()
        return cls._instance


# 装饰模式给函数增加线程锁
def lockFun(func):
    lock = threading.RLock()

    def wrapper(*args, **kw):
        lock.acquire()
        ret = func(*args, **kw)
        # print(id(lock)) #查看线程锁是否重合
        lock.release()
        return ret

    return wrapper


# 皇帝类
class Emperor(Singleton):
    __name = None

    def setName(self, name):
        self.__name = str(name)

    # @lockFun
    def doSomething(self, Minister):
        time.sleep(1)
        print(Minister.name + "朝拜" + self.__name)

    @lockFun
    def say(self, Minister):
        time.sleep(0.5)
        print(Minister.name + "上奏" + self.__name)


# 臣子类
class Minister(threading.Thread):
    name = None

    def run(self):
        print(self.name)
        self.my_emperor = Emperor(self.name)
        self.my_emperor.doSomething(self)
        self.my_emperor.say(self)


if __name__ == "__main__":
    Emperor().setName("秦始皇")
    for i in range(100):
        my_entity = Minister()
        my_entity.name = "臣子" + str(i)
        my_entity.start()
