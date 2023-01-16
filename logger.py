import logging


class Logger:
    def __init__(self, name):
        self.name = name

        self.logger = logging.getLogger(f"{__name__}.{name}")
        self.logger.setLevel(logging.INFO)

        # create a separate file handler for each name
        file_handler = logging.FileHandler(f"logs/{name}.log", mode="w")

        # file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(message)s")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        print(f"{self}.__init__")
        print(self.logger)

    def __str__(self):
        return f"Logger.{self.name}"
