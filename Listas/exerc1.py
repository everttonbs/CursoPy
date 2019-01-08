
'''
a = (input('Teste 1 '))
print(type(a))
print('O numero x 4 e: {} '.format(a))
print(f'O numero x 4 e: {(a.upper())} ')

'''

lista_num = [1, 1, 3 , 5, 7, 9]


def maior_numeros(lista):
    #qualquer numero da lista será maior que zero e se tornará o maior
    maior = 0

    for x in lista:
        if(x > maior):
            maior = x

    return (maior)

def menor_numeros(lista):
    #Precisamos definir que o maior numerod a lista será 100, com isso
    #qualquer numero será menor que cem e  se tornará o menor
    menor = 100

    for y in lista:
        if(y < menor):
            menor = y

    return (menor)

def soma_numeros(lista):
    soma = 0

    for z in lista:
        soma = soma + z

    return (soma)

def frequencia_numeros(lista, valor):

    contador = 0

    for x in range(0 , len(lista)):
        if(lista[x] == valor):
            contador += 1

    return (contador)


def media_numeros(lista):

    soma = 0

    for y in lista:
        soma = soma + y

    #Podemos usar a função soma para retornar o valor da soma 
    # soma = soma_numeros(lista)

    media = soma / len(lista)
    
    return(media)



    
maior = maior_numeros(lista_num)
menor = menor_numeros(lista_num)
soma =  soma_numeros(lista_num)
contador = frequencia_numeros(lista_num, 1)
media = media_numeros(lista_num)


print(f"Maior numero da lista eh: {maior}")
#print(max(lista_num))
print(f"Menor numero da lista eh: {menor}")
#print(min(lista_num))
print(f"Soma dos numeros da lista: {soma}")
#print(sum(lista_num))
print("O numero aparece: {}" .format(contador))
print("A media dos numeros da lista: {}" .format(media))
#print(sorted(lista_num))

