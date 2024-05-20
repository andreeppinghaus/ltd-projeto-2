import pandas as pd

def ler_csv_e_salvar_json(arquivo_csv, arquivo_json):
    dados = pd.read_csv(arquivo_csv)

    dados_json = dados.to_json(orient='records')

    with open(arquivo_json, 'w') as json_saida:
        json_saida.write(dados_json)

    print(dados)

ler_csv_e_salvar_json(r'C:\Users\Jean\Documents\Jean\Programação\GIT-E-GITHUB\ltd-projeto-2\documentos\Taco_4a_edicao_2011.csv',r'C:\Users\Jean\Documents\Jean\Programação\GIT-E-GITHUB\ltd-projeto-2\documentos\Taco_4a_edicao_2011.jason')