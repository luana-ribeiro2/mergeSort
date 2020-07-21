def mergeSort(listaOrdenar):
    if len(listaOrdenar) > 1:
        meio = len(listaOrdenar)//2
        dire = listaOrdenar[meio:]
        esq = listaOrdenar[:meio]
        mergeSort(dire)
        mergeSort(esq)
        i = j = l = 0
        while j < len(dire) and i < len(esq):
            if esq[i] > dire[j]:
                listaOrdenar[l] = dire[j]
                j += 1
            else:
                listaOrdenar[l] = esq[i]
                i += 1
            l += 1
        while j < len(dire):
            listaOrdenar[l]=dire[j]
            j += 1
            l += 1
        while i < len(esq):
            listaOrdenar[l]=esq[i]
            i += 1
            l += 1

def splitInt(lista):
    lista1 = lista.split(' ')
    lista2 = []
    for x in lista1:
        lista2.append(int(x))
    return lista2

t = int(input(''))
for i in range(t):
    string = ''
    lista = input('')
    listaComInteiro = splitInt(lista)
    mergeSort(listaComInteiro)
    for x in range(0, len(listaComInteiro)):
        if x == len(listaComInteiro)-1:
            string+=str(listaComInteiro[x])
        else:
            string+=str(listaComInteiro[x])+' '
    
    print(string)