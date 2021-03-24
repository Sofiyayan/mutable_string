from collections.abc import MutableSequence


class MutableString(MutableSequence):
    def __init__(self, string: str):
        self.string = string

    def __getitem__(self, item):
        return self.string[item]

    def __setitem__(self, key, value):
        self.string = "".join(
            [self.string[:key], str(value), self.string[key + len(value):]]
        )

    def __str__(self):
        return self.string

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        for character in self.string:
            yield character

    def __repr__(self):
        return f"Mutable String type: {self.string}"

    def __add__(self, other):
        return "".join([self.string, str(other)])


    def __delitem__(self, key):
        value = self.string[key]
        self.string = "".join([self.string[:key], self.string[key + len(value):]])
        return self.string

    def title(self):
        return self.string.title()

    def capitalize(self):
        return self.string.upper()

    def center(self, width, fill=None):
        if fill is None:
            fill = " "
        return "{:{fill}^{width}}".format(self.string, fill=fill, width=width)

    def upper(self):
        return self.string.upper()

    def lower(self):
        return self.string.lower()

    def startswith(self, string, start=0, end=None):
        return self.string.startswith(string, start, end)

    def endswith(self, string, start=None, end=None):
        return self.string.endswith(string, start, end)

    def find(self, string, start=None, end=None):
        return self.string.find(string, start, end)

    def rfind(self, string, start=None, end=None):
        return self.string.rfind(string, start, end)

    def index(self, string, start=None, end=None):
        return self.string.index(string, start, end)

    def rindex(self, string, start=None, end=None):
        return self.string.rindex(string, start, end)

    def split(self, symbol):
        return self.string.split(symbol)

    def replace(self, old, new):
        return self.string.replace(old, new)

    def rreplace(self, old, new):
        return self.string.replace(old, new)

    def isdigit(self):
        return self.string.isdigit()

    def isalpha(self):
        return self.string.isalpha()

    def isalnum(self):
        return self.string.isalnum()

    def islower(self):
        return self.string.islower()

    def isupper(self):
        return self.string.isupper()

    def isspace(self):
        return self.string.isspace()

    def istitle(self):
        return self.string.istitle()

    @staticmethod
    def join(array):
        list_1 = [str(item) for item in array]
        return "".join(list_1)

    def format(self, *args, **kwargs):
        return self.string.format(*args, **kwargs)

    def ord(self):
        return ord(self.string)

    @staticmethod
    def chr(d):
        return chr(d)

    def count(self, string, start=None, end=None):
        return self.string.count(string, start, end)

    def lstrip(self, c=None):
        return self.string.lstrip(c)

    def rstrip(self, c=None):
        return self.string.rstrip(c)

    def strip(self, c=None):
        return self.string.strip(c)

    def insert(self, index: int, value) -> None:
        self.string = "".join([self.string[:index], str(value), self.string[index:]])


if __name__ == "__main__":
    pass
