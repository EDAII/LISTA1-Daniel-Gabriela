import matplotlib.pyplot as plt
import random
import time
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

# TODO BUSCA POR INTERPOLAÇÃO [O(log(log n))]

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
# https://marciobueno.com/arquivos/ensino/ed2/ED2_11_Pesquisa.pdf

#INICIALIZA OS DICIONÁRIOS QUE CONTERÃO O Nº DE REGISTROS : TEMPO
def main():
    registersQtt = []
    sequentialSearchTime = []
    sequentialSearchSentinelTime = []
    binarySearchTime = []
    interpolationSearchTime = []

    keys = generateRandomUniqueNumbers(1, 9999999, MAX_REGISTRY)

    for i in range(10, MAX_REGISTRY, 100):
        vector = keys[:i]
        registersQtt.append(i)

        auxVectorSequentialSearch = []
        auxVectorBinarySearch = []
        auxVectorSequentialSentinelSearch = []
        auxVectorInterpolationSearch = []
        
        for n in range(10):
            element = random.choice(vector)

            auxVectorSequentialSearch.append(sequentialSearch(element, vector) * 1000000)
            auxVectorSequentialSentinelSearch.append(sequentialSearchSentinel(element, vector.copy()) * 1000000)
            auxVectorBinarySearch.append(binarySearch(element, vector) * 1000000)
            auxVectorInterpolationSearch.append(interpolationSearch(element, vector) * 1000000)

        # SAIU DO FOR PEGA OS VETORES AUXILIARES CALCULA A MEDIA E APPEND NOS VETORES DE TEMPO
        # TODO no lugar de i+n deve ficar o tempo que demorou para cada método de busca encontrar a chave
        sequentialSearchTime.append(averageVector(auxVectorSequentialSearch))
        sequentialSearchSentinelTime.append(averageVector(auxVectorSequentialSentinelSearch))
        binarySearchTime.append(averageVector(auxVectorBinarySearch))
        interpolationSearchTime.append(averageVector(auxVectorInterpolationSearch))

    # PLOTANDO GRÁFICOS
    plt.figure('Search methods')
    plt.title("Search methods")

    plt.plot(registersQtt, sequentialSearchTime, label='Sequential Search')
    plt.plot(registersQtt, sequentialSearchSentinelTime, label='Sequential Sentinel Search')
    plt.plot(registersQtt, binarySearchTime, label='Binary Search')
    plt.plot(registersQtt, interpolationSearchTime, label='Interpolation Search')

    plt.xlabel('Quantidade de Registros')
    plt.ylabel('Tempo (µs)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()