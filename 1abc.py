import random

arr = []

for i in range(10):
    n = round(random.random() * 100)
    arr.append(n)

print("Исходный список:", arr)

lst = []
i = 0

while i < len(arr):
    if 20 < arr[i] < 40:
        lst.append(arr[i])
        del arr[i]
    else:
        i += 1

print("Список после удаления по условию:", arr)
print("Список удаленных:", lst)
