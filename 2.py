numbers = []

# Запрашиваем 10 чисел с клавиатуры и добавляем их в список
for i in range(10):
    num = float(input("Введите число: "))
    numbers.append(num)

# Выводим сумму, максимальное и минимальное значения
print("Сумма чисел:", sum(numbers))
print("Максимальное значение:", max(numbers))
print("Минимальное значение:", min(numbers))
