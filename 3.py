def main():
    # Чтение входных данных
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        N = int(data[0])
        K = int(data[1])
        M = int(data[2])
        adj = [[0] * (N + 1) for _ in range(N + 1)]
        idx = 3
        for _ in range(M):
            a = int(data[idx]);
            b = int(data[idx + 1])
            idx += 2
            adj[a][b] = 1
            adj[b][a] = 1

    # Функция для подсчета сплоченности команды
    def cohesion(team):
        cnt = 0
        for i in range(len(team)):
            for j in range(i + 1, len(team)):
                if adj[team[i]][team[j]]:
                    cnt += 1
        return cnt

    # Функция для подсчета количества единиц в маске
    def count_ones(mask):
        cnt = 0
        while mask:
            cnt += mask & 1
            mask >>= 1
        return cnt

    # Генерация всех комбинаций с помощью битовых масок
    best_mask = 0
    max_sum_cohesion = -1

    # Перебираем все маски с ровно K единицами
    for mask in range(1 << N):
        # Считаем количество единиц в маске
        if count_ones(mask) != K:
            continue

        # Формируем команды
        teamA = []
        teamB = []
        for i in range(N):
            if mask & (1 << i):
                teamA.append(i + 1)  # +1 т.к. участники с 1 до N
            else:
                teamB.append(i + 1)

        # Считаем сплоченность
        cohA = cohesion(teamA)
        cohB = cohesion(teamB)
        total = cohA + cohB

        if total > max_sum_cohesion:
            max_sum_cohesion = total
            best_mask = mask

    # Формируем ответ
    result = []
    for i in range(N):
        if best_mask & (1 << i):
            result.append(i + 1)

    # Запись результата
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(map(str, result)))


if __name__ == "__main__":
    main()