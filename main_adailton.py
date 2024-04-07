import pandas as pd

def ler_csv_e_salvar_json(arquivo_csv, arquivo_json):
    dados = pd.read_csv(arquivo_csv)

    dados_json = dados.to_json(orient='records')

    with open(arquivo_json, 'w') as json_saida:
        json_saida.write(dados_json)

    print(dados)

ler_csv_e_salvar_json('C:\\Users\\adail\\OneDrive\\Área de Trabalho\\Pasta LTD - PROJETO\\ltd-projeto-2\\documentos\\Taco_4a_edicao_2011.csv','C:\\Users\\adail\\OneDrive\\Área de Trabalho\\Pasta LTD - PROJETO\\ltd-projeto-2\\documentos\\Taco_4a_edicao_2011.json')