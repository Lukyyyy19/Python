# 1. problema pertenece (in s:seq⟨Z⟩, in e: Z) : Bool {
# requiere: { T rue }
# asegura: { (res = true) ↔(existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e) }
# }
# Implementar al menos de 3 formas distintas    este problema.

def pertenece(lista: list[int],perteneciente:int)->bool:
    for i in lista:
        if(i==perteneciente):
            return True
    return False

def pertenece(lista: list[int],perteneciente:int)->bool:
    for i in range(len(lista)):
        if(lista[i]==perteneciente):
            return True
    return False

# 2. problema divide a todos (in s:seq⟨Z⟩, in e: Z) : Bool {
# requiere: { e ̸= 0 }
# asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0) }
# }

def divide_a_todos(lista:list[int],divider:int)->bool:
    for i in lista:
        if(i%divider!=0):
            return False
    return True 

# 3. problema suma total (in s:seq⟨Z⟩) : Z {
# requiere: { T rue }
# asegura: { res es la suma de todos los elementos de s }
# }
# Nota: no utilizar la funci´on sum() nativa.

def suma_total(lista:list[int])->int:
    sumador:int=0
    for i in lista:
        sumador+=i
    return sumador

# 4. problema maximo (in s:seq⟨Z⟩) : Z {
# requiere: { |s| > 0 }
# asegura: { res = al mayor de todos los n´umeros que aparece en s }
# }
# Nota: no utilizar la funci´on max() nativa.

def maximo(lista:list[int])->int:
    maxActual:int = lista[0]
    for i in lista:
        if(i>maxActual):
            maxActual=i
    return maxActual

miLista:list[int]=[1,2,3,4,5]

# 5. problema minimo (in s:seq⟨Z⟩) : Z {
# requiere: { |s| > 0 }
# asegura: { res = al menor de todos los n´umeros que aparece en s }
# }
# Nota: no utilizar la funci´on min() nativa.

def minimo(lista:list[int])->int:
    minActual:int = lista[0]
    for i in lista:
        if(i<minActual):
            minActual=i
    return minActual

# 6. problema ordenados (in s:seq⟨Z⟩) : Bool {
# requiere: { T rue }
# asegura: { res = true ↔(para todo i ∈ Z si 0 ≤ i < (|s| − 1) → s[i] < s[i + 1] }
# }

def ordenados(lista:list[int])->bool:
    auxAnterior:int=lista[0]
    print(auxAnterior)
    for i in range(1,len(lista)):
        if(auxAnterior>lista[i]):
            return False
        auxAnterior=lista[i]
    return True
    
# 7. problema pos maximo (in s:seq⟨Z⟩) : Z {
# requiere: { T rue }
# asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ´ındice de la posici´on donde aparece el mayor elemento
# de s (si hay varios es la primera aparici´on) }
# }

def pos_aximo(lista:list[int])->int:
    for i in range(len(lista)):
        if(lista[i]==maximo(lista)):
            return i
    return -1

# 8. problema pos minimo (in s:seq⟨Z⟩) : Z {
# requiere: { T rue }
# asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ´ındice de la posici´on donde aparece el menor elemento
# de s (si hay varios es la ´ultima aparici´on) }
# }

def pos_minimo(lista:list[int])->int:
    for i in range(len(lista)):
        if(lista[i]==minimo(lista)):
            return i
    return -1

# 9. Dada una lista de palabras (seq⟨seq⟨Char⟩⟩), devolver verdadero si alguna palabra tiene longitud mayor a 7. Ejemplo:
# [“termo”, “gato”, “tener”, “jirafas”], devuelve falso.
# problema long mayorASiete (in s:seq⟨seq⟨Char⟩⟩) : Bool {
# requiere: { T rue }
# asegura: { (res = true) ↔ (existe i ∈ Z tal que (0 ≤ i < (|s| − 1)) y (|s[i]| > 7) }
# }

def long_mayorASiete(lista:list[str])->bool:
    for i in lista:
        if(len(i)>7):
            return True
    return False

# 10. Dado un texto en formato string, devolver verdadero si es pal´ındromo (se lee igual en ambos sentidos), falso en caso
# contrario. Las cadenas de texto vac´ıas o con 1 s´olo elemento son pal´ındromo.
# problema es palindroma (in s:seq⟨Char⟩) : Bool {
# requiere: { T rue }
# asegura: { (res = true) ↔ (s es igual a su reverso) }
# }

