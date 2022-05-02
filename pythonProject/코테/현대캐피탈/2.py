#풀다 맘

import math

def solution(p, vs):
    result = ""
    new_data = {}
    for words in vs:
        temp = words.split(":")
        if temp[0] in new_data.keys():
            new_data[temp[0]].append(temp[1])
        else:
            new_data[temp[0]] = ([temp[1]])
    result
    for key in new_data.keys():
        new_vs = new_data[key]
        visited = {}
        ans = 0
        while new_vs:
            now = new_vs.pop()
            if now in visited.keys():
                visited[now] += 1
            else:
                visited[now] = 1
            ans += (math.ceil(p / visited[now]))
            new_data[key] = ans
    MAX = 0
    result = ""
    for key, value in new_data.items():
        if value > MAX:
            MAX = value
            result = key

    print(result)

    return result