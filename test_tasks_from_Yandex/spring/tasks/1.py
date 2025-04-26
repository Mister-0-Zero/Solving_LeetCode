N, K = map(int, input().split())
n = list(map(int, input().split()))

count = 0

dir_vis_direction = {}

for i in range(K):
    num_direction = n[i]
    if num_direction in dir_vis_direction:
        dir_vis_direction[num_direction] += 1
    else:
        count += 1
        dir_vis_direction[num_direction] = 1

res = count

for i in range(1, N - K + 1):
    pred_num_direction = n[i - 1]
    current_num_direction = n[i + K - 1]

    if dir_vis_direction[pred_num_direction] == 1:
        count -= 1
    dir_vis_direction[pred_num_direction] -= 1

    if current_num_direction in dir_vis_direction:
        if dir_vis_direction[current_num_direction] == 0:
            count += 1
        dir_vis_direction[current_num_direction] += 1
    else:
        count += 1
        dir_vis_direction[current_num_direction] = 1

    if count > res:
        res = count

print(res)