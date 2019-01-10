import random

num_aleatorio = random.randint(1, 100)

lista_ten = [0, 101]

while(True):
    ten_usuario = int(input("Digite um numero: "))
    lista_ten.append(ten_usuario)
    lista_ten.sort()    
    a = lista_ten.index(ten_usuario)
    #print(f"Index {a}")

    if(ten_usuario > num_aleatorio):
        print("Tente um numero menor")
        print(f'[ {lista_ten[a - 1]} , {lista_ten[a]} ]')

    elif(ten_usuario < num_aleatorio):
        print("Tente um numero maior")
        print(f'[ {lista_ten[a]} , {lista_ten[a + 1]} ]')

    else:
        print("Parabéns!! Você acertou.")
        break

    #lista_ord = lista_ten.sort()
    #print(f"Lista de tentativas: {lista_ten}")

    #print(f'Lista ordenada: {lista_ten}')
