'''
14.	Exercício: Leia um arquivo .csv que contenha duas colunas: "Produto" e "Preço". Exiba os produtos cujo preço seja maior que 50.
'''

import pandas as pd

df = pd.read_csv('exercicio14.csv')
print(df[df['Preço'] > 50])
 


