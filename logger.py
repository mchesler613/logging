import logging


class Logger:
    def __init__(self, name):
        self.name = name
        logging.basicConfig(
            filename=f"{name}.log",
            level=logging.INFO,     # only log this type
            filemode="w",           # overwrite log file each time
            format="%(message)s",
        )
        self.logger = logging.getLogger(name)
