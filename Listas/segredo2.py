def decifrar(num):
    lista_letras = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for x in range(0, len(lista_letras)):
        if(num == x):
            return lista_letras[x]


def cifrar(letra):
    lista_letras = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for x in range(0, len(lista_letras)):
        if(letra == lista_letras[x]):
            return x


def inicio():
    nome_usuario = input("Digite seu nome:")
    print("Bem vindo ao Cifrador, {}!" .format(nome_usuario))
    print("1 - Cifrar texto")
    print("2 - Decifrar texto")
    print("0 - Sair")
    escolha_usuario = int(input())
    palavra_decifrada = []
    palavra_cifrada = []
    if(escolha_usuario == 1):
        palavra = input("Digite o texto:")
        for x in range(0, len(palavra)):
            palavra_cifrada.append(cifrar(palavra[x]))
        # print(palavra[0])
        print("Palavra cifrada {}". format(palavra_cifrada))

    elif(escolha_usuario == 2):
        tamanho = int(input("Digite quantos numeros existem:"))
        #numeros = []
        for x in range(tamanho):
            num = int(input("Digite o numero: "))
            palavra_decifrada.append(decifrar(num))
        print(palavra_decifrada)

    else:
        return 0
    return 1


a = True
while(a == True):
    a = inicio()
