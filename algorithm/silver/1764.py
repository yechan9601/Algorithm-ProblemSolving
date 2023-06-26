import sys

# N, M 입력
n, m = map(int, input().split())

mydict = {}
for i in range(n + m):
  name = sys.stdin.readline().rstrip()
  if name in mydict.keys():
    mydict[name] = 2
  else:
    mydict[name] = 1

cnt = 0
for value in mydict.values():
  if value == 2:
    cnt += 1
print(cnt)

mydict = dict(sorted(mydict.items()))
for key, value in mydict.items():
  if value == 2:
    print(key)