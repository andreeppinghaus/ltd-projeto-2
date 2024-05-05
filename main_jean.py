# Ler arquivos csv e txt

import pandas as pd

arquivo_csv = ('documentos/Taco_4a_edicao_2011.csv')

arquivo_txt = ('documentos/tabela_medidas_caseiras.txt')

arquivo_csv_lido = pd.read_csv(arquivo_csv)

with open(arquivo_txt, 'r', encoding='utf-8') as arquivo_txt_saida:
  arquivo_txt_todas_linhas = arquivo_txt_saida.readlines()

#Pegar dados da primeira coluna do arquivo txt

  alimento_array = []

  for linha in arquivo_txt_todas_linhas:
    quantidade_linha = 0

    posicao_virgula = linha.find(',')
    dados_ate_virgula = linha[0:posicao_virgula]
    if linha.strip():
      alimento_array.append(dados_ate_virgula)
      quantidade_linha += 1
      print("A linha contém algum dado.")
    else:
      print("A linha está vazia.")
  
# Criar um novo arquivo csv com uma nova coluna na posição 3 e colocar esses dados lá


# Transformar esse arquivo csv em json