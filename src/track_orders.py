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
        count = {}

        for index in data:
            if customer == data[index][0] and data[index][1] not in count:
                count[data[index][1]] = 1
            elif customer == data[index][0] and data[index][1] in count:
                count[data[index][1]] += 1

        result = max(count, key=count.get)
        return result

    def get_never_ordered_per_customer(self, customer):
        data = self.data
        all_plates = set()
        eaten = set()

        for index in data:
            if data[index][1] not in all_plates:
                all_plates.add(data[index][1])

            if customer == data[index][0] and data[index][1] not in eaten:
                eaten.add(data[index][1])

        never_eaten = all_plates.difference(eaten)
        return never_eaten

    def get_days_never_visited_per_customer(self, customer):
        data = self.data
        all_days = set()
        visited = set()

        for index in data:
            if data[index][2] not in all_days:
                all_days.add(data[index][2])

            if customer == data[index][0] and data[index][2] not in visited:
                visited.add(data[index][2])

        never_visited = all_days.difference(visited)
        return never_visited

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
