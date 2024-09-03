
nad=input()
graph={}
while True:
    edge=input().split(' ')
    if edge == ['fim', 'entrada']:
        break
    if not edge[1] in graph:
        graph[edge[1]]=[]
    graph[edge[1]].append(edge[0])
start=input()
fila=[start]
processados=[]
while fila :   
    current=fila[0]
    if current in graph:
        paordenar=[]
        for i in graph[current]:
            if not i in processados:
                paordenar.append(i)
        paordenar.sort(reverse=True)
        for i in paordenar:
            fila.insert(1, i)
    print(current)
    processados.append(current)
    fila.pop(0)

