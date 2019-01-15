# **kwargs

def resultado(**aprovados):
    for pos, nomes in aprovados.items():
        print(f" [{pos}] -> {nomes}")


if __name__ == "__main__":
    #Parâmentros nomeados
    resultado(primeiro = 'Anna', segundo = 'Jose', terceiro = 'Maria')
