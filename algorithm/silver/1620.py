import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 도감 목록 입력
pokemon = {}
pokemon_array = [0]
for i in range(1, n + 1):
  # name, index 형태로 dict 저장
  name = input().rstrip()
  pokemon[name] = i
  pokemon_array.append(name)

# 맞춰야하는 목록 및 결과
for j in range(m):
  problem = input().rstrip()
  if problem.isdigit():
    # value로 key 찾기
    print(pokemon_array[int(problem)])
    # for key, value in pokemon.items():
    #   if value == int(problem):
    #     print(key)
  else:
    # key로 value 찿기
    print(pokemon[problem])

    
    

