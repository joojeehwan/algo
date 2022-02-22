from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)  # 대기트럭(truck_weights)을 담은 deque 생성
    bridge = deque([0 for i in range(bridge_length)])  # 다리길이만큼 0을 채워서 변수 생성
    time = 0  # 경과 시간
    bridge_weight = 0  # 다리를 건너고 있는 트럭의 무게
    # bridge의 크기가 0이 될때까지 반복
    while len(bridge) != 0:
        out = bridge.popleft()  # 다리를 건너는 첫번째 트럭(bridge[0])을 pop해줌
        bridge_weight -= out  # 다리 무게에서 다리를 건넌 트럭의 무게를 빼줌
        time += 1  # 시간을 더해줌

        if truck_weights:  # deque에 요소가 남아있으면 True

            # 현재 다리를 건너는 트럭의 무게와 다리에 오를 트럭의 무게의 합이
            if bridge_weight + truck_weights[0] <= weight:
                # 다리가 견딜 수 있는 무게 이하일때
                left = truck_weights.popleft()  # 대기트럭 deque에서 다음 트럭을 pop하고
                bridge_weight += left  # 다리를 건너고 있는 트럭 무게에 더하고
                bridge.append(left)  # 건너는 트럭 리스트에 넣어준다.
            else:
                # 다리가 견딜 수 있는 무게 초과일때
                bridge.append(0)  # 다음 트럭이 못지나 가므로 0을 채워준다.
    return time


# 2개의 자리에 [0. 0] 2개가 들어와야대서 1 ~ 2초 6 ~ 7초 이렇게 걸리는 것임

def solution(bridge_length, weight, truck_weights):
    time = 0
    # 다리위의 빈공간을 0으로 두는 것이 point
    q = [0] * bridge_length

    while q:
        q.pop(0)
        time += 1
        if truck_weights:
            # 다리위에 있는것하고 그 다음 들어오는 것의 합이 지탱할 수 있는 것의 무게보다 작으면
            # 다리 위로 올린다
            # pop을 사용해서 대기 리스트에서는 빼고
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return time
