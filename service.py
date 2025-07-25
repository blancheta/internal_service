from api import get_data


class Service:

    def use_data(self):
        data = get_data()
        return data

    def run(self):
        self.use_data()
