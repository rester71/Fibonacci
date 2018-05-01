#Sucesión de Fibonacci
def main():
    #Esta Sucesión tiene la siguiente forma
    # 0 1 1 2 3 5 8 13 21 34 55 ...
    """versión facil con listas(arreglos)"""
    tamaño = 10
    lista = []
    #agrego los dos primeros numeros a la lista
    lista.append(0)
    lista.append(1)
    for i in range(0, tamaño):
        if i+1 >= tamaño: #no necesario
            break
        aux = lista[i] + lista[i+1]
        lista.append(aux)
    print(lista)

if __name__ == main():
    main()
