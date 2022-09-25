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
        bigger = 0
        result = ''

        for index in data:
            if customer == data[index][0] and data[index][1] not in count:
                count[data[index][1]] = 1
            elif customer == data[index][0] and data[index][1] in count:
                count[data[index][1]] += 1

        for item in count:
            if count[item] > bigger:
                bigger = count[item]
                result = item

        return result

    def get_never_ordered_per_customer(self, customer):
        data = self.data
        all_plates = []
        eaten = []
        result = set()

        for index in data:
            if data[index][1] not in all_plates:
                all_plates.append(data[index][1])

            if customer == data[index][0] and data[index][1] not in eaten:
                eaten.append(data[index][1])

        for plate in all_plates:
            if plate not in eaten:
                result.add(plate)

        return result

    def get_days_never_visited_per_customer(self, customer):
        data = self.data
        all_days = []
        visited = []
        result = set()

        for index in data:
            if data[index][2] not in all_days:
                all_days.append(data[index][2])

            if customer == data[index][0] and data[index][2] not in visited:
                visited.append(data[index][2])

        for plate in all_days:
            if plate not in visited:
                result.add(plate)

        return result

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
