# 用一个中介对象封装一系列的对象交互，中介者使各对象不需要显示地相互作用，从而使其耦合松散，而且可以独立地改变它们之间的交互。

class colleague():
    _mediator = None


# 采购人员（同事1）
class Purchase(colleague):
    def __init__(self, _mediator):
        self._mediator = _mediator
        self._mediator._purchase = self

    def buy(self, num):
        print("---采购人员采购设备---")
        print("购买" + str(num) + "设备")
        self._mediator.execute("buy", num)


# 销售人员（同事2）
class Sale:
    def __init__(self, _mediator):
        self._mediator = _mediator
        self._mediator._sale = self

    def sell(self, num):
        print("---销售人员销售设备---")
        print("销售" + str(num) + "设备")
        self._mediator.execute("sell", num)

    def offsell(self, num):
        print("---销售人员折价销售设备---")
        print("折价销售" + str(num) + "设备")
        self._mediator.execute("offsell", num)


# 仓管人员（同事3）
class Stock:
    _num = 50
    _max = 100
    _min = 20

    def __init__(self, _mediator):
        self._mediator = _mediator
        self._mediator._stock = self

    def add(self, _num):
        self._num += _num
        self.has_num()

    def sub(self, _num):
        self._num -= _num
        self.has_num()

    def has_num(self):
        print("仓库含有" + str(self._num) + "设备")

    def get_num(self):
        return self._num

    def get_max(self):
        return self._max

    def get_min(self):
        return self._min


# 中介者依赖同事们
class Mediator:
    _purchase = None
    _sale = None
    _stock = None

    def execute(self, name, *args):
        if self._purchase == None:
            print("没有初始化_purchase")
            return
        if self._sale == None:
            print("没有初始化_sale")
            return
        if self._stock == None:
            print("没有初始化_stock")
            return
        if hasattr(self, name):
            # print("中介处理了" + name)
            getattr(self, name)(*args)
        else:
            print("中介未处理" + name)

    def buy(self, num):
        _num = self._stock.get_max() - self._stock.get_num()
        if _num > num:
            print("库存情况良好全数采购")
            self._stock.add(num)
        else:
            print("库存情况不好补仓后多余的清仓销售")
            self._stock.add(num)
            self._sale.offsell(num - _num)

    def sell(self, num):
        _num = self._stock.get_num() - num
        self._stock.sub(num)
        if _num < 0:
            print("销售库存不够，采购" + str(-_num + self._stock.get_min()))
            self._purchase.buy(-_num + self._stock.get_min())

    def offsell(self, num):
        _num = self._stock.get_num() - num
        self._stock.sub(num)
        if _num < 0:
            print("折价销售库存不够，采购" + str(-_num))
            self._purchase.buy(-_num)


if __name__ == "__main__":
    mediator = Mediator()
    purchase = Purchase(mediator)
    sale = Sale(mediator)
    stock = Stock(mediator)
    purchase.buy(5)
    print("—————————————————————————")
    purchase.buy(50)
    print("—————————————————————————")
    sale.sell(50)
    print("—————————————————————————")
    sale.offsell(55)
    # print("————————————可以增加访问权限来保护流程——————————————————")
    # stock.add(15)
    # mediator._sale.sell(25)
    # 要点1：同事类之间的一对多的依赖转换为对中介的一对一的依赖
    # 要点2：中介者负责调度逻辑，同事种类越多调度逻辑约复杂
    # 要点3：中介场景：资源调度，现实中如中介服务的房产中介。
    # 要点4：多个对象有依赖关系，但是依赖之间的逻辑不确定或变化比较大适合中介者模式
