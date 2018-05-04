def search(l):
    for item in l:
        if type(item) is list:
            search(item)
        else:
            print(item)


if __name__ == "__main__":
    l = [1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15, [16, [17, ]], 19]]]]]]]
    search(l)
