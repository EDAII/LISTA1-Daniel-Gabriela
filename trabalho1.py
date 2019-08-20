# REGRAS: 
## Todos os valores ordenados
## Sem repetição

# BUSCA SEQUENCIAL COM SENTINELA [O(n)]
def sequentialSearch(key, values):
    i = 0
    while(i < values.length):
        if (values[i] == key):
            return True
        i += 1
    return False

# BUSCA BINÁRIA (COM VETOR) [O(log n)]
def binarySearch(key, values, init, final):
    half = (final - init)/2
    while(final >= init):
        if(values[half] == key):
            return True
        elif(values[half] < key):
            binarySearch(key, values, init, final - (final - init)/2)
        else:
            binarySearch(key, values, init + (final - init)/2, final)
    return False



# TODO BUSCA POR INTERPOLAÇÃO [O(log(log n))]
# https://marciobueno.com/arquivos/ensino/ed2/ED2_11_Pesquisa.pdf


# TODO Gerar 1.000.000.000 números aleatórios
# TODO Ordenar valores
# TODO Separar vetores de tamanho 10, 100, 10.000, 1.000.000, 100.000.000, 1.000.000.000
# TODO Criar array com o tempo que cada função demorou pra fazer a busca
# TODO Plotar o gráfico


