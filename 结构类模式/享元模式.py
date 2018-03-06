# 使用共享对象可有效地支持大量的细粒度的对象。

# 外部状态
class Coffee:
    name = ''
    price = 0

    def __init__(self, name):
        self.name = name
        self.price = len(name)

    def show(self):
        print("Coffee Name:%s Price:%s" % (self.name, self.price))


# 内部状态
class Order:
    coffee_factory = ""
    name = ""

    def __init__(self, name, coffee):
        self.name = name
        self.coffee = coffee
        print("%s ordered a cup of coffee:%s" % (self.name, self.coffee))


# 享元工厂
class Factory:
    coffee_dict = {}

    def getOrder(self, customer_name, coffee_name):
        if not coffee_name in self.coffee_dict:
            self.coffee_dict[coffee_name] = Coffee(coffee_name)
        return Order(customer_name, self.coffee_dict[coffee_name])

    def getCoffeeCount(self):
        return print(len(self.coffee_dict))


if __name__ == "__main__":
    coffee_factory = Factory()
    order1 = coffee_factory.getOrder("A", "cappuccino")
    order2 = coffee_factory.getOrder("B", "mocha")
    order3 = coffee_factory.getOrder("C", "cappuccino")
    order1.coffee.show()
    order2.coffee.show()
    order3.coffee.show()
    coffee_factory.getCoffeeCount()
    # 要点1：较少内存，共享相同数据
    # 要点2：内部和外部状态分离设计是一个难点
    # 要点3：线程安全问题，外部状态的检查需要考虑线程问题带来的享元BUG
    # 要点4：复杂的外部状态的相等判断会带来一定的性能损失。所以外部状态的判断逻辑也是制约享元模式应用的一个点
    # 场景1：系统中存在，大量相似对象，细粒度对象可以分理处相同的外部对象
    # 场景2：需要缓冲池的场景
