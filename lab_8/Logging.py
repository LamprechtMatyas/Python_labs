
class Logger:
    level = 0
    printers = []

    def __init__(self, name):
        self.name = name

    def set_level(self, level):
        self.level = level

    def log(self, level, message):
        if level > self.level:
            for printer in self.printers:
                print(message, file=printer)

    def add_printer(self, printer):
        self.printers.append(printer)




