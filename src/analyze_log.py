from os.path import exists
import csv
import sys


'''
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


def count_orders(data_client):
    count_orders = {}

    for order in data_client:
        if order[1] not in count_orders:
            count_orders[order[1]] = 1
        elif order[1] in count_orders:
            count_orders[order[1]] += 1
    
    return count_orders


def analyze_log(path_to_file):
    '''
        filtrar informaçoes

        criar arquivo > result_file = 'data/mkt_campaign.txt'

        salvar dados filtrados em csv
    '''
    data = open_csv(path_to_file)

    data_client = filter_person(data, 'maria')
    maria_orders = count_orders(data_client)
    maria_larger_order = ''

    for index in enumerate(maria_orders):
        length = 0
        if maria_orders[index[1]] > length:
            length = maria_orders[index[1]]
            maria_larger_order = index[1]

    # print(maria_larger_order)

    data_client = filter_person(data, 'arnaldo')
    arnaldo_orders = count_orders(data_client)
    arnaldo_count_orders = 0

    for index in enumerate(arnaldo_orders):
        if index[1] == 'hamburguer':
            arnaldo_count_orders = arnaldo_orders[index[1]]
    
    # print(arnaldo_count_orders)
