#soma 2 numeros
def soma_2(a, b):
    return a+ b
#soma 3 numeros
def soma_3(a, b, c):
    return a + b + c
#soma n numeros 
def soma_n(*numeros):
    #*numeros é uma tupla
    soma = 0
    for x in numeros:
        soma = soma + x
    
    return soma

def soma_n2(num):
    soma = 0 
    for x in num:
        soma = soma + x

    return soma

if __name__ == '__main__':
    print(soma_2(1, 2))
    print(soma_3(1, 2, 3))
    print(soma_n(1, 1, 1, 1, 1, 1, 1))#empacota todos os numeros em uma tupla

    tupla_nums = (1, 2, 3, 4)
    print(soma_n(*tupla_nums))#desempacota os numeros

    lista_nums = [1, 2, 3, 4]
    print(soma_n(*tupla_nums))#desempacota os numeros

    print(soma_n2(lista_nums))
    print(soma_n2(tupla_nums))
