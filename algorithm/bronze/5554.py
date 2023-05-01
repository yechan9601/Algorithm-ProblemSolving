"""
Inputs: 
- home_to_school_sec
- school_to_pc_sec
- pc_to_academy_sec
- academy_to_home_sec

60 seconds = 1 minute.

Outputs:
 - final_min, final_sec
"""

times = []

for i in range(4):
  times.append(int(input()))

total_time = sum(times)

print(total_time // 60)
print(total_time % 60)
