pieces=int(input())

prices=list(map(float, input().split(' ')))

minum=[float('inf') for i in range(pieces+1)]
minum[0]=0


#faz a forca bruta entre o numero e os numeros abaixo dele 
for i in range(pieces+1):
    for j in range(i):
        minum[i]=min(minum[i], minum[i-j-1]+prices[j])

print(minum[pieces])

#complexidade o(n²) -> n = pedacos de bolo
#complecidade problema da mochila é o(w) -> w= peso da mochila
