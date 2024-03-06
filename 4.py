# Создаем пустой список
numbers = []

# Цикл для ввода 10 чисел
for _ in range(10):
    num = float(input("Введите число: "))
    numbers.append(num)

# Сортировка списка
numbers.sort()

# Вывод отсортированного списка с каждым числом, умноженным на 10
for num in numbers:
    print(num * 10)
