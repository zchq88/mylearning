# 动态地给一个对象添加一些额外的职责。就增加功能来说，装饰模式相比生成子类更为灵活
import datetime
import time


def log(func):
    def wrapper(*args, **kw):
        # print('call %s():' % func.__name__)
        t0 = datetime.datetime.now()
        result = func(*args, **kw)
        t1 = datetime.datetime.now()
        print("Total time running %s: %s seconds" % (func.__name__, str(t1 - t0)))
        return result

    return wrapper


@log
def now():
    time.sleep(0.1)
    print('2016-12-04')


@log
def add(a, b):
    time.sleep(0.5)
    print(a + b)


if __name__ == "__main__":
    now()
    add(1, 2)
    # 要点1：装饰着和被装饰着相互独立并不耦合
    # 要点2：装饰模式是继承的一种替代方案
    # 要点3：可以动态扩展类的功能
    # 要点4：多层装饰会带来调试困难
    # 要点5：满足开闭原则非常适合修改功能使用的设计模式
