def main():
    # Чтение входных данных
    n = int(input())
    participants = []

    for i in range(n):
        data = input().split()
        login = data[0]
        solved = int(data[1])
        penalty = int(data[2])
        participants.append((login, solved, penalty))

    # Функция сравнения: возвращает True если a должен быть перед b
    def should_go_before(a, b):
        # Сначала по решённым задачам (убывание)
        if a[1] != b[1]:
            return a[1] > b[1]
        # Затем по штрафу (возрастание)
        if a[2] != b[2]:
            return a[2] < b[2]
        # Наконец по логину (лексикографически)
        return a[0] < b[0]

    # In-place quick sort
    def quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)

    def partition(arr, low, high):
        # Выбираем опорный элемент (середина)
        mid = (low + high) // 2
        pivot = arr[mid]

        # Меняем опорный с последним элементом
        arr[mid], arr[high] = arr[high], arr[mid]

        i = low
        for j in range(low, high):
            if should_go_before(arr[j], pivot):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        # Ставим pivot на правильное место
        arr[i], arr[high] = arr[high], arr[i]
        return i

    # Сортируем
    quicksort(participants, 0, n - 1)

    # Вывод
    for p in participants:
        print(p[0])


if __name__ == "__main__":
    main()