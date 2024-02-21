arr=[[1, 2, 3], [4, 5, 6]]
sum=0
for i in range (len(arr)):
  for j in range (len(arr[i])):
    sum += arr[i][j]
    print(sum, end= ' ')
