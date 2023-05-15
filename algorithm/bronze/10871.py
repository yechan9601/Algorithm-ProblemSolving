N, X = map(int, input().split())

A = [0] * N
A = list(map(int, input().split()))

for i in range(N):
  if (A[i] < X) :
    print(A[i], end=" ")