p=int(input())
bk=[]
for s in range(0,p):
 ja=input()
 bk.append(ja)
bb=[]
for s in zip(*bk):
 if(s.count(s[0])==len(s)):
  bb.append(s[0])
 else:
  break
print(''.join(bb))
