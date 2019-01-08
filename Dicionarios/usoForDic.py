dic = {'Nome' : "Anna", 'idade' : '60'}
'''
#Pecorre as chaves do dicionario
for nomesDic in dic:
    print(f'Chave : {nomesDic}')
    

#Pecorre os valores do dicionario
for valorDic in dic.values():
    print(f'Valores : {valorDic}')


for nomesDic, valorDic in dic, dic.values():
    print(f'Chave : {nomesDic} -> Valor {valorDic}')
'''
for chave, valor in dic.keys(), dic.values():
    print(f'{chave} : {valor}')



