import random

def verificar_ganhador(num_sorteados, apostas):

    maior = 0
    
    for x in range(len(apostas)):
        cont = 0
        for y in range(len(numeros_sorteados)):
            if(apostas[x][y] == numeros_sorteados[y]):
                print("Ok")
                cont+= 1
    
    if(cont >= maior):
        maior = cont
        ganhador =  apostas[x][0]
        print(ganhador)




numeros_sorteados =[]

while(len(numeros_sorteados) != 6):
    a = random.randint(1, 10)
    numeros_sorteados.append(a)

print(numeros_sorteados)

apostas = []

lista_prov = ["Anna", 1, 2 , 3, 4, 6, 7]
apostas.append(lista_prov)
cond_parada = 1

while(cond_parada):
    
    cond_parada = int(input("1 - Nova aposta: \n0 - Sair\n"))

    if(cond_parada == 1):
        lista_apostador = []

        nome = input("Nome do apostador: ")
        lista_apostador.append(nome)

        while(len(lista_apostador)!= 7):
            num = int(input("Digite um numero:"))
            lista_apostador.append(num)

        apostas.append(lista_apostador)
    
    else:
        cond_parada = 0

verificar_ganhador(numeros_sorteados, apostas)
print("Numeros sorteados : {}" .format(numeros_sorteados))
#print(lista_apostador)
print(apostas)

