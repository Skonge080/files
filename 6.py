matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Найдем сумму элементов каждого столбца
column_sums = [sum(column) for column in zip(*matrix)]

# Отсортируем столбцы по возрастанию их сумм
sorted_columns = [column for _, column in sorted(zip(column_sums, zip(*matrix)))]

print("Суммы элементов столбцов:", column_sums)
print("Отсортированные столбцы по суммам:", sorted_columns)
