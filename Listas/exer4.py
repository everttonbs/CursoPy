def teste():
    material_escolar = ["lapis", "caneta", "borracha", "caderno"]

    for x in material_escolar:
        print("Lista material escolar : {}" .format(x), end = '\n')

    print("Numero de elementos na lista: {}" .format(len(material_escolar)))

    for y in range(0, len(material_escolar)):
        print("Numero de elementos na posicao {} sao: {}" .format(y, len(material_escolar[y])))


material_escolar = ["lapis", "caneta", "borracha", "caderno"]

def maior_elemento_lista(lista):
    maior = 0
    
    for x in range(0, len(lista)):

        tam_elemento = len(lista[x])
        if(tam_elemento > maior):
            maior = tam_elemento
            posicao_elemento = x

    lista_a = []
    lista_a.append(posicao_elemento)
    lista_a.append(maior)

    #return (maior, posicao_elemento)
    return(lista_a)

#Temos como retorno uma lista
a = maior_elemento_lista(material_escolar)

print("O elemento {} eh o elemento com mais caractere: {}" .format(material_escolar[a[0]], a[1]))

#Retorna a posicao do elemento na lista
print(material_escolar.index("lapis"))    

print(material_escolar[2].count("h")) #Faz a busca na posição 2(borracha). Resp 1
print(material_escolar.count("h")) #Faz a busca na lista. Resp 0

