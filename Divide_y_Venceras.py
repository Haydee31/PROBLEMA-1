import random
def crear_fila(inicio, fin):
    if inicio == fin:                         
        return [random.randint(99, 999)]
    mitad = (inicio + fin) // 2
    izquierda = crear_fila(inicio, mitad)      
    derecha   = crear_fila(mitad + 1, fin)    
    return izquierda + derecha                 


 
