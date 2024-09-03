figurinha = input()

figurinha = float(figurinha[2:])

m = input().split(' ')
price = [0.25, 0.1, 0.05, 0.01]
qtd = []
moedas = []

for i in range(4):
    qtd.append(int(m[i]))
    moedas.append(int(m[i]) * price[i])

maximo_figurinhas = int(sum(moedas) * 100 // (figurinha * 100))

print(f"{maximo_figurinhas:.0f}")

som = 0
total = maximo_figurinhas * figurinha * 100


price = [p * 100 for p in price]

for i in range(4):
    totali = int(total // price[i])
    if totali > qtd[i]:
        totali = qtd[i]
    total -= totali * price[i]
    som += totali

print(f"{sum(qtd) - som:.0f}")
