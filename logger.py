import logging


class Logger:
    """
    This class is a representation of a logging object
    with a custom file handler for logging INFO-level custom messages
    using the Python logging library
    """

    def __init__(self, name: str) -> None:
        self.name = name

        # retrieve a child logger from the logging library
        self.logger = logging.getLogger(f"{__name__}.{name}")

        # set log level to INFO only
        self.logger.setLevel(logging.INFO)

        # create a file handler with overwrite mode
        file_handler = logging.FileHandler(f"logs/{name}.log", mode="w")

        # associate file handler to child logger
        self.logger.addHandler(file_handler)

    def __str__(self):
        return f"Logger.{self.name}"

    def log(self, message: str) -> None:
        """
        A convenient method for clients to use to log a raw message
        """
        self.logger.info(message)
