
"""
Calcule o montante de um capital de R$10.000,00, aplicado a juros
compostos, durante 1 ano, à taxa de 2,5% ao mês.

M = P ∙ (1 + i)^n

"""

P = 10000.0
i = 0.025
n = 12

M = P * (1 + i)**n

#Usando diferentes formas do print
print("Valor do montante M = %.2f" %(M))
print("Valor do montante M =", M)
print("Valor do montante M = {:.2f}" .format(M))
print(f"Valor do montante M = {M :.2f}")