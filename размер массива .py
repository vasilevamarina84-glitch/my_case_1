# Ввод размера массива
n = int(input("Введите размер массива N: "))

if n <= 0:
    print("Размер массива должен быть положительным целым числом.")
else:
    print(f"Введите ровно {n} целых чисел через пробел:")
    data = input().split()

    if len(data) != n:
        print(f"Ошибка: вы ввели {len(data)} чисел, но нужно ровно {n}.")
    else:
        try:
            A = list(map(int, data))
        except ValueError:
            print("Ошибка: все элементы должны быть целыми числами.")
        else:
            # Находим индексы первого вхождения минимума и максимума
            min_val = min(A)
            max_val = max(A)
            min_index = A.index(min_val)
            max_index = A.index(max_val)

            # Определяем границы (не включая сами min и max)
            left = min(min_index, max_index)
            right = max(min_index, max_index)

            # Суммируем отрицательные элементы между ними
            total = 0
            has_negative = False
            for i in range(left + 1, right):
                if A[i] < 0:
                    total += A[i]
                    has_negative = True

            if has_negative:
                print(f"Сумма отрицательных элементов между минимумом и максимумом: {total}")
            else:
                print("Между минимальным и максимальным элементами нет отрицательных чисел.")

input("Нажмите Enter, чтобы выйти...")