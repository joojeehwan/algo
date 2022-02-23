# 1 2개의 방법으로 풀이

# 1 원래 풀던 크루스칼 알고리즘 풀이 방법

# 2

# def solution(n, costs):

#     def find_parent(parent, x):

#         if parent[x] != x:
#             parent[x] = find_parent(parent, parent[x])
#         return parent[x]

#     def union_parent(parent, a, b):

#         a = find_parent(parent, a)
#         b = find_parent(parent, b)
#         if a > b:
#             parent[a] = b
#         else:
#             parent[b] = a

#     answer = 0
#     costs.sort(key=lambda x:x[2]) #비용 기준으로 오름차순 정렬
#     parent = [i for i in range(n)] #parent 배열 부모를 자기자신으로 초기화

#     for a, b, cost in costs:
#         if find_parent(parent, a) != find_parent(parent, b): #사이클이 발생하지 않는 경우에만 집합에 포함시킴.
#             union_parent(parent, a, b)
#             answer += cost #여기에 비용 넣어주기

#     return answer


def solution(n, costs):
    costs = sorted(costs, key=lambda x: x[2])
    node = set([costs[0][0], costs[0][1]])
    answer = costs[0][2]
    while len(node) != n:
        for i in range(1, len(costs)):
            if costs[i][0] in node and costs[i][1] in node:  # 사이클이 발생한다면
                continue

            if costs[i][0] in node or costs[i][1] in node:  # 사이클이 발생하지 않고, 최소의 값이면
                node.update([costs[i][0], costs[i][1]])
                answer += costs[i][2]
                break

    return answer