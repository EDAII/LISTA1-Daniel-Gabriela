import random
# INFO: 
## Todos os valores ordenados
## Sem repetição

# GERAR NÚMEROS ALEATÓRIOS EXCLUSIVOS DENTRO DE UM INTERVALO
def generateRandomUniqueNumbers(start, end, quantity):
    numbers = random.sample(range(start, end), quantity)
    numbers.sort()
    return numbers

# BUSCA SEQUENCIAL COM SENTINELA [O(n)]
def sequentialSearch(key, values):
    i = 0
    while(i < values.length):
        if (values[i] == key):
            return True
        i += 1
    return False

# BUSCA BINÁRIA (COM VETOR) [O(log n)]
def binarySearch(key, values, start, end):
    half = (end - start)/2
    while(end >= start):
        if(values[half] == key):
            return True
        elif(values[half] < key):
            binarySearch(key, values, start, end - (end - start)/2)
        else:
            binarySearch(key, values, start + (end - start)/2, end)
    return False

# TODO BUSCA POR INTERPOLAÇÃO [O(log(log n))]
# https://marciobueno.com/arquivos/ensino/ed2/ED2_11_Pesquisa.pdf


# TODO Gerar 1.000.000.000 números aleatórios
# TODO Ordenar valores
# TODO Separar vetores de tamanho 10, 100, 10.000, 1.000.000, 100.000.000, 1.000.000.000
# TODO Criar array com o tempo que cada função demorou pra fazer a busca
# TODO Plotar o gráfico


