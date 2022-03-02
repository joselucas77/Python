s = int(input())
h = s // 3600
r = s % 3600
m = r // 60
S = r % 60
print('%i:%i:%i'%(h,m,S))