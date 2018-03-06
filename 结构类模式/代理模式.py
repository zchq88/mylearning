# 为其他对象提供一种代理以控制对这个对象的访问。
class GamePlayer:
    name = ""
    level = 0
    _Prox = None  # 强制代理

    def __init__(self, _name):
        self.name = _name

    def login(self, user):
        print("登录名为" + user + "登录" + self.name)

    def killBoss(self):
        print(self.name + "打怪")

    def upgrade(self):
        if (self.isProx()):  # 强制代理
            self.level += 1
            print(self.name + "升级" + str(self.level))
        else:
            print(self.name + "请使用代理升级")

    def isProx(self):
        return not self._Prox == None


# 普通代理
class GamePlayerProxy(GamePlayer):
    _gamePlayer = None

    def __init__(self, Object):
        self._gamePlayer = Object

    def login(self, user):
        self._gamePlayer.login(user)

    def killBoss(self):
        print("代练代理:", end='')
        self._gamePlayer.killBoss()

    def upgrade(self):
        self._gamePlayer._Prox = self  # 强制代理
        self._gamePlayer.upgrade()
        self._gamePlayer._Prox = None  # 强制代理


# 动态代理
class DynamicProxy:
    _obj = None

    def __init__(self, Object):
        self._obj = Object
        for fun in dir(Object):
            if "__" not in fun:
                _attr = getattr(Object, fun)
                if fun == "killBoss":
                    def function():
                        print("代练动态代理:", end='')
                        getattr(self._obj, "killBoss")()

                    _newattr = function
                elif fun == "upgrade":
                    def function():
                        self._obj._Prox = self  # 强制代理
                        getattr(self._obj, "upgrade")()
                        self._obj._Prox = None  # 强制代理

                    _newattr = function
                else:
                    _newattr = _attr
                setattr(self, fun, _newattr)


if __name__ == "__main__":
    def run(object, _name):
        object.login(_name)
        object.killBoss()
        object.upgrade()
        print("------------------" + str(id(object)))


    player = GamePlayer("玩家1")
    run(player, "A")
    playerproxy = GamePlayerProxy(player)
    run(playerproxy, "B")
    dynamicproxy = DynamicProxy(player)
    run(dynamicproxy, "C")
    run(player, "A")
    # 要点1：虚拟代理，在真实使用时实例化
    # 要点2：业务逻辑，不需要关心非本职的工作，通过代理解决预处理和后期处理
    # 要点3：代理后期扩展性高
    # 要点4：智能化，可使用动态代理，代理不同类型的相同业务逻辑完成审计类需求
    # 要点5：强制代理，某些业务逻辑使用强制代理，约束调用代理
    # 要点6：主要解决面向切面编程
