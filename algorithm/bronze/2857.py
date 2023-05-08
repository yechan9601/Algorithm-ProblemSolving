names = []
for i in range(5):
  str = input()
  names.append(str)

fbi_exist = False

for i in range(5):
  if ("FBI" in names[i]):
    print(i + 1)
    fbi_exist = True
  if (i == 4 and fbi_exist == False):
    print("HE GOT AWAY!")
