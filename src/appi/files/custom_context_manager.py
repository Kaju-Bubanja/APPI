from datetime import datetime
import traceback


class CustomLogger:
    def __init__(self, filename, mode="w"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type:
            traceback.print_exception(exc_type, exc_value, tb)
        self.file.close()

    def write(self, content):
        now = datetime.now()
        self.file.write(f"{now}: " + content + "\n")


with CustomLogger("custom_logger.txt") as file:
    file.write("First line")
    file.write("Hallo world")
