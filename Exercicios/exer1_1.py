
'''
1 - Calcule o montante resultante da aplicação de R$100.000,00 à taxa de
10,5% a.a., em juros simples, durante 145 dias.

M = P ∙ (1 + (i ∙ n))

onde P = principal (capital), i= taxa de juros, n = número de períodos

'''
P = 100000.0
i = 0.105 / 365
n = 145

#Juros por dia = 0.029
#print (i)

M = P * (1 + (i * n))

#Usando diferentes formas do print
print("Valor do montante M = %.2f" %(M))
print("Valor do montante M =", M)
print("Valor do montante M = {:.2f}" .format(M))
print(f"Valor do montante M = {M :.2f}")


