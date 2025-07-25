import os
import pickle

from service import Service as BaseService


class Service(BaseService):

    def use_data(self):
        print("Using fake data")

        if not os.path.exists("data.pickle"):
            data = super().use_data()
            with open('data.pickle', 'wb') as handle:
                pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

        with open('data.pickle', 'rb') as handle:
            data = pickle.load(handle)

        return data
