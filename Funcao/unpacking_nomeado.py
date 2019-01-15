## **kwargs

def resultado(primeiro, segundo, terceiro):
    print(f"1) {primeiro}")
    print(f"2) {segundo}")
    print(f"3) {terceiro}")

def resultado_valor(dic):
    print(f" {dic['primeiro']}")
    

def resultado_normal(dic):
    for chave, valor in dic.items():
        print(f'{chave} : {valor}')

if __name__ == '__main__':

    classificados = {'primeiro' : 'Anna',
                     'segundo'  : 'Jose',
                     'terceiro' : 'Maria'}

    resultado(**classificados)
    print(10 * '*')
    resultado_normal(classificados)
    print(10 * '*')
    resultado_valor(classificados)

