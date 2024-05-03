import pandas as pd

# Ler arquivos csv e txt

arquivo_csv = ('ltd-projeto-2/documentos/Taco_4a_edicao_2011.csv')

arquivo_txt = ('ltd-projeto-2/documentos/tabela_medidas_caseiras.txt')

arquivo_csv_lido = pd.read_csv(arquivo_csv)

with open(arquivo_txt, 'r', encoding='utf-8') as arquivo_txt_saida:
  arquivo_txt_todas_linhas = arquivo_txt_saida.readlines()


  for linha in arquivo_txt_todas_linhas:
    posicao_virgula = linha.find(',')
    dados_ate_virgula = linha[0:posicao_virgula]
    print(dados_ate_virgula)

#Pegar dados da primeira coluna do arquivo txt
  
# Criar um novo arquivo csv com uma nova coluna na posição 3 e colocar esses dados lá


# Transformar esse arquivo csv em json