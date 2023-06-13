n, k = map(int, input().split())

def factorial(x):
  if x == 1 or x == 0:
    return 1
  return x * factorial(x - 1)

# nCr = n! / r! * (n - r)!
c = factorial(n) // (factorial(k) * factorial(n - k))
print(c)