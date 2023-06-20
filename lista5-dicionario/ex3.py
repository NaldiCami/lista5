def cadastroTelefone():
    listaNome = []
    listaTel = []
    while True:
        nome = input("Digite um nome: ")
        tel = int(input("Digite o telefone dessa pessoa: "))
        listaNome.append(nome)
        listaTel.append(tel)
        repete = input("Deseja cadastrar mais algum telefone? (s/n) ")
        if repete == "n":
            break
    dicionarioLista = {}
    x = len(listaNome)
    for item in range(x):
        nome = listaNome[item]
        tel = listaTel[item]
        dicionarioLista[tel]=nome
    print(dicionarioLista)

cadastroTelefone()