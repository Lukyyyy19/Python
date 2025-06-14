import math
#EJERCICIO 1
def stock_productos(stock_cambios:list[tuple[str,int]])->dict[str,tuple[int,int]]:
    res:dict[str,tuple[int,int]] = dict()
    #primero relleno res con las claves
    for nombre,stock in stock_cambios:
        if(not nombre in res.keys()):
            res[nombre] = (stock,stock)
    for nombre,stock in stock_cambios:
        min:int = res[nombre][0]
        max:int = res[nombre][1]
        if(stock<min):
            res[nombre] = (stock,max)
        elif(stock>max):
            res[nombre] = (min,stock)
    return res
print(stock_productos([('a',1),('b',4),('a',5),('b',2),('c',5),('d',0),('d',10)]))

#EJERCICIO 2
def filtrar_codigos_primos(codigos_barra:list[int])->list[int]:
    res :list[int] = []
    ultimos_tres:int = 0
    for i in codigos_barra:
        suma:int = sumar_ultmios_tres(i)
        if(es_primo(suma)):
            res.append(i%1000)
    return res

def sumar_ultmios_tres(num:int)->int:
    ultimos_tres = num%1000
    unidad:int = ultimos_tres%10
    decena:int = (math.floor(ultimos_tres/10)%10)
    centena:int = (math.floor(ultimos_tres/100))%10
    return unidad + decena + centena
    

def es_primo(num:int)->bool:
    if(num == 1 or num == 0 or num<0):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

print(filtrar_codigos_primos([1352,1111111111,11111142,123,789,0o3]))