import random
def crear_fila(inicio, fin):
    if inicio == fin:                         
        return [random.randint(99, 999)]
    mitad = (inicio + fin) // 2
    izquierda = crear_fila(inicio, mitad)      
    derecha   = crear_fila(mitad + 1, fin)    
    return izquierda + derecha    
             
def crear_matriz(fila_ini, fila_fin, n):
    if fila_ini == fila_fin:                            
        return [crear_fila(0, n - 1)]
    mitad = (fila_ini + fila_fin) // 2
    superior = crear_matriz(fila_ini, mitad,     n)      
    inferior  = crear_matriz(mitad + 1, fila_fin, n)     
    return superior + inferior 

def mostrar_fila(fila, inicio, fin):

    if inicio == fin:
        print(f"{fila[inicio]:>5}", end="")
        return
    mitad = (inicio + fin) // 2
    mostrar_fila(fila, inicio, mitad)
    mostrar_fila(fila, mitad + 1, fin)
 
def mostrar_matriz(matriz, fila_ini, fila_fin, n):
    if fila_ini == fila_fin:
        mostrar_fila(matriz[fila_ini], 0, n - 1)
        print()                                          
        return
    mitad = (fila_ini + fila_fin) // 2
    mostrar_matriz(matriz, fila_ini, mitad,      n)
    mostrar_matriz(matriz, mitad + 1, fila_fin,  n)
 

                          
 

 
