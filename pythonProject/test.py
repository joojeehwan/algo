def count_x(string):

    if len(string) == 0 :
        return 0

    if string[0] == "x":
        return 1 + count_x(string[1: len(string)])
    else:
        return count_x(string[1: len(string)])

print(count_x("abvxx"))