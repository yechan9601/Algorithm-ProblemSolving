a = input()
b = input()

c = int(a) * int(b[2])
d = int(a) * int(b[1])
e = int(a) * int(b[0])
total = c + d * 10 + e * 100

print("{0}\n{1}\n{2}\n{3}".format(c, d, e, total))
