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

#EJERCICIO 3
def subsecuencia_mas_larga(tipos_pacientes_atendidos:list[str])->int:
    contador:int = 0
    contador_max: int=0
    indice:int = 0
    anterior_fue_aceptado:bool = False
    animales_aceptados = ['perro','gato']
    for i in range(len(tipos_pacientes_atendidos)):
        if(tipos_pacientes_atendidos[i] in animales_aceptados):
            contador+=1
            # if(not anterior_fue_aceptado):
                
            anterior_fue_aceptado = True
        else:
            if contador > contador_max:
                contador_max = contador
                indice = i-contador_max
            anterior_fue_aceptado = False
            contador = 0
    if contador > contador_max:
            contador_max = contador
            indice = len(tipos_pacientes_atendidos)-contador_max   
    return indice

#EJERCICIO 4
def un_responsable_por_turno(grilla_horaria:list[list[str]])->list[tuple[bool,bool]]:
    res:list[tuple[bool,bool]] = []
    persona_anterior:str = grilla_horaria[0][0]
    for fila in range(len(grilla_horaria)):
        misma_persona_man:bool = True
        misma_persona_tar:bool = True
        for persona in range(len(grilla_horaria[fila])):
            if(persona==4):
                persona_anterior = grilla_horaria[fila][persona]
            if(grilla_horaria[fila][persona]!=persona_anterior):
                if(persona<4):
                    misma_persona_man = False
                else:
                    misma_persona_tar = False
            persona_anterior = grilla_horaria[fila][persona]
        res.append((misma_persona_man,misma_persona_tar))
    return res

print(un_responsable_por_turno([['a','a','a','b','a','a','a','a'],
                                ['a','a','a','a','c','a','a','a'],
                                ['a','a','a','b','a','a','a','b'],
                                ['a','a','a','b','a','a','a','a']]))
        
        
            


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
