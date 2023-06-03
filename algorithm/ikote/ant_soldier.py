"""
- constraints: 
  - 붙어있는 창고를 선택할 수 없음

- 점화식:
  a[i] = i번째 식량창고까지의 최적의 해
  k[i] = i번째 식량창고에 있는 식량의 양
  a[i] = max(a[i-1], a[i-2] + k[i])

"""

n = int(input())

storage = list(map(int, input().split()))

d = [0] * 100

d[0] = storage[0] # 주어진 식량창고가 첫번째 하나밖에 없을 때 최적의 해
d[1] = max(storage[0], storage[1]) # 주어진 식량창고가 두번째까지만 있을 때 최적의 해
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + storage[i])

print(d[n - 1])

