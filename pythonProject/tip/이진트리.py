


#이진 트리 생성
class TreeNode() : 
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        
        
node1= TreeNode()
node1.data = '화사'

node2= TreeNode()
node2.data = '솔라'
node1.left = node2

node3= TreeNode()
node3.data = '문별'
node1.right = node3

node4= TreeNode()
node4.data = '휘인'
node2.left = node4

node5= TreeNode()
node5.data = '쯔위'
node2.right = node5

node6= TreeNode()
node6.data = '선미'
node3.left = node6
    
print(node1.data, end=' ')
print()
print(node1.left.data, node1.right.data, end=' ')
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data, end=' ')



#이진 탐색 트리 삽입


## 전역 변수 선언 부분 ##
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인 코드 부분 ##

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)
#print(memory)

for name in nameAry[1:]:
    
    node = TreeNode() # 새 노드 생성
    node.data = name

    current = root # 항상 루트 노드부터 시작. 즉, 현재 작업 노드는 항상 루트 노드부터 진행한다.
                   # 항상 루트부터 시작해서, 비교를 진행
    while True:
        if name < current.data: #문자를 아스코드로 변환해서 문자열 값 비교
            #작은건 왼쪽
            if current.left == None:
                current.left = node
                break
            #다음 비교를 위해서, current를 바꿔줌
            current = current.left
        else:
            #큰건 오른쪽
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)


## 검색, 삭제도 위의 삽입과정은 동일
## => 데이터가 있어야, 검색도 삭제도 가능하다.
## 데이터 검색

findName = '마마무'     # 찾고자 하는 데이터

current = root          # 루트 노드부터 검색 시작
while True:             # 데이터를 찾거나 못 찾을 때까지 반복
    if findName == current.data:
        print(findName, '을(를) 찾음')
        break
    elif findName < current.data:
        if current.left == None:
            print(findName, '이(가) 트리에 없음')
            break
        current = current.left
    else:
        if current.right == None:
            print(findName, '이(가) 트리에 없음')
            break
        current = current.right
        
        

##데이터 삭제

deleteName = '마마무'

current = root
parent = None
while True:
    if deleteName == current.data:
        #노드 삭제후 다시 연결
        if current.left == None and current.right == None:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            del (current)

        elif current.left != None and current.right == None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
            del (current)

        elif current.left == None and current.right != None:
            if parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
            del (current)

        print(deleteName, '이(가) 삭제됨')
        break

    elif deleteName < current.data:
        if current.left == None:
            print(deleteName, '이(가) 트리에 없음')
            break
        parent = current
        current = current.left
    else:
        if current.right == None:
            print(deleteName, '이(가) 트리에 없음')
            break
        parent = current
        current = current.right