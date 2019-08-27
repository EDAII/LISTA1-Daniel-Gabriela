import random
import time
import matplotlib.pyplot as plt
from functools import reduce
# INFO: 
## Todos os valores ordenados
## Sem repetição

MAX_REGISTRY = 10000

# TODO Colocar instalação do matplotlib no readme e requirements.txt

def averageVector(values):
    return reduce(lambda a, b: a + b, values) / len(values)

# GERAR NÚMEROS ALEATÓRIOS EXCLUSIVOS DENTRO DE UM INTERVALO
def generateRandomUniqueNumbers(start, end, quantity):
    numbers = random.sample(range(start, end), quantity)
    numbers.sort()
    return numbers

# BUSCA SEQUENCIAL COM SENTINELA [O(n)] (Está inserindo a sentinela na lista passada por parametro)
def sequentialSearchSentinel(key, values):
    init = time.time()
    i = 0
    values.append(key)
    pos = len(values) - 1
    while (values[i] != key):
        i += 1
    if i == (len(values) -1):
        return -1
    return time.time() - init

# BUSCA SEQUENCIAL SEM SENTINELA [O(n)]
def sequentialSearch(key, values):
    init = time.time()
    for i in values:
        if (key == i):
            return time.time() - init
    return -1

# BUSCA BINÁRIA (COM VETOR) [O(log n)]
def binarySearch(key, values):
    init = time.time()
    start = 0
    end = len(values) - 1
    while(start <= end):
        half = start + (end - start)//2
        if(values[half] == key):
            return time.time() - init
        elif(values[half] < key):
            start = half + 1
        else:
            end = half - 1
    return -1

# BUSCA POR INTERPOLAÇÃO [O(log(log n))]
def interpolationSearch(key, values):
    init = time.time()
    lower = 0
    upper = len(values) - 1

    while lower <= upper and key >= values[lower] and key <= values[upper]:
        if lower == upper:
            if values[lower] == key:
                return time.time() - init
            return -1

        position = lower + int((upper - lower) * ((key - values[lower]) / (values[upper] - values[lower])))

        if values[position] == key:
            return time.time() - init

        if values[position] < key:
            lower = position + 1
        else:
            upper = position - 1

    return -1

# TODO BUSCA INDEXADA


def getTimeResults(values):
    timeResults = {'Sequential Search': [], 'Sequential Sentinel Search': [], 'Binary Search': [], 'Interpolation Search': []}
    registersQtt = []

    for i in range(10, MAX_REGISTRY, 100):
        vector = values[:i]
        registersQtt.append(i)

        auxDict = {'Sequential Search': [], 'Sequential Sentinel Search': [], 'Binary Search': [], 'Interpolation Search': []}
        
        for n in range(10):
            element = random.choice(vector)

            auxDict['Sequential Search'].append(sequentialSearch(element, vector) * 1000000)
            auxDict['Sequential Sentinel Search'].append(sequentialSearchSentinel(element, vector.copy()) * 1000000)
            auxDict['Binary Search'].append(binarySearch(element, vector) * 1000000)
            auxDict['Interpolation Search'].append(interpolationSearch(element, vector) * 1000000)

        for key, value in auxDict.items():
            timeResults[key].append(averageVector(value))

    return timeResults, registersQtt


def plotLineChart(registersQuantity, timeDict):
    plt.figure('Search methods')
    plt.title("Search methods")

    for key, value in timeDict.items():
        plt.plot(registersQuantity, value, label=key)

    plt.xlabel('Quantidade de Registros')
    plt.ylabel('Tempo (µs)')

    plt.legend()
    plt.show()

#INICIALIZA OS DICIONÁRIOS QUE CONTERÃO O Nº DE REGISTROS : TEMPO
def main():

    timeResults, registersQtt = getTimeResults(generateRandomUniqueNumbers(0, 99999, MAX_REGISTRY))
    
    plotLineChart(registersQtt, timeResults)

if __name__ == '__main__':
    main()