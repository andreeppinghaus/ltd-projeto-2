import csv
from io import StringIO
import numpy as np
import pandas as pd

# while inotifywait -e close_write myfile.py; do ./myfile.py; done

def replace_names(name):
    array = {
    "C/AÇ": "COM AÇUCAR",
    "PICADO": "PICADO",
    "PICADA": "PICADA",
    "EM" : "EM",
    "COL" : "COLHER",
    "S": "SOPA",
    "CALDA" : "CALDA",
    "CO": "CONCHA",
    "COL A": "COLHER DE ARROZ",
    "A": "ARROZ",
    "COL CAFÉ": "COLHER DE CAFÉ",
    "COL CHÁ": "COLHER DE CHÁ",
    "COL S": "COLHER DE SOPA",
    "COLS": "COLHER DE SOPA",
    "COLSR": "COLHER DE SOPA RASA",
    "COL SOBREMESA": "CONCHA",
    "CHÁ":"CHÁ",
    "CH.":"CHEIA",
    "PAU":"PAU",
    "COLPAUPR": "COLHER DE PAU PEQUENA RASA",
    "ESC": "ESCUMADEIRA",
    "ESCM": "ESCUMADEIRA MÉDIA",
    "ESCMR": "ESCUMADEIRA MÉDIA RASA",
    "FOLHA": "FOLHA",
    "FT": "FATIA",
    "FTM": "FATIA MÉDIA",
    "FTP": "FATIA PEQUENA",
    "INDUSTR": "INDUSTRIAL",
    "PED": "PEDAÇO",
    "PTF": "PRATO FUNDO",
    "PTR": "PRATO RASO",
    "PT SOB": "PRATO SOBREMESA",
    "PT": "PRATO",
    "PIRES":"PIRES",
    "COPO":"COPO",
    "SOB":"SOBREMESA",
    "RAMO":"RAMO",
    "UND": "UNIDADE",
    "X": "XÍCARA",
    "D": "DUPLO",
    "DOSE":"DOSE",
    "G": "GRANDE",
    "GG": "MUITO GRANDE",
    "M": "MÉDIO",
    "P": "PEQUENO",
    "CH": "CHEIO",
    "N": "NIVELADO",
    "R": "RASO",
    "GQ": "GRANDE QUANTIDADE",
    "MQ": "MÉDIA QUANTIDADE",
    "PQ": "PEQUENA QUANTIDADE",
    "GARFADA": "GARFADA",
    "g": "GRAMA",
    "mg": "Miligrama",
    "mL": "Mililitro",
    # "": "Micrograma",
    "mg": "Miligrama",
    "mg": "Miligrama",
    "mg": "Miligrama",
    "FPICADO": "FUNDO PICADO",
    "ITR": "PRATO RASO",
    "FTG": "FATIA GRANDE",
    "UNDP": "UNIDADE PEQUENA",
    "UNDM": "UNIDADE MÉDIA",
    "CAFÉ": "CAFÉ",
    "COMERCIAL": "COMERCIAL",
    "CAIXA": "CAIXA",
    "PACOTE": "PACOTE",
    "CANUDO": "CANUDO",
    "PUNHADO":"PUNHADO",
    "1/2": "1/2",
    "LATA":"LATA",
    "PRETA":"PRETA",
    "VERDE":"VERDE",
    "PORÇÃO":"PORÇÃO",
    "DESFIADO":"DESFIADO",
    "MCDONALD'S":"MCDONALD'S",
    "RODELA":"RODELA",
    "RALADA":"RALADA",
    "CXA":"CAIXA", 
    "BOLINHA/PALITO": "BOLINHA/PALITO",
    "ROSCA":"ROSCA",
    "BOLINHA":"BOLINHA",
    "F":"FUNDO",
    "GARRAFA":"GARRAFA",
    "TULIPA":"TULIPA",
    "1/2":"MEIO",
    "COZIDO":"COZIDO",
    "COZIDA":"COZIDA",
    "SORVETE": "SORVETE",
    "EMBALAGEM": "EMBALAGEM",
    "COMERCIAL":"COMERCIAL",
    "TABLETE":"TABLETE",
    "BARRA": "BARRA",
    "PASTA":"PASTA",
    "CORTE":"CORTE",
    "BAGO":"BAGO",
    "PEGADOR":"PEGADOR",
    } 
#https://superuser.com/questions/181517/how-to-execute-a-command-whenever-a-file-changes
    list = name.split(' ')
    list_not_found= []
    for val in list:
        if val in array:
            print(array[val])
        else:
            print("Chave não encontrada:", val)
            list_not_found.append(val)
            # print(val)
    if (len(list_not_found) >0 ):
        print('-------------------------------------')
        print('                            Produtos nao encontrados')
        print("                            ",list_not_found)
        print('--------------------------------------')

df = pd.read_csv('tabela_formatada_python.csv', on_bad_lines='skip')
# df2 = pd.read_csv('tabela_formatada_python.csv')

#765 
stop=2600

for indice in range(len(df)):
    # get line 
    row = df.iloc[indice].name

    #convert to array
    array = row[0].split(' ')

    # join all array element minus last 
    homemade_measure =  " ".join(map(str, array[:-1]))
    
    # get last array element
    grama_total = array[-1]

    print(f"medida = {homemade_measure} - gramas={grama_total}")
    replace_names(homemade_measure)
    if (stop==indice):
        break
    # print(f"medida = {new_name} - gramas={grama_total}")

