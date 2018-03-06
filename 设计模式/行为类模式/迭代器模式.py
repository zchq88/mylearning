# 它提供一种方法访问一个容器对象中各个元素，而又不需暴露该对象的内部细节。

def MyGenerater(n):
    index = 0
    while index < n:
        yield str(index ** 2)
        index += 1


if __name__ == "__main__":
    lst = ["hello Alice", "hello Bob", "hello Eve"]
    lst_iter = iter(lst)
    print(lst_iter)
    print(lst_iter.__next__())
    print(lst_iter.__next__())
    print(lst_iter.__next__())
    # print(lst_iter.__next__())
    x_square = MyGenerater(5)
    for x in x_square:
        print("0-" + x)
    for x in x_square:  # 不会输出
        print("1-" + x)
    for x in MyGenerater(5):
        print("2-" + x)
    # 要点1：迭代器无法重复迭代
    # 要点2：迭代器模式已被很多语言原生实现，多数情况并不需要再自己实现了
