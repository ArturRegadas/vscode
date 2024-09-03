
# Lê o número de pedaços
N = int(input())

# Lê os preços de cada pedido
V = list(map(float, input().split()))



min_cost = {i: float('inf') for i in range(N + 1)}
min_cost[0] = 0  


for i in range(1, N + 1):
    for j in range(i):
        min_cost[i] = min(min_cost[i], min_cost[j] + V[i-j-1])


print(f"{min_cost[N]:.2f}")


