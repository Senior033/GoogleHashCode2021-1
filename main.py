#! /usr/bin/python

from sys import stdin, argv, stderr, exit
from sources import badException, inputClass

def main(path):
    cityPlan = inputClass.InputClass(path)
    cityPlan.print()

if __name__ == "__main__":
    try:
        if len(argv) != 2:
            raise badException.BadException("No file was past on parameter")
        main(argv[1])
    except BaseException as error:
        stderr.write(str(type(error).__name__) + ": {}\n".format(error))
        exit(84)