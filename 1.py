def remove_duplicates(lst):
    return list(set(lst))

input_list = input("Введите список элементов через пробел: ").split()
result = remove_duplicates(input_list)
print("Результат после удаления повторяющихся элементов:", result)
