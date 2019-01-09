def cifrar(lista, key):
    texto_cifrado = []
    for x in range(len(lista)):
        texto_cifrado.append(ord(lista[x]) + 1)

    print(texto_cifrado)


def decifrar(lista):
    texto_decifrado = []

    for x in range(-5, 5):
        for y in range(len(lista)):
            a = int(lista[y])
            texto_decifrado.append(chr(a - x))

        print(texto_decifrado)
        texto_decifrado.clear()


entr = int(input("1 - Cifrar\n2- Decifrar"))
if(entr == 1):
    chave = input("Digite a chave")
    texto = input("Digite o texto")
    cifrar(texto, chave)

else:
    texto = input("numeros")
    decifrar(texto.split(","))
