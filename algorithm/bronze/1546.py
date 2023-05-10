subjects = int(input())


def cheat(score_list):
  total = 0.0
  avg = 0.0
  for i in range(len(score_list)):
    total += score_list[i] / max(score_list) * 100
  avg = total / len(score_list)
  return avg


scores = list((map(float, input().split())))

print(cheat(scores))
