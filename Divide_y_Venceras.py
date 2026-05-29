import random
def crear_fila(inicio, fin):
    if inicio == fin:                         
        return [random.randint(99, 999)]
    mitad = (inicio + fin) // 2
    izquierda = crear_fila(inicio, mitad)      
    derecha   = crear_fila(mitad + 1, fin)    
    return izquierda + derecha    
             
def crear_matriz(fila_inicio, fila_fin, n):
    if fila_inicio == fila_fin:                            
        return [crear_fila(0, n - 1)]
    mitad = (fila_inicio + fila_fin) // 2
    superior = crear_matriz(fila_inicio, mitad,     n)      
    inferior  = crear_matriz(mitad + 1, fila_fin, n)     
    return superior + inferior 

def mostrar_fila(fila, inicio, fin):

    if inicio == fin:
        print(f"{fila[inicio]:5d}", end="")
        return
    mitad = (inicio + fin) // 2
    mostrar_fila(fila, inicio, mitad)
    mostrar_fila(fila, mitad + 1, fin)
 
def mostrar_matriz(matriz, fila_inicio, fila_fin, n):
    if fila_inicio == fila_fin:
        mostrar_fila(matriz[fila_inicio], 0, n - 1)
        print()                                          
        return
    mitad = (fila_inicio + fila_fin) // 2
    mostrar_matriz(matriz, fila_inicio, mitad,      n)
    mostrar_matriz(matriz, mitad + 1, fila_fin,  n)
 
def es_multiplo(numero):
    return 1 if (numero % 5 == 0 or numero % 7 == 0) else 0
 
def contar_fila(fila, inicio, fin):
    if inicio == fin:                                   
        return es_multiplo(fila[inicio])
    mitad = (inicio + fin) // 2
    izquierda = contar_fila(fila, inicio, mitad)         
    derecha   = contar_fila(fila, mitad + 1, fin)       
    return izquierda + derecha                           
 
def contar_matriz(matriz, fila_inicio, fila_fin, n):
    if fila_inicio == fila_fin:                             
        return contar_fila(matriz[fila_inicio], 0, n - 1)
    
    mitad = (fila_inicio + fila_fin) // 2
    superior = contar_matriz(matriz, fila_inicio, mitad,      n)   
    inferior  = contar_matriz(matriz, mitad + 1, fila_fin, n)   
    return superior + inferior                                   

n = int(input("Ingrese el número de elementos por lado de la Matriz (N x N): "))
matriz = crear_matriz(0, n - 1, n)
 
print(f"\nMatriz {n} x {n}:")
print("-" * (n * 6))
mostrar_matriz(matriz, 0, n - 1, n)
print("-" * (n * 6))

cantidad = contar_matriz(matriz, 0, n - 1, n)
print(f"=> Cantidad de números múltiplos de 5 o 7: {cantidad}")

                          
 

 
