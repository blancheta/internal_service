import importlib

from config import DATA_LOADER

service_mod =  importlib.import_module(DATA_LOADER)


class Runner:

    def start_process(self):
        # Get class from module
        service_class = getattr(service_mod, "Service")
        service_instance = service_class()
        service_instance.run()


if __name__ == "__main__":

    runner = Runner()
    runner.start_process()