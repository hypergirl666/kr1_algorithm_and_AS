def main():
    n = int(input())

    # Инициализируем переменные для максимальных и минимальных значений
    max1 = max2 = max3 = -10 ** 18  # три наибольших
    min1 = min2 = 10 ** 18  # два наименьших

    for i in range(n):
        num = int(input())

        # Обновляем три максимальных значения
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

        # Обновляем два минимальных значения
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    # Вычисляем два возможных варианта максимального произведения
    product1 = max1 * max2 * max3  # три самых больших
    product2 = min1 * min2 * max1  # два самых маленьких и одно самое большое

    # Выбираем максимальный вариант без использования max()
    result = product1
    if product2 > product1:
        result = product2

    print(result)


if __name__ == "__main__":
    main()