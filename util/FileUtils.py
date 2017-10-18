import os.path
from datetime import datetime

import sys

sys.path.insert(0, '')

def writeFile(fileName, content):
    file = open(fileName, "w")
    file.write(content)
    file.close()


def appendFile(fileName, content):
    existFile = os.path.exists(fileName)
    file = open(fileName, "a")
    if (existFile):
        file.write("\n")
    file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    file.write("\t")
    file.write(content)
    file.close()


def readFile(fileName):
    file = open(fileName, "r")
    return file.read()
