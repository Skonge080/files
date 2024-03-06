def average_of_negatives(lst):
    negatives = [num for num in lst if num < 0]
    if not negatives:
        return "No negative numbers in the list."
    else:
        return sum(negatives) / len(negatives)

# Пример использования
my_list = [1, -2, 3, -4, 5, -6]
result = average_of_negatives(my_list)
print("Среднее арифметическое отрицательных элементов:", result)
