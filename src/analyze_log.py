from os.path import exists
import csv
import sys

'''
    - Qual o prato mais pedido por 'maria'?

    - Quantas vezes 'arnaldo' pediu 'hamburguer'?

    - Quais pratos 'joao' nunca pediu?

    - Quais dias 'joao' nunca foi à lanchonete?
'''

def open_csv(path_to_file):
    print(path_to_file)
    if ".csv" not in path_to_file:
        raise ValueError("Arquivo inválido")

    if not exists(path_to_file):
        print(f"Arquivo {path_to_file} não encontrado", file=sys.stderr)
        return None
    
    with open(path_to_file, mode="r") as file:
        file_infos = list(csv.reader(file))
        return file_infos


def analyze_log(path_to_file):
    '''
        filtrar informaçoes

        criar arquivo > result_file = 'data/mkt_campaign.txt'

        salvar dados filtrados em csv
    '''
    open_csv(path_to_file)
