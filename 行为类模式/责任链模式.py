# 使多个对象都有机会处理请求，从而避免了请求的发送者和接受者之间的耦合关系。
# 将这些对象连成一条链，并沿着这条链传递该请求，直到有对象处理它为止。

class request:
    _info = {}

    def setRequest(self, info):
        self._info = info

    def getRequest(self):
        return self._info


class manager:
    _next = None
    _name = None
    _num = None

    def __init__(self, name, num):
        self._name = name
        self._num = num

    def setNext(self, next):
        self._next = next

    def __canhandle(self, request):
        request = request.getRequest()
        if request["number"] > self._num:
            print(self._name + "不可以处理" + request["Type"] + str(request["number"]) + "天" + "并移交下一级")
            return False
        else:
            return True

    def handle(self, request):
        if self.__canhandle(request):
            if self.echo(request):
                return
        elif not self._next == None:
            self._next.handle(request)
        else:
            print("不能请假，处理结束")


    def echo(self, request):
        request = request.getRequest()
        print(self._name + "可以处理" + request["Type"] + str(request["number"]) + "天" + "并批准")
        return True


if __name__ == "__main__":
    a = manager("部门经理", 3)
    b = manager("副经理", 7)
    c = manager("总经理", 10)
    a.setNext(b)
    b.setNext(c)
    # c.setNext(a)
    req = request()
    req.setRequest({"Type": "A请假", "number": 2})
    a.handle(req)
    print("______________________")
    req.setRequest({"Type": "B请假", "number": 5})
    a.handle(req)
    print("______________________")
    req.setRequest({"Type": "C请假", "number": 8})
    a.handle(req)
    print("______________________")
    req.setRequest({"Type": "D请假", "number": 11})
    a.handle(req)
    print("______________________")
    # 要点1：请求和处理分开，请求不需要知道谁处理的，处理可以不用知道请求的全貌。
    # 要点2：性能问题，请求链式调用性能会成问题，请求链长调试不方便。
    # 要点3：可以限制setNext来解决无意识的破坏系统性能问题