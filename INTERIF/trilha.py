data=input().split(' ')
inout=input().split(' ')
graph={}
for i in range(int(data[1])):
    edge=input().split(' ')
    if not edge[0] in graph:
        graph[edge[0]]={}

    graph[edge[0]][edge[1]]=int(edge[2])
    if not edge[1] in graph:
        graph[edge[1]]={}
    graph[edge[1]][edge[0]]=int(edge[2])
queue=[inout[0]]
processed=[]
path={}
while queue:
    current=queue[0]
    for i in graph[current]:
        if not i in queue and not i in processed:
            queue.append(i)
            if not i in path:
                path[i]={}
            path[i][current]=graph[current][i]

    processed.append(current)
    queue.pop(0)
pathresult=[]
atual=inout[1]


while atual !=inout[0] :
    preco=float('inf')
    for i in path[atual]:
        if i == inout[0]:
            oatual=i
            break
        elif preco > path[atual][i]:
            preco=path[atual][i]
            oatual=i
    atual=oatual
    pathresult.append(atual)

pathresult.reverse()
pathresult.append(inout[1])

        

print(f"Percurso: {'--> '.join(pathresult)}")