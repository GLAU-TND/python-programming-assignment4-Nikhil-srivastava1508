l=eval(input())
n=int(input())
new=[]
for i in l:
  if i[0] not in mew:
    new.append(i[0])
dct={}
for i in new:
  dct[i]=[]
for i in dct:
  for j in l:
    if i==j[0]:
      dct[i].append(j[l])
dct2={}
r=0
for i in range(len(dct)):
  for j in range(i+1,len(dct)):
    res= len(set(dct[list(dct)[i]]) & set(dct[list(dct)[j]]))/float(len(set(dct[list(dct)(i)]) | set(dct[list(dct)[j]])))*100
    if 1!=j:
      dct2[r]=[round(res,2),list(dct)[j],list(dct)[i]]
      r=r+1
a=list(dct2.values())
for k in range(len(a)):
  if a[k][1]>a[k][2]:
    c=a[k][1]
    a[k][1]=a[k][2]
    a[k][2]=c

a.sort(key = lambda a: a[0],reverse=True)
l=[]
for q in range(n):
  l+=[(a[q][1],a[q][2])]
print(l)
