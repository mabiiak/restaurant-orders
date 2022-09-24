from os.path import exists
import csv
import sys


file_path = '/home/mabi/Documentos/Trybe/4-CS/sd-016-a-restaurant-orders/data/orders_1.csv'

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


def count_days(data_client):
    count_days_orders = {}

    for order in data_client:
        if order[2] not in count_days_orders:
            count_days_orders[order[2]] = 1

    return count_days_orders


def about_restaurant(data, search):
    all_plates = []
    open_days = []

    if search == "plates":
        for orders in enumerate(data):
            if not orders[1][1] in all_plates:
                all_plates.append(orders[1][1])
        return all_plates

    if search == "days":
        for orders in enumerate(data):
            if not orders[1][2] in open_days:
                open_days.append(orders[1][2])

        return open_days


def analyze_log(path_to_file):
    '''
        filtrar informaçoes

        criar arquivo > result_file = 'data/mkt_campaign.txt'

        salvar dados filtrados em csv
    '''
    data = open_csv(path_to_file)

    data_client_maria = filter_person(data, 'maria')
    maria_orders = count_orders(data_client_maria)
    maria_larger_order = ''
    length = 0

    for index in enumerate(maria_orders):
        if maria_orders[index[1]] > length:
            length = maria_orders[index[1]]
            maria_larger_order = index[1]

    print(maria_larger_order)

    # -----------------------------------------------------------

    data_client_arnaldo = filter_person(data, 'arnaldo')
    arnaldo_orders = count_orders(data_client_arnaldo)
    arnaldo_count_orders = 0

    for index in enumerate(arnaldo_orders):
        if index[1] == 'hamburguer':
            arnaldo_count_orders = arnaldo_orders[index[1]]
    
    print(arnaldo_count_orders)

    # -----------------------------------------------------------

    data_client_joao = filter_person(data, 'joao')
    joao_orders = count_orders(data_client_joao)
    joao_days_orders = count_days(data_client_joao)
    plates = about_restaurant(data, 'plates')
    days = about_restaurant(data, "days")

    did_not_prove = []
    did_not_attend = []

    for index in enumerate(plates):    
        if index[1] not in joao_orders:
            did_not_prove.append(index[1])

    for index in enumerate(days):
        if index[1] not in joao_days_orders:
            did_not_attend.append(index[1])

    print(set(did_not_prove))
    print(set(did_not_attend))


analyze_log(file_path)
