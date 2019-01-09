def decifrar(lista):
    lista_letras = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decifrado = []
    for ch in range(-5, 6):
        decifrado.clear()
        for key in lista:
            value = int(key)
            decifrado.append(lista_letras[value-ch])
        print(f'{ch}: [{decifrado}]')


def cifrar(frase, chave):
    lista_letras = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cifrado = []
    for caractere in frase:
        pos = lista_letras.index(caractere)
        cifrado.append(pos + chave)
    print(cifrado)


option = int(input('0 (cifra) / 1 (decifra): '))
if option:
    fr = input('Frase a decifrar: ')
    decifrar(fr.split(','))
else:
    fr = input('Frase a cifrar: ')
    chave = int(input('Chave (-5 a 5): '))
    cifrar(fr, chave)
