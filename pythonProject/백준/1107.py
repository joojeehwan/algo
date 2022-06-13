import sys

input = sys.stdin.readline

target = int(input())

n = int(input())

broken = list(map(int, input().split()))

#현재 채널에서 + 혹은 -만 사용!하는 경우

min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    #왜 str로 바꾸나?! nums 중에서 하나의 숫자만 뽑기 위해서! 그렇게 한 것!
    # str로 안바꾸면 하나의 숫자를 뽑을 수가 없으니깐!
    # print(nums)
    for j in range(len(nums)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in broken:
            break

        #고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            #아 abs(int(nums) - target) 부분이 ++ , -- 와 같은 역활을 한다.
            #거기다가 숫자의 길이를 더해주면,,
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)

'''

결국 2가지 케이스가 존재하는 것! 

 1. 현재채녈에서 희망채널까지 + , - 로 이동하는 경우
 2. 모든 채널을 순회하면서 해당 채널에서 희망채널까지 +- 버튼으로 이동했을떄의 횟수
'''


'''

풀이법 및 코드 설명
브루트포스 방식으로 모든 경우의 수를 탐색한다.

 

처음에는 고장나지 않은 숫자들로 만들 수 있는 모든 순열을 만들어주고, target과 가장 가까운 순열을 구해 두 숫자 사이의 차이를 구하고자 했다.

 

하지만, 순열을 만드는 과정에서 요소를 중복해서 뽑을 수 있어야하기 때문에 (Ex ) 5555 등..) 기존에 알고 있던 itertools.permutations를 사용할 수 없었다.

 

따라서, 모든 가능한 수에 대하여 해당 작업을 처리해주었다.

 

여기서 range를 N의 최대 범위인 500,000이 아닌 그 두 배 1,000,000로 해준 것은, 수빈이가 이동하려는 채널의 범위는 500,000 이하이지만 채널 자체는 무한대라는 점 때문이다.

 

따라서, target와 가장 가까운 숫자를 찾을 때 target보다 작은 값은 물론이고 target보다 큰 값도 찾아줘야하고, 이 값은 500,000 이상도 가능하다.

 

만약에 수빈이가 이동하려는 채널이 500,000이고, 리모컨의 숫자 중 1, 2, 3, 4, 5가 고장났다고 가정하자.

 

이 때, range의 범위가 500,000으로 제한되면, 시작점인 100번에서 +만 눌러서 500,000까지 도달하는 총 499,900번 버튼을 클릭하게 할 것이다.

 

하지만 물론 이것은 최적의 해가 아니다.

 

600,000에서 -를 100,000번 눌러 target에 도달하는 것이 최적의 해일 것이다.

 

이러한 이유 때문에 range는 1,000,000까지로 설정해주어야 한다.

https://seongonion.tistory.com/99

'''