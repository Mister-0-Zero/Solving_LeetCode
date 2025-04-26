N, K = map(int, input().split())
n = list(map(int, input().split()))

count = 0

list_visited_direction = [0] * (max(n) + 1)

for i in range(K):
    num_direction = n[i]
    if list_visited_direction[num_direction] == 0:
        count += 1
    list_visited_direction[num_direction] += 1

res = count

for i in range(1, N - K + 1):
    pred_num_direction = n[i - 1]
    current_num_direction = n[i + K - 1]

    if list_visited_direction[pred_num_direction] == 1:
        count -= 1
    list_visited_direction[pred_num_direction] -= 1

    if list_visited_direction[current_num_direction] == 0:
        count += 1
    list_visited_direction[current_num_direction] += 1

    if count > res:
        res = count

print(res)