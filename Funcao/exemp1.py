'''
Tipos de parâmetro:
    - Posicional
    - Nomeado

- *args - tupla
- **kwargs - dicionário

'''
lista_x = [1, 2, 3, 4]

lista = ''.join(f' {x} ' for x in lista_x )

print(type(lista))

print(lista)