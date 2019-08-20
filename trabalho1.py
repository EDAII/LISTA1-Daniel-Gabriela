import random
# INFO: 
## Todos os valores ordenados
## Sem repetição

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
def binarySearch(key, values, start, end):
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


# TODO Gerar 1.000.000.000 números aleatórios
# TODO Ordenar valores
# TODO Separar vetores de tamanho 10, 100, 10.000, 1.000.000, 100.000.000, 1.000.000.000
# TODO Criar array com o tempo que cada função demorou pra fazer a busca
# TODO Plotar o gráfico


