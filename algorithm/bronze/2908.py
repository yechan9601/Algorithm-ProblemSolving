A, B = map(str, input().split())

for i in range(2, -1, -1) :
  if (int(A[i]) < int(B[i])) :
    print(B[ : : -1])
    break
  elif (int(B[i]) < int(A[i])) :
    print(A[ : : -1])
    break
  