def maiorIdade():
    dicionario = {}
    while True:
        nome = str(input("Digite um nome: "))
        idade = int(input("Digite sua idade: "))
        dicionario[idade]=nome
        continua = str(input("Deseja cadastrar mais alguém? (s/n) "))
        if continua.lower() == "n":
            break
    x = 0
    for i in dicionario.keys():
        if i > 17:
            maiorIdade = []
            maiorIdade.append(dicionario[i])
            x += 1
    if x == 0:
        print("Não há maiores de idade nessa lista")
    else:
        print("Os maiores de idade são:\n",maiorIdade)

maiorIdade()