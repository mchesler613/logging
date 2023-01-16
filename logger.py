import logging


class Logger:
    """
    This class is a representation of a logging object
    with a custom file handler for logging information-only custom messages
    using the Python logging library
    """

    def __init__(self, name):
        self.name = name

        # retrieve the parent logger
        self.logger = logging.getLogger(f"{__name__}.{name}")

        # set log level to INFO only
        self.logger.setLevel(logging.INFO)

        # create a separate file handler for this instance with overwrite mode
        file_handler = logging.FileHandler(f"logs/{name}.log", mode="w")

        # create a log entry formatter to display only the message
        formatter = logging.Formatter("%(message)s")

        # link formatter to file handler
        file_handler.setFormatter(formatter)

        # add file handler to root logger
        self.logger.addHandler(file_handler)

    def __str__(self):
        return f"Logger.{self.name}"
