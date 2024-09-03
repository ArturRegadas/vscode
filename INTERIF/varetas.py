cont = 1
while True:
    result = {'1': 0, '2': 0, '3': 0}
    price = {'1': 5, '2': 10, '3': 15, '4': 20, '5': 50}
    
    pessoa = input().strip()
    if pessoa == '-1':
        break
    
    varetas = []
    while True:
        varetas1 = input().strip().split()
        varetas += varetas1
        if varetas1[-1] == '-1':
            break

    for i in varetas:
        if i == '0':
            if pessoa == '1':
                pessoa = '2'
            elif pessoa == '2':
                pessoa = '3'
            else:
                pessoa = '1'
        elif i == '-1':
            break
        else:
            result[pessoa] += price[i]
    max_pontuacao = max(result.values())
    vencedores = [jogador for jogador, pontos in result.items() if pontos == max_pontuacao]

    if cont != 1:
        print() 
    nad="Ganhador" if len(vencedores)==1 else "Empate"
    print(f"RODADA {cont}")
    print(f"{nad} com {max_pontuacao} pontos")
    print("Jogador " + ", Jogador ".join(vencedores))
    
    cont += 1
