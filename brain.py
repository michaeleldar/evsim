import neurons


class Brain:
    constantNeuron = neurons.InputNeuron(neurons.InputNeuronType.CONSTANT.value)
    print(constantNeuron.returnType())
