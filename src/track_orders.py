class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.__length = 0
        self.data = {}

    def __len__(self):
        self.__length = len(self.data)
        return self.__length

    def add_new_order(self, customer, order, day):
        id = len(self.data) + 1
        self.data[id] = (customer, order, day)

    def get_most_ordered_dish_per_customer(self, customer):
        data = self.data
        count_itens = {}
        bigger = 0
        result = ''
    
        for index in data:
            if customer == data[index][0] and data[index][1] not in count_itens:
                count_itens[data[index][1]] = 1
            elif customer == data[index][0] and data[index][1] in count_itens:
                count_itens[data[index][1]] += 1

        for item in count_itens:
            if count_itens[item] > bigger:
                bigger = count_itens[item]
                result = item

        return result


    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
