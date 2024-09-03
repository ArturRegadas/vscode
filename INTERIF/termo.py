bigTORORO=[1, 1, 1, 2, 2]
constante_1=0
constante_2=4
while True:
    try:
        pra_nao_cansar=int(input())
        while len(bigTORORO)<pra_nao_cansar:
            bigTORORO.append(bigTORORO[constante_1]+bigTORORO[constante_2])
            constante_1+=1
            constante_2+=1
        print(bigTORORO[pra_nao_cansar-1])
    except:
        break

