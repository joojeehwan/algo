def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

#아름답다
'''
progresses = [93,30,55]

speeds = [1,30,5]  



1) count, time 변수를 설정해둔다. 

2) 첫번째가 100이 될때까지 loop 를 돌며 time 을 늘린다. 

    else --> time+=1

3) (time =7) 이 되면  첫번째 값이(93) 100이 되어 if에 따라 pop 되고 count +=1

4) 현재 time 이 7이기 때문에 두번째 값(30)도 if에 따라 pop 되고 count +=1 

5) 세번째 값은 100이 안되기 때문에 loop를 돌며 time 을 늘리는데 

    2) 번과 달리 그전에 완성된 친구들 count 값이 있기 때문에 이 친구들을 출시해줘야함 

        따라서 answer 리스트에 append하고 count 초기화!!! 

    그후에 loop를 돌며 time 을 늘리는데 

6) 세번째 값(55)이 100을 넘으면 count +=1 하고 

    이 count 를 다시한번 answer 리스트에 append 해줌으로써 마지막 제품까지 출시 ! 



'''