def es_palindroma(palabra:str)->bool:
    return palabra == revertir(palabra)

def revertir(palabra:str)->str:
    palabraRevertida:str=""
    for i in range((len(palabra)-1),-1,-1):
        palabraRevertida+=palabra[i]
    return palabraRevertida

# 11. Recorrer una seq⟨Z⟩ y devolver verdadero si hay 3 n´umeros iguales consecutivos, en cualquier posici´on y False en caso
# contrario.
# problema iguales consecutivos (in s:seq⟨Z⟩) : Bool {
# requiere: { T rue }
# asegura: { (res = true) ↔ (existe i, j, k ∈ Z tal que (0 ≤ i, j, k < (|s| − 1)) y (i + 2 = j + 1 = k) y
# (s[i] = s[j] = s[k])) }
# }

def iguales_consecutivos(lista:list[int])->bool:
    sonIguales:bool=False
    indice:int=0
    while(not sonIguales):
        if(not((indice+2)>=len(lista))and(son_todos_iguales([lista[indice],lista[indice+1],lista[indice+2]]))):
            sonIguales=True
            print(lista[indice],lista[indice+1],lista[indice+2])
            return True
        indice+=1
        if(indice+2>=len(lista)):
            sonIguales=False
            return False
    return False

        
def son_todos_iguales(lista:list[int])->bool:
    for i in lista:
        if(i!=lista[0]):
            return False
    return True

# 1. problema CerosEnPosicionesPares (inout s:seq⟨Z⟩) {
# requiere: { T rue }
# modifica: { s }
# asegura: { (|s| = |s@pre|) y (para todo i entero, con 0 <= i < |s|, si i es impar entonces s[i] = s@pre[i] y, si i
# es par, entonces s[i] = 0) }
# }

def CerosEnPosicionesPares(lista:list[int]):
    for i in range(len(lista)):
        if(i%2==0):
            lista[i]=0


def CerosEnPosicionesPares2(lista:list[int])->list[int]:
    unaLista:list[int]=lista.copy()
    for i in range(len(unaLista)):
        if(i%2==0):
            unaLista[i]=0
    return unaLista

milista:list[int]=[1,2,3,4]
milista1:list[int]=[1,2,3,4]
CerosEnPosicionesPares(milista)
x=CerosEnPosicionesPares2(milista1)
print("Mi lista es: " + str(milista))
print("Mi lista1 es: " + str(milista1))
print("Mi x es: " + str(x))

# 6.4. problema columnas ordenadas (in m:seq⟨seq⟨Z⟩⟩) : seq⟨Bool⟩ {
# requiere: { esM atriz(m) }
# asegura: { Para todo ´ındice de columna c: 0 ≤ c < |m[0]| → (res[c] = true ↔ ordenados(columna(m, c))) }
# asegura: {|res| = |m[0]|}
# }
# Nota: Reutilizar la funci´on ordenados() implementada previamente para listas

def filas_ordenadas(matriz:list[list[int]])->list[bool]:
    filaOrdenada:list[bool] = []
    for i in matriz:
        filaOrdenada.append(ordenados(i))
    return filaOrdenada

def columnas_ordenas(matriz:list[list[int]])->list[bool]:
    columnaOrdenada:list[bool]=[]
    currentColumna:list[int]=[]
    for valor in range(len(matriz[0])):
                columnaOrdenada.append(ordenados(lista_De_Columna(matriz,valor)))
    return columnaOrdenada

def lista_De_Columna(matriz:list[list[int]],col:int)->list[int]:
    columna:list[int]=[]
    for fila in range(len(matriz)):
        for valor in range(len(matriz[fila])):
            if(valor==col):
                columna.append(matriz[fila][valor])
    return columna

def columnas_ordenas2(matriz:list[list[int]])->list[bool]:
    columnaOrdenada:list[bool]=[]
    currentColumna:list[int]=[]
    for valor in range(len(matriz[0])):
        currentColumna:list[int]=[]
        for fila in range(len(matriz)):
            currentColumna.append(matriz[fila][valor])
        columnaOrdenada.append(ordenados(currentColumna))

               
    return columnaOrdenada



miMatriz:list[list[int]]=[[1,2,0,4],[2,3,41,4],[3,3,4,5]]
print("Columna " + str(ordenados(lista_De_Columna(miMatriz,2))))
print(columnas_ordenas2(miMatriz))
print(ordenados([0,41,4]))
