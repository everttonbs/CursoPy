def mdc(num1, num2):

    resto = num1 % num2

    if(resto == 0):
        return num2

    else:
        return mdc(num2, resto)


num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o primeiro numero: "))


valor = mdc(num1, num2)
print(f'O MDC entre {num1} e {num2} é igual {valor}')
