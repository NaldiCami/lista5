def ordenaChave():
    
    dic = {"Kaue":"Portal","Camila":"Guitar Hero","José":"Friv"}
    
    #Separando
    chaves = []
    for i in dic.keys():
        chaves.append(i)
    chaves.sort()
    print(chaves)
    
ordenaChave()
        