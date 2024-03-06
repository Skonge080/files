def is_unique(lst):
    unique_elements = set(lst)
    return len(unique_elements) == len(lst)

numbers = [1, 2, 3, 4, 5]
result = is_unique(numbers)
print(result)  # Выведет: True, так как каждое число встречается только один раз

numbers_with_duplicates = [1, 2, 3, 4, 5, 1]
result_with_duplicates = is_unique(numbers_with_duplicates)
print(result_with_duplicates)  # Выведет: False, так как есть повторяющиеся числа
