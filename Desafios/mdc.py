
def mdc(num1, num2):
    
    resto = num1 % num2
    print(resto)
    
    if(resto == 0):        
        print('ok')
        print(f"Num2 : {num2}")
        return num2
             

    elif(resto == 1):
        return (1)
    
    else:
        mdc(num2, resto)

    
    print("Aqui")

#valor = mdc(23732, 180)
valor = mdc(30, 12)
print(f'MDC : {valor}')
print(valor)
