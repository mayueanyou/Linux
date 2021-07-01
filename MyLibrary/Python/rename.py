import os,sys,random,torch

offset=4
file=os.listdir()

number=[]
for i in file:
    if i!= 'models' and i !='rename.py':
        number.append(int(i.split('_')[1].split('.')[0]))

if offset>0:
    number.sort(reverse=True)
if offset<0:
    number.sort()

for i in range(len(number)):
    file=os.listdir()
    for j in file:
        file=os.listdir()
        if j !='rename.py'and j !='models'and str(number[i]) == j.split('_')[1].split('.')[0]:
            new= j.replace(j.split('_')[1].split('.')[0],str(int(j.split('_')[1].split('.')[0])+offset))
            os.rename(j,new)
