
produtos = {'cafe' : '2.7', 'leite':'3.0'}

def perfil_admin():
    
    escolha_admin = 100

    while(escolha_admin != 0):
        print("**** Perfil Adminstrador ****")
        print("1 - Cadastrar produto: ")
        print("2 - Editar produto: ")
        print("3 - Remover produto: ")
        print("4 - Buscar produto: ")
        print("0 - Sair: ")

        escolha_admin = int(input())

        if(escolha_admin == 1 ):
            cadastro_produto()

        elif(escolha_admin == 5):
            relatorio_produtos(produtos)


        else:
            return 0





def perfil_cliente():
    pass

def cadastro_produto():
    print("**** Cadastro de produtos ****")
    nome_produto = input("Nome do produto: ")
    preco_produto = float(input("Preço do produto: "))

    produtos[nome_produto] = preco_produto

    print(produtos)

def relatorio_produtos(dic_produtos):    

    for chave, valor in dic_produtos.items():
        print(f'{chave} : {valor}')
        


def editar_produto():
    pass

def remocao_produto():
    pass

def main():
    print("Bem vindo ao sistema do SuperPreço")
    print("1 - Administrador ")
    print("2 - Cliente ")
    print("0 - Sair  ")

    escolha_usuario = int(input())

    if(escolha_usuario == 1):
        perfil_admin()

    else:
        return 0

main()

print("End")


    