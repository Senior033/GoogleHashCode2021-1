#! usr/bin/python3

class InputClass():
    def __init__(self, path):
        self.fd = open(path, "r")
        self.tab = self.fd.read().rstrip().split('\n')

    def __str__(self):
        return f

    def print(self):
        for x in self.tab:
            print(x)