
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'({self.nome}, idade {self.idade})'

    def Adulto(self):
        return True if self.idade >= 18 else False

class Vendedor(Pessoa): 
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        #Pessoa.__init__(self, nome, idade)
        self.salario = salario

class Compra():
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor

class Cliente(Pessoa):
    def registrar_compra(self, compra):
        self.compras.append(compra)

    def __init__(self, nome, idade, compras):
        super().__init__(nome, idade)
        self.compras = []
        self.registrar_compra(compras)

    def get_data_ultima_compra(self):
        return self.compras[-1].data
        
    def total_compras(self):
        total = 0
        for c in self.compras:
            total += c.valor            
        return total




if __name__ == "__main__":
    pessoa = Pessoa("LCCV", 50)
    pessoa2 = Pessoa('João',34)
    #print(pessoa)
    #print(pessoa.Adulto())

    vendedor = Vendedor(pessoa.nome, pessoa.idade,2000.00)
    #print(vendedor.salario)

    compra1 = Compra(vendedor, "10/01", 100.00)
    compra2 = Compra(vendedor, "15/01", 150.00)
    print(compra1.vendedor.nome)

    cliente = Cliente(pessoa2.nome,pessoa2.idade,compra1)
    cliente.registrar_compra(compra2)
    print(cliente.get_data_ultima_compra())
    print(cliente.total_compras())


