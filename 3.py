import random

# Генерация 100 случайных вещественных чисел и заполнение ими списка
random_numbers = [random.uniform(0, 100) for _ in range(100)]

# Сортировка списка
random_numbers.sort()

# Вывод отсортированного списка на экран
print(random_numbers)
