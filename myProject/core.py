
import numpy as np


def helloFunction():
    return "Hello World"


def returnTrueFunction():
    return True

class myClass(object):
    def __init__(self):
        self.array = np.array([0.0, 1.0, 2.0])

    def getArray(self):
        return self.array
