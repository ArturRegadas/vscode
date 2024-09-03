def menor_Chave(chave, queue):
    menor=float('inf')
    o_nome=None
    for i in chave:
        if chave[i] < menor and i in queue:
            menor=chave[i]
            o_nome=i
    return o_nome
def PrimArrombado(graph, r):
    chave={}
    predecessor={}
    queue=[]
    for i in graph:
        chave[i]=float('inf')
        predecessor[i]=None
        queue.append(i)
    queue.remove(r)
    queue.insert(0, r)
    chave[r]=0
    while queue:
        u = menor_Chave(chave, queue)
        queue.remove(u)
        for i in graph[u]:
            if i in queue and graph[u][i]< chave[i]:
                predecessor[i]=u
                chave[i]=graph[u][i]
    return chave, predecessor


data= input("").split(' ')
graph={}
for i in range(int(data[1])):
    edge=input().split(' ')
    if not edge[0] in graph:
        graph[edge[0]]={}

    graph[edge[0]][edge[1]]=int(edge[2])
    if not edge[1] in graph:
        graph[edge[1]]={}
    graph[edge[1]][edge[0]]=int(edge[2])

chave, predecessor=PrimArrombado(graph, '1')
som=0
for i in predecessor:
    if not predecessor[i] == None:
        som+=graph[i][predecessor[i]]
print(som)