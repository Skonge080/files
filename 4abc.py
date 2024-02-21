arr=[[1, 2, 3],[4, 5, 6]]
sum=0
for row in arr:
  for elem in row:
    sum += elem
    print(sum, end=' ')
