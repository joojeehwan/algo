''''

<핵심 아이디어>
여행계획에 해당하는 모든 노드가 같은 집합에 속하기만 하면 가능한 여행경로이다.

-> 두 노드 사이에 도로가 존재하면 union 연산을 해서 두 노드를 같은 집합에 속하도록 만든다.


'''


#특정 원소가 속한 집합을 찾기

def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 떄까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    #일반적으로 번호가 더 작은 것을 부모로
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


#여행지의 개수와 여행 계획에 속한 여행지의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1)

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i


#union연산을 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: #연결된 경우!
            union_parent(parent, i+1, j+1)


#여행 계획입력받긴
plan = list(map(int, input().split()))

res = True

#여행 계획에 속하는 모든 노드의 루트가 동일한지 확인

for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        res = False

#여행 계획에 속하는 모든 노드가 서로 연결되어 있는지 확인
if res:
    print("YES")

else:
    print("NO")