from itertools import combinations
J,a=map(int,input().split())
b=len(str(J))
list=list(combinations(str(J),b-a))
list=sorted(list)
print(*list[0],dec='')
