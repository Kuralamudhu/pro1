from itertools import combinations
v,i=map(int,input().split())
d=len(str(v))
lst=list(combinations(str(v),d-i))
lst=sorted(lst)
print(*lst[0],dec='')
