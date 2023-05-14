"""
sudo code

how_many_lines = int(input())
scores = []

for i in range(how_many_lines):
  OX_str = input()
  score = 0
  for i in range(len(OX_str)):
    if (OX_str[i] == 'O'):
      if (score == 0):
        score = 1
      else :
        score += 1
      scores.append(score)
  print(sum(scores))

"""

how_many_lines = int(input())

for i in range(how_many_lines):
  OX_str = input()
  score = 0
  scores = []
  for j in range(len(OX_str)): 
    if (OX_str[j] == 'O'):
      if(score == 0):
        score = 1
      else :
        score += 1
      scores.append(score)
    else :
      score = 0
      scores.append(score)
  print(sum(scores))
    