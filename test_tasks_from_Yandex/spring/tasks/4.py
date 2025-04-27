from datetime import datetime, timedelta

def parse_data(num_entries: int, sort_index: int):
    """Читает данные и сортирует по нужному индексу."""
    data = []
    for _ in range(num_entries):
        number, time_start, time_end, cost = input().split()
        time_start = datetime.strptime(time_start, "%H:%M:%S")
        time_end = datetime.strptime(time_end, "%H:%M:%S")
        cost = int(cost)
        data.append([number, time_start, time_end, cost])
    return sorted(data, key=lambda x: x[sort_index])

def prepare_min_cost(data_train):
    """Предрасчитывает минимальные стоимости поездов справа налево."""
    min_cost_from_here = [None] * len(data_train)
    min_cost_from_here[-1] = data_train[-1]
    for i in range(len(data_train) - 2, -1, -1):
        if data_train[i][3] <= min_cost_from_here[i + 1][3]:
            min_cost_from_here[i] = data_train[i]
        else:
            min_cost_from_here[i] = min_cost_from_here[i + 1]
    return min_cost_from_here

def find_next_train(data_train, min_cost_from_here, end_time, start_index):
    """Находит подходящий поезд с минимальной стоимостью."""
    min_start_time = end_time + timedelta(minutes=15)
    while start_index < len(data_train) and data_train[start_index][1] < min_start_time:
        start_index += 1

    if start_index == len(data_train):
        return None, float("inf"), start_index

    num, start, end, cost = min_cost_from_here[start_index]
    return num, cost, start_index

def main():
    N = int(input())
    data_el = parse_data(N, 2)

    M = int(input())
    data_train = parse_data(M, 1)

    min_cost_from_here = prepare_min_cost(data_train)

    best_el = None
    best_train = None
    current_element_index = 0
    train_index = 0

    # Предрассчитаем первый поезд
    first_num_tr, first_cost_tr, train_index = find_next_train(data_train, min_cost_from_here, data_el[0][2], train_index)
    best_el = data_el[0][0]
    best_train = first_num_tr

    min_total_cost = data_el[0][3] + first_cost_tr

    for i, (num, start, end, cost) in enumerate(data_el):
        if cost < data_el[current_element_index][3]:
            num_tr, cost_tr, train_index = find_next_train(data_train, min_cost_from_here, end, train_index)
            if cost + cost_tr < min_total_cost:
                current_element_index = i
                best_el = num
                best_train = num_tr
                min_total_cost = cost + cost_tr

    print(best_el)
    print(best_train)

if __name__ == "__main__":
    main()
