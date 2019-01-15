#Entram na função todos os parâmetros, tanto os posicionais como os nomeados
def todos_param(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == "__main__":
    todos_param('a', 'b', 'c', 'd')
    todos_param('a', 'b', nome = 'Anna')
    



