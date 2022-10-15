
#조합
nums = [1, 2, 3, 4]
num_cnt = len(nums)
combi_list = []
PICK_CNT = 2


def combination_recursive(now_idx, combi):
    if len(combi) == PICK_CNT:
        combi_list.append(combi[:])
        return
    for other_idx in range(now_idx, num_cnt):
        # 자기 다음부터 보기 때문에 사용했는지 확인 안함!!!
        combi.append(nums[other_idx])
        combination_recursive(other_idx+1, combi)
        combi.pop()


combination_recursive(0, [])
print(combi_list)


#순열
nums = [1, 2, 3, 4]
num_cnt = len(nums)
used = [0] * num_cnt
permu_list = []
PICK_CNT = 2

def permutaion_recursive(cnt, permu):
    if cnt == PICK_CNT:
        permu_list.append(permu[:])
    for i in range(num_cnt):
        # 처음부터 보기 때문에 사용했는지 확인하는게 포인트!!!
        if not used[i]:
            used[i] = 1
            permu.append(nums[i])
            permutaion_recursive(cnt+1, permu)
            used[i] = 0
            permu.pop()

permutaion_recursive(0, [])
print(permu_list)