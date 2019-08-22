import matplotlib.pyplot as plt
import random
# INFO: 
## Todos os valores ordenados
## Sem repetição

# TODO Colocar instalação do matplotlib no readme

# GERAR NÚMEROS ALEATÓRIOS EXCLUSIVOS DENTRO DE UM INTERVALO
def generateRandomUniqueNumbers(start, end, quantity):
    numbers = random.sample(range(start, end), quantity)
    numbers.sort()
    return numbers

# BUSCA SEQUENCIAL COM SENTINELA [O(n)] (Está inserindo a sentinela na lista passada por parametro)
def sequentialSearchSentinel(key, values):
    i = 0
    values.append(key)
    pos = len(values) - 1
    while (values[i] != key):
        i += 1
    if i == (len(values) -1):
        return False
    return True

# BUSCA SEQUENCIAL SEM SENTINELA [O(n)]
def sequentialSearch(key, values):
    for i in values:
        if (key == i):
            return True
    return False

# BUSCA BINÁRIA (COM VETOR) [O(log n)]
def binarySearch(key, values):
    start = 0
    end = len(values) - 1
    while(start <= end):
        half = start + (end - start)//2
        if(values[half] == key):
            return True
        elif(values[half] < key):
            start = half + 1
        else:
            end = half - 1
    return False

# TODO BUSCA POR INTERPOLAÇÃO [O(log(log n))]
# https://marciobueno.com/arquivos/ensino/ed2/ED2_11_Pesquisa.pdf

#INICIALIZA OS DICIONÁRIOS QUE CONTERÃO O Nº DE REGISTROS : TEMPO
sequentialSearchTime = []
binarySearchTime = []
sequentialSearchSentinelTime = []
registersQtt = []

for i in range(100):
    keys = generateRandomUniqueNumbers(1, 1000, i)

    registersQtt.append(i)
    #no lugar de i+n deve ficar o tempo que demorou para cada método de busca encontrar a chave
    sequentialSearchTime.append(i+50)
    binarySearchTime.append(i+60)
    sequentialSearchSentinelTime.append(i+70)

# PLOTANDO GRÁFICOS
plt.plot(registersQtt, sequentialSearchTime)
plt.plot(registersQtt, binarySearchTime)
plt.plot(registersQtt, sequentialSearchSentinelTime)
plt.ylabel('Tempo (ms)')
plt.xlabel('Quantidade de Registros')
plt.show()


