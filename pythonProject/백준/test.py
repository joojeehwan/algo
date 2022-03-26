


print("1" < "2")


def dfs(idx, sel):
    if idx > len(lst):
        return
    if sel == m:
        print()
    return


    check[idx] = True
    dfs(idx + 1, sel + 1)
    check[idx] = False


m = 2
lst = [1, 2, 3]
dfs(0, 0)