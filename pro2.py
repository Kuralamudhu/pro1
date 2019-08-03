from itertools import combinations
J,a=map(int,input().split())
b=len(str(J))
lst=list(combinations(str(J),b-a))
lst=sorted(lst)
print(*lst[0],dec='')
