from enum import Enum


class InputNeuronType(Enum):
    CONSTANT = "constant"


class InputNeuron:
    def __init__(self, type):
        self.type = type

    def returnType(self):
        return self.type
