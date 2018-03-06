# 给定一门语言，定义它的文法的一种表示，并定义一个解释器，该解释器使用该表示来解释语言中的句子。

# 环境角色
# 上下文类：演奏内容
class PlayContext():
    PlayText = None


# 抽象表达式类
class Expression():
    def Interpret(self, context):
        if len(context.PlayText) == 0:
            return
        else:
            playKey = context.PlayText[0:1]
            context.PlayText = context.PlayText[1:]
            tmp = context.PlayText.index(' ')  # 找出第一个空格出现的位置
            playValue = context.PlayText[0:tmp]
            context.PlayText = context.PlayText[tmp + 1:]
            self.Excute(playKey, playValue)

    def Excute(self, playKey, playValue):
        pass


# 空格(终结符表达式)
class Pitch(Expression):
    pitch = None

    def Excute(self, key, value):
        value = int(value)
        if value == 1:
            self.pitch = '低音'
        elif value == 2:
            self.pitch = '中音'
        elif value == 3:
            self.pitch = '高音'
        print("")
        print(self.pitch, end='')


# 音符(非终结符表达式)
class Note(Expression):
    Notes = {
        'C': 1,
        'D': 2,
        'E': 3,
        'F': 4,
        'G': 5,
        'A': 6,
        'B': 7,
    }
    note = None

    def Excute(self, key, value):
        self.note = self.Notes[key]
        print('key:%d time:%s' % (self.note, value), end=' ')


def clientUI():
    context = PlayContext()
    context.PlayText = "O2 E0.6 G0.5 A3 E0.5 G0.5 D3 E0.5 G0.5 A0.5 O3 C1 O1 A0.5 G1 C0.5 E0.5 D3 "
    expression = None;
    while (len(context.PlayText) > 0):
        str = context.PlayText[0:1];
        if (str == 'O'):
            expression = Pitch()
        elif (str == 'C' or str == 'D' or str == 'E' or str == 'F' or
              str == 'G' or str == 'A' or str == 'B' or str == 'P'):
            expression = Note()
        expression.Interpret(context)
    return


# 全局命名空间为空，使用局部命名空间
def make_fn(code):
    return eval('lambda x: %s' % code)


# 使用全局命名空间
def make_fng(code):
    import math
    ALLOWED = {v: getattr(math, v)
               for v in filter(lambda x: not x.startswith('_'), dir(math))
               }

    ALLOWED['__builtins__'] = None
    return eval('lambda x: %s' % code, ALLOWED, {})


if __name__ == '__main__':
    clientUI()
    print(eval('1 + 1'))
    f = make_fn('x + 1')
    print(f(8))
    f = make_fng('cos(x*x)')
    print(f(3))
    try:
        g = "3"
        eval("print(g)")
        eval("print(g)", {"g": 2}, {})
        eval("print(g)", {"g": 2}, {"g": 1})
        eval("__import__('os').system('dir')", {"__import__": None}, {})
    except BaseException as e:
        print(e.args)
    # 要点1：解释器语言的定义和解析逻辑很复杂容易出现BUG
    # 要点2：方便客户可以扩展逻辑
    # 要点3：效率问题，多一层解析带来效率问题
    # 场景1：逻辑不由程序控制，而有用户控制部分可以使用解释器模式
    # 场景2：逻辑经常变更而不想重新开发程序部分可以使用解释器模式
    # 场景3：一个简单语法需要解释的场景
    # python中可以用eval来模拟解释器，不过也会带来安全性的问题。如"__import__('os').system('dir')"，需要控制全局变量来提升安全性

