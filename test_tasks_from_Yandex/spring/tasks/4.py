from datetime import datetime, timedelta

def parsing_data(kol_str, ind_sort):
    data = []
    for i in range(kol_str):
        number, time_start, time_end, cost = input().split()
        time_start = datetime.strptime(time_start, "%H:%M:%S")
        time_end = datetime.strptime(time_end, "%H:%M:%S")
        cost = int(cost)
        data.append([number, time_start, time_end, cost])
    return sorted(data, key=lambda x: x[ind_sort])

N = int(input())
data_el = parsing_data(N, 2)
M = int(input())
data_train = parsing_data(M, 1)

# print(data_el)
# print(data_train)

def cost_train(end):
    global data_train
    ind = 0
    min_start_train_time = end + timedelta(minutes=15)
    while ind < len(data_train) and data_train[ind][1] < min_start_train_time:
        ind += 1

    if ind == len(data_train):
        return None, float('inf')

    data_train = data_train[ind:]
    num, start, end, cost = min(data_train, key=lambda x: x[3])
    return cost, num

ind = 0
min_cost = float('inf')
i = 0
cost_tr, num_tr = cost_train(data_el[0][2])
b_num_el, b_num_tr = data_el[0][0], num_tr
for num, start, end, cost in data_el:
    if cost < data_el[ind][3]:
        cost_tr, num_tr = cost_train(end)
        if cost + cost_tr < min_cost:
            ind = i
            b_num_el = num
            b_num_tr = num_tr
            min_cost = cost + cost_tr
    i += 1

print(b_num_el)
print(b_num_tr)

