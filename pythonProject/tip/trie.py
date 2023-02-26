'''

https://velog.io/@gojaegaebal/210126-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%8050%EC%9D%BC%EC%B0%A8-%ED%8A%B8%EB%9D%BC%EC%9D%B4Trie-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B0%9C%EB%85%90-%EB%B0%8F-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0feat.-Class

트라이(Trie)란?

트라이(Trie)란 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조다. 래딕스 트리(radix tree)나 접두사 트리(prefix tree)라고도 한다.
retrieval(탐색)에서 trie를 따왔다고도 한다.
이 자료구조를 활용해 검색어 자동완성, 사전에서 찾기 그리고 문자열 검사 등을 한다고 한다.


사용 목적
문자열의 탐색을 할 때, 단순하게 하나씩 비교하면서 탐색을 하는것보다 시간복잡도 측면에서 훨씬 효율적이다. 단, 빠르게 탐색이 가능하다는 장점이 있지만 각 노드에서 자식들에 대한 포인터들을 배열로 모두 저장하고 있다는 점에서 저장 공간의 크기가 크다는 단점도 있다.

시간 복잡도
제일 긴 문자열의 길이를 L 총 문자열들의 수를 M이라 할 때 시간복잡도는 아래와 같다.

생성 시간 복잡도 : O(M*L), 모든 문자열들을 넣어야하니 M개에 대해서 트라이 자료구조에 넣는건 가장 긴 문자열 길이만큼 걸리니 L만큼 걸려서 O(M*L)만큼 걸립니다. 물론 삽입 자체만은 O(L)만큼 걸린다.
탐색 시간 복잡도: O(L), 트리를 타고 들어가봤자 가장 긴 문자열의 길이만큼만 탐색하기 때문에 O(L)


'''

'''

Node를 Class로 만들기
- Key에는 해당 노드의 문자가 들어가고, Child에는 자식 노드가 포함되게 된다.
- Data는 문자열이 끝나는 위치를 알려주는 역할을 한다. 예를 들어서 “car”이 “r”에서 끝날 때, “r”을 key로 가지는 노드의 data에 “car”를 입력한다.해당 노드에서 끝나는 문자열이 없을 경우에는 None으로 그대로 놔둔다.



'''

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

'''

Trie구조 만들기 : 삽입과 검색기능 구현

'''


class Trie(object):
    def __init__(self):
        self.head = Node(None)
  # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.children[char]
        #문자열이 끝난 지점의 노드의 data값에 해당 문자열을 입력
        curr_node.data = string
    # 문자열이 존재하는지 search
    def search(self, string):
        #가장 아래에 있는 노드에서 부터 탐색 시작
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        #탐색이 끝난 후 해당 노드의 data값이 존재한다면
        #문자가 포함되어있다는 뜻이다.
        if curr_node.data != None:
            return True