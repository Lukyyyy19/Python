from queue import Queue as Cola
#Ejercicio 1:
def maximas_cantidades_consecutivas(v:list[int])->dict[int:int]:
    #Claves de res son todos los numeros de v sin repetir
    res:dict[int,int] = dict()
    #los valores de res son la maxima cantidad de apariciones consecutivas de la llave
    #Primero voy a rellenar todas las llaves de res.
    for num in v:
       if(not num in res.keys()):
           res[num] = maxima_cantidad_de_repeticiones(num,v)
    return res

def maxima_cantidad_de_repeticiones(numero:int,v:list[int])->int:
    contador:int=0
    mayor_apariciones:list[int] = []
    for num in v:
        if(num == numero):
            contador+=1
        else:
            mayor_apariciones.append(contador)
            contador = 0
    return maximo(mayor_apariciones)

def maximo(v:list[int])->int:
    aux:int = v[0]
    for num in v:
        if(num>aux):
            aux=num
    return aux

#Ejercicio 2
def maxima_cantidad_primos(A:list[list[int]])->int:
    #Tengo que devolver la maxima cantidad de primos de las columnas de A ?
    longitud_fila:int = len(A[0])
    matriz_en_una_fila:list[int]=[]
    contador:int = 0
    res:int=0
    for fila in A:
        for celda in fila:
            matriz_en_una_fila.append(celda)
    for i in range(longitud_fila):
        #esto seria una columna
        for pos in range(i,len(matriz_en_una_fila),longitud_fila):
            if(es_primo(matriz_en_una_fila[pos])):
                contador+=1
        if(contador>res):
            res = contador
        contador = 0
    return res

def es_primo(num:int)->bool:
    if(num==1 or num == 0 or (num<0)):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

#Ejercicio 3
def tuplas_positivas_y_negativas(cola:Cola[tuple[int,int]]):
    colaaPos:Cola[tuple[int,int]] = Cola()
    colaaNeg:Cola[tuple[int,int]] = Cola()

    while not cola.empty() :
        tupla = cola.get()
        if(tupla[0]*tupla[1]>0):
            colaaPos.put(tupla)
        elif(tupla[0]*tupla[1]<0):
            colaaNeg.put(tupla)
    while not colaaPos.empty():
            cola.put(colaaPos.get())
    while not colaaNeg.empty():
        cola.put(colaaNeg.get())

#Ejercicio4
#def resolver_cuenta(s:str)->float:
     
# def separar_numeros(s:str)->list[float]:
#     anterior:str = ""
#     anterior_fue_decimal:bool = False
#     res:list[float]=[]
#     for char in range(len(s)):
#         if(s[char] == '.'):
#             res[char-1] = (float(anterior) + float('.'+s[char+1]))
#             anterior_fue_decimal = True
#             continue
#         elif(anterior_fue_decimal):
#             continue
#         elif(s[char]!='+' and s[char]!='-'):
#             res.append(float(s[char]))
#             anterior = s[char]
#     return res

# print(separar_numeros('-10+15.5-23.5+23.4'))
