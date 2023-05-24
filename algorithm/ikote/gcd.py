a, b = map(int, input('Enter A B\n').split())


# Euclid not using recursive
def gcd(a, b):
  while b != 0:
    temp = b
    b = a % b
    a = temp
  return a


# Euclid using recursive
def gcd_recursive(a, b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)


# # Example usage
# num1 = 24
# num2 = 36

result = gcd(a, b)
print("GCD:", result)  # Output: 12

result2 = gcd_recursive(a, b)
print("GCD using Recursive:", result2)
