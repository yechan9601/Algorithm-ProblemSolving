"""
1. int row_num, int col_num, String row, list boong_eo_bbang
2. for loop
"""
row_num = 0
col_num = 0
row = ""
boong_eo_bbang = []

row_num, col_num = input().split()
row_num = int(row_num)
col_num = int(col_num)

for i in range(row_num):
  row = input()[::-1]
  boong_eo_bbang.append(row)

for i in range(row_num):
  print(boong_eo_bbang[i], end="\n")
  
  