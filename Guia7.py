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
    auxAnterior:int = lista[0]
    
