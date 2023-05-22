N = int(input())

fear_rate_list = list(map(int, input().split()))

num_of_group = 0

fear_rate_list.sort(reverse=False)  # 오름차순
num_of_people_in_group = 0

for i in range(len(fear_rate_list)):
  num_of_people_in_group += 1
  if fear_rate_list[i] <= num_of_people_in_group:
    num_of_group += 1
    num_of_people_in_group = 0

print(num_of_group)
