'''

달이 차오른다 가자


1. '0' 부터 BFS 탐색

- 새롭게 이동할 곳이 '1' 이거나 '.' 이면 그냥 방문

- 새롭게 이동할 곳이 'a' ~ 'f' 사이 key가 존재하는 경우, 현재 key에서 or 연산을 통해 key 흭득하기

- 새롭게 이동할 곳이 'A' ~ 'F" 사이 door가 존재하는 경우, 현재 key에서 and 연산을 통해 문을 통과할 수 있는지 확인하기


또한, 이미 탐색한 정점인지를 판단하기 위해서 사용된 Visit배열은 3차원 배열로 선언해주었다.

   왜냐하면, 이미 지나왔던 길이라도, 내가 특정 열쇠를 주운 후에 다시한번 지난가는 길은 다른 의미를 가지고 있기 때문이다.

   Visit[][][64] ! 갑자기 또 64가 왜나왔을까??

   키가 6개이므로 비트로 표현하면 111111이 되고, 모든 열쇠를 다 가지고 있을 경우 2^6 = 64가 되기 때문에 크기를 64로

   잡아주었다 !



'''



'''

print(1 << ord("B") - ord("A"))
print(1 << ord("C") - ord("A"))
답이 2 , 4 나오는데

ob oo1o 이라고 볼 수 있음 B니깐 2번째에 표시가 되어야 한다!  
ob 0100 이라고 볼 수 있음 C니깐 3번째에 표시가 되어야 한다. 

알파벳을 인덱스화 해서! 유무를 파악하는 것 그것이 바로 비트 마스크 
'''

import sys
from collections import deque



dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def haveKey(cur_key, door):
    #" 알파벳 A를 Index화 시켜서 그 Index번호만큼 1을 왼쪽으로 Shift시킨 후, 우리가 가진 키와 AND연산 !
    value = cur_key & (1 << (ord(door)- ord("A")))
    return True if value else False



def bfs(row, col):

    #row, col, 이동횟수, 내가 현재 가진 키
    q = deque([(row, col, 0, 0)])
    #3차원 배열로 표현 => 키를 가지고돌아오는 것은 또 다른 길이라 판단
    #이미 지나왔던 길이라도, 내가 특정 열쇠를 주운 후에 다시한번 지난가는 길은 다른 의미를 가지고 있기 때문이다.
    check = [[[False] * (1 << 6) for _ in range(50)] for _ in range(50)]
    #처음 위치는 키없이 들린 곳
    check[row][col][0] = True


    while q:
        row, col, cnt, key = q.popleft()
        #그 때 까지의 이동 경로를 반환! 탈출하는 곳에 왔으니 
        if MAP[row][col] == "1":
            return cnt

        for k in range(4):
            next_row = row + dr[k]
            next_col = col + dc[k]

            if 0 <= next_row < N and 0 <= next_col < M: #범위 안에 있음.
                if not check[next_row][next_col][key]: #방분하지 않은 곳
                    if MAP[next_row][next_col] == "1" or MAP[next_row][next_col] == ".":
                        check[next_row][next_col][key] = True #나 방문 했다!
                        q.append((next_row, next_col, cnt + 1, key)) #그리고 이동 했으니깐 cnt 증가 시킨다.

                    #열쇠를 줍는 부분 => 영어 소문자끼리 대소 구분 가능!, 비트 마스킹으로 키 줍기! 해당 인덱스 부분 1로 표시
                    elif "a" <= MAP[next_row][next_col] <= "f":
                        tmp_key = key | (1 << (ord(MAP[next_row][next_col]) - ord("a")))
                        check[next_row][next_col][tmp_key] = True
                        q.append((next_row, next_col, cnt + 1, tmp_key))
                    #문을 만나는 부분! => 내가 키를 가지고 있고 문을 열수 있는지 & 연산으로 판단
                    elif "A" <= MAP[next_row][next_col] <= "F":
                        if haveKey(key, MAP[next_row][next_col]):
                            check[next_row][next_col][key] = True
                            q.append((next_row, next_col, cnt + 1, key))

    return -1


N, M = map(int, sys.stdin.readline().split())

#이차원 그래프 배열 입력받기
MAP = [list(map(str,sys.stdin.readline().rstrip())) for _ in range(N)]


for i in range(N):
    for j in range(M):
        if MAP[i][j] == "0":
            start_row, start_col = i , j
            #민식이가 있는 곳은 이동할 수 있는 곳이니깐!
            MAP[i][j] = "."

print(bfs(start_row, start_col))




