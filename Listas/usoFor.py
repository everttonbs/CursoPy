
palavra = "Huppermago"

for letra in palavra:
    print("Letra: {}" . format(letra), end = ' ')
    #print("Letra: {}" . format(letra))
    print();

#Mostra na tela as letras fora de ordem
for letra in set("Hello World!"):
    print (f'Letra -> {letra}')

listaNomes = ["Maria", "Jose"]

for nome in listaNomes:
    print("Nomes : {}" . format(nome))

#Acessando pelo indice
for i in range(0 , len(listaNomes)):
    print('Nomes : {}' .format(listaNomes[i]))

#Mostra na tela a posicao e os nomes
for posicao, nome in enumerate(listaNomes):
    print(f'{posicao + 1} - {nome}')

