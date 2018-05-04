def qsort(L):
    if len(L) <= 1:
        return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1] + qsort([ge for ge in L[1:] if ge >= L[0]])


if __name__ == "__main__":
    iList = [3, 14, 2, 12, 9, 33, 99, 35]
    print(qsort(iList))
