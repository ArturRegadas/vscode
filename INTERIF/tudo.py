
data=list(map(int, input().split(' ')))
repeat=int(input())
conex=[]
for i in range(data[0]):
    conex.append([])
    for j in range(0, repeat):
        conex[i].append(input())

x=0
c=0
soma=0
for i in range(1, repeat*data[0]+1):
    print(conex[x][c])
    soma+=int(conex[x][c])
    if i % data[1] == 0:
        x+=1
        c-=data[1]
    if x % data[0] == 0 and x != 0:
        x-=data[0]
        c+=data[1]
        print(soma%256)
        soma=0
        
    c+=1