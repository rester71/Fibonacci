#Sucesión de Fibonacci
def main():
    #Esta Sucesión tiene la siguiente forma
    # 0 1 1 2 3 5 8 13 21 34 55 ...
    """versión sin (arreglos)"""
    tamaño = 15
    for i in range(0, tamaño):
        if i == 0:
            A = 0
            print(' ',A,' ',end=' ')
        elif i == 1:
            B = 1
            print(' ',B,' ',end=' ')
        else:
            C = A + B
            A = B
            B = C
            print(' ',C,' ',end=' ')
if __name__ == main():
    main()
