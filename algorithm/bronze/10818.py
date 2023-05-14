num_of_int = int(input())

numbers = list(map(int, input().split()))

print("{} {}".format(min(numbers), max(numbers)))
