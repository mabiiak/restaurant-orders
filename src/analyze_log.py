from os.path import exists
import csv
import sys


'''
    - Quantas vezes 'arnaldo' pediu 'hamburguer'?

    - Quais pratos 'joao' nunca pediu?

    - Quais dias 'joao' nunca foi à lanchonete?
'''

def open_csv(path_to_file):
    if ".csv" not in path_to_file:
        raise ValueError("Arquivo inválido")

    if not exists(path_to_file):
        print(f"Arquivo {path_to_file} não encontrado", file=sys.stderr)
        return None
    
    with open(path_to_file, mode="r") as file:
        file_infos = list(csv.reader(file))
        return file_infos


def filter_person(data, name):
    data_person = []

    for index in data:
        if index[0] == name:
            data_person.append(index)

    return data_person


def filter_larger_order(data_client):
    count_orders = {}
    tamanho = 0
    most_requested = ''

    for order in data_client:
        if order[1] not in count_orders:
            count_orders[order[1]] = 1
        elif order[1] in count_orders:
            count_orders[order[1]] += 1

    for index in enumerate(count_orders):
        if count_orders[index[1]] > tamanho:
            tamanho = count_orders[index[1]]
            most_requested = index[1]
    
    return most_requested


def analyze_log(path_to_file):
    '''
        filtrar informaçoes

        criar arquivo > result_file = 'data/mkt_campaign.txt'

        salvar dados filtrados em csv
    '''
    data = open_csv(path_to_file)

    data_client = filter_person(data, 'maria')
    maria_larger_order = filter_larger_order(data_client)
