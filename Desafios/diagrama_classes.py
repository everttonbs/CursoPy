from datetime import datetime
class Pessoas:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return (f'Nome : {self.nome}\nIdade: {self.idade}')


    def adulto(self):

        if self.idade >= 18:
            return True
        else:
            return False


class Vendedor(Pessoas):
    def __init__(self, nome, idade, salario):
        #super().__init__(nome, idade)
        Pessoas.__init__(self, nome, idade)   

        self.salario = salario


class Cliente(Pessoas):
    def __init__(self, nome, idade, compras):
        super().__init__(nome, idade)
        #Pessoas.__init__(self, nome, idade)

        self.compras = compras

    def registrar_compras(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        return datetime.now()

    def total_compras(self):
        total = 0
        for x in self.compras:
            total = total + x

    
class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor
    
vend1 = Vendedor("Anna", 22, 2000.00)
# print(vend1.nome)
# print(vend1.idade)
# print(vend1.salario)

lista_compras = ["calça", "bermuda"]
cliente1 = Cliente("Mari", 20, lista_compras)

print(cliente1.compras)

