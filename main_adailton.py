import pandas as pd

def ler_csv(arquivo_csv):
    dados = pd.read_csv(arquivo_csv)

    print(dados)

ler_csv('C:\\Users\\adail\\OneDrive\\Área de Trabalho\\Pasta LTD - PROJETO\\ltd-projeto-2\\documentos\\Taco_4a_edicao_2011.csv')