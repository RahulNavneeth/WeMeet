f=open('C:\Python39\hmmm.txt','r').readlines()
countAnd=0

for i in f:
    i=i.lower().replace('\n', "") 
    if i=='and':
        countAnd+=1
print(countAnd)