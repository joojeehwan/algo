def solution(wolf_count, sheep_count, cabbage_count, wolf_weight, sheep_weight, cabbage_weight, limit):

    total_wolf = wolf_weight * wolf_count
    total_sheep = sheep_weight *  sheep_count
    total_cabbage = cabbage_weight * cabbage_count

    if limit >= (total_wolf + total_sheep + total_cabbage):
        answer = 1
        return answer

    else:
        answer = 0
    return answer