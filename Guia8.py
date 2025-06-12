from queue import LifoQueue as Pila
from queue import Queue as Cola
from random import randint,shuffle

def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)->Pila[int]:
    pilaADevolver :Pila[int] = Pila()
    for i in range(cantidad+1):  
        pilaADevolver.put(rnd.randint(desde,hasta))
    return pilaADevolver
pila = generar_nros_al_azar(10,1,10)
# for i in range(10):
#     print(pila.get())

def buscar_el_maximo(pila:Pila[int])->int:
    maximoVal:int = pila.get()
    while not pila.empty():
        val :int = pila.get()
        if(maximoVal<val):
            maximoVal=val
    return maximoVal

miPila :Pila[int]=Pila()
miPila = generar_nros_al_azar(10,1,10)

print(buscar_el_maximo(miPila))

def armar_secuencia_de_bingo()->Cola[int]:
    colaADevolver : Cola[int] = Cola()
    pilaRandom : Pila[int] = generar_nros_al_azar(100,0,99)
    listaVacia:list[int]=[]
    for i in range(0,100):
        listaVacia.append
    shuffle(listaVacia)
    for i in listaVacia:
        colaADevolver.put(i)
    return colaADevolver

