
"""
Após 12 meses de aplicação a juros compostos de 2% ao mês, estou com
1.902,36. Qual foi o montante inicial?

Valor no presente = Valor no futuro / (1 + i)^n

"""

Vf = 1902.36
i = 0.02
n = 12

Vp = Vf / (1 + i)**n

#Usando diferentes formas do print
print("Valor do montante M = %.2f" %(Vp))
print("Valor do montante M =", Vp)
print("Valor do montante M = {:.2f}" .format(Vp))
print(f"Valor do montante M = {Vp :.2f}")