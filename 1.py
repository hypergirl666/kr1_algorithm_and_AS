def main():
    # Читаем всю строку входных данных
    data = input().split()

    # Разделяем на множества A и B
    A = []
    B = []
    current_set = A
    zero_count = 0

    for item in data:
        num = int(item)
        if num == 0:
            zero_count += 1
            if zero_count == 1:
                current_set = B
            elif zero_count == 2:
                break
        else:
            current_set.append(num)

    # Создаем массивы для отметки встречаемости чисел (1..20000)
    max_num = 20000
    in_A = [False] * (max_num + 1)
    in_B = [False] * (max_num + 1)

    # Отмечаем элементы множества A
    for num in A:
        if 1 <= num <= max_num:
            in_A[num] = True

    # Отмечаем элементы множества B
    for num in B:
        if 1 <= num <= max_num:
            in_B[num] = True

    # Находим симметрическую разность
    result = []
    for num in range(1, max_num + 1):
        # Число принадлежит симметрической разности, если оно есть только в одном из множеств
        if in_A[num] != in_B[num]:
            result.append(num)

    # Выводим результат
    if not result:
        print(0)
    else:
        # Формируем строку результата
        output = []
        for num in result:
            output.append(str(num))
        print(' '.join(output))


if __name__ == "__main__":
    main()