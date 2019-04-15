import sys


class IText(object):
    @staticmethod
    def name():
        pass

    @staticmethod
    def process(text: str):
        raise NotImplemented


class ToUpper(IText):

    @staticmethod
    def name():
        return "to_upper"

    @staticmethod
    def process(text: str):
        return text.upper()


class ToLower(IText):

    @staticmethod
    def name():
        return "to_lower"

    @staticmethod
    def process(text: str):
        return text.lower()


class Capitalize(IText):

    @staticmethod
    def name():
        return "capitalize"

    @staticmethod
    def process(text: str):
        return text.capitalize()



def _main():
    apply = sys.argv[1:]
    for text in sys.stdin:
        for item in apply:
            if item == ToLower.name():
                text = ToLower.process(text)
            elif item == ToUpper.name():
                text = ToUpper.process(text)
            elif item == Capitalize.name():
                text = Capitalize.process(text)
        print(text)


if __name__ == "__main__":
    _main()
