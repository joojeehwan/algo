'''

플로이드 워셜 문제

Dab = min(Dab, Dak + Dkb)

 'A에서 B로 가는 최소 비용'과 'A에서 K를 거쳐 B로 가는 비용'을 비교하여 더 작은 값으로 갱신하겠다는 것입니다.
 즉 '바로 이동하는 거리'가 '특정한 노드를 거쳐서 이동하는 거리'보다 더 많은 비용을 가진다면 이를 더 짧은 것으로 갱신한다는 것입니다.
'''


INF = int(1e9) #무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기

n = int(input())
m = int(input())

# 2차원 리스트를 만들고 , 모든값을 무한으로 초기화


#N + 1로 만드는 이유! 0번 노드는 없다! 1번 노드 부터 시작이라!
MAP = [[INF] * (n + 1) for _ in range(n + 1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if row == col:
            MAP[row][col] = 0
            

#단 반향 연결
#각 각선에 대한 정보를 입력받아, 그 값으로 초기화

'''
도시와 도시를 잇는 간선이 여러개 일 수 있구나! 

여러개,,! 
'''

for _ in range(m):
    # a도시 에서 b도시로 간다!
    frm, to, cost = map(int, input().split())
    #가장 최단의 도시만 연결
    if cost < MAP[frm][to]: #3 -> 4로 가는 것중에 가장 작은게 들어가겠네! 왜냐면 MAP의 값을 통해서 확인하니깐!
        MAP[frm][to] = cost


#점화식에 따라 플로이드 워셜 알고리즘 수행!

for k in range(1 ,n + 1):
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            MAP[row][col] = min(MAP[row][col], MAP[row][k] + MAP[k][col])


#수행된 결과를 출력!
#이차원 배열 그냥 출력하면 된다.
for row in range(1, n + 1):
    for col in range(1, n + 1):
        if MAP[row][col] == INF:
            print("0", end= " ")
        else:
            print(MAP[row][col], end =" ")

    print()
