# 将对象组合成树形结构以表示“部分-整体”的层次结构，使得用户对单个对象和组合对象的使用具有一致性。
import uuid


# 透明组合模式
class Component:
    _list = None
    _obj = None
    _id = None
    _parent = None

    def __init__(self, obj):
        self._list = {}
        self._obj = obj
        self._id = str(uuid.uuid1())

    def add(self, component):
        if not type(component) == Component:
            raise Exception("添加类型不是树类型")
        else:
            component.setParent(self)
            self._list[component.getID()] = component

    def remove(self, id):
        ret = False
        if not self._list.get(id) == None:
            print(id + "子节点删除")
            del self._list[id]
            ret = True
        else:
            for i, value in root.getAllChildren():
                if id == i:
                    value.getParent().remove(id)
                    ret = True
        if ret == False:
            print("没有找到节点" + id)
        return ret

    def getChildren(self):
        return self._list.items()

    def getAllChildren(self):
        alllist = {}
        for id, value in self.getChildren():
            alllist[id] = value
            for Childrenid, Childrenvalue in value.getAllChildren():
                alllist[Childrenid] = Childrenvalue
        return alllist.items()

    def getObj(self):
        return self._obj

    def getID(self):
        return self._id

    def setParent(self, parent):
        self._parent = parent

    def getParent(self):
        return self._parent


if __name__ == '__main__':
    root = Component("root")
    a = Component("a")
    # a = Component(Component("root"))
    b = Component("b")
    root.add(a)
    root.add(b)
    a.add(Component("a1"))
    a.add(Component("a1"))
    a.add(Component("a2"))
    a.add(Component("a3"))
    a.add(Component("a4"))
    b1 = Component("b1")
    b.add(b1)
    b1a = Component("b1a")
    b1.add(b1a)
    # print(root.getChildren())
    # print(a.getChildren())
    # print(b.getChildren())
    # print(b1.getChildren())
    # print(root.getID())
    # print(a.getParent().getID())
    print("____________________")
    for i, value in root.getAllChildren():
        print(str(value.getObj()))
    root.remove(b1a.getID())
    print("____________________")
    for i, value in root.getAllChildren():
        print(str(value.getObj()))
    root.remove(a.getID())
    print("____________________")
    for i, value in root.getAllChildren():
        print(str(value.getObj()))
    root.remove(root.getID())
    print("____________________")
    for i, value in root.getAllChildren():
        print(str(value.getObj()))

    # 要点1：高层代码对于节点的调用简单并不用知道。
    # 要点2：扩展节点比较容易。
    # 要点3：以上是透明组合模式，安全组合模式(区分叶子节点和树枝节点，不过在python的便利方法并不会因为空数据而异常所以不这么写了)
    # 要点4：真实组合模式，由于关系型数据库，所以真实的组合模式如何存储关系型数据，表结构如何也是值得扩展的问题。
    # 要点5：如何顺序的读取树也可以继续扩展。