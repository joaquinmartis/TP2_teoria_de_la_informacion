import numpy as np
import sys
def cuenta_palabras_codigo(nombre_archivo):
    palabras_codigo={}
    with open(nombre_archivo,"rt") as archivo: #se abre el archivo en modo de lectura binaria
        for linea in archivo:     # reading each line 
            for palabra in linea.split():    # reading each word            
                if palabra in palabras_codigo:
                    palabras_codigo[palabra]+=1
                else:
                    palabras_codigo[palabra]=1
    
    archivo.close()
    return palabras_codigo

def probabilidad_palabras(palabras_codigo):
    total= sum(palabras_codigo.values())
    if(total!=0):
        for palabra in palabras_codigo:
            palabras_codigo[palabra]/=total
    
def genera_alfabeto_codigo(palabras_codigo):
    alfabeto = set()  # Usamos un conjunto para asegurar caracteres únicos

    for palabra in palabras_codigo:
        alfabeto.update(set(palabra))

    return sorted(list(alfabeto))  # Convierte el conjunto a una lista ordenada


def genera_probabilidades_simbolos(palabras_codigo,alfabeto_codigo):
    total_simbolos=0
#    probabilidades_simbolos={for letra in alfabeto_codigo :0}
    for palabra in palabras_codigo:
        for letra in palabra:
            if letra in alfabeto_codigo:
                probabilidades_simbolos[letra]+=palabras_codigo[palabra]
    for letra in probabilidades_simbolos:
        total_simbolos+=probabilidades_simbolos[letra]
    for letra in probabilidades_simbolos:
        probabilidades_simbolos/=total_simbolos
    return probabilidades_simbolos



#probabilidades_simbolos=genera_probabilidades_simbolos(palabras_codigo,alfabeto_codigo)
#print(probabilidades_simbolos)

if len(sys.argv) ==2:
    palabras_codigo= cuenta_palabras_codigo(sys.argv[1])
    probabilidad_palabras(palabras_codigo)
    print("Las probabilidades de las palabras contenidas en el archivo son:")
    for palabra, probabilidad in palabras_codigo.items():
        print(f"{palabra}: {probabilidad:.2f}")
    alfabeto_codigo= genera_alfabeto_codigo(palabras_codigo)
    print("El alfabeto resulta: ",alfabeto_codigo)
else:
    print("Error: no se ha ingresado el nombre del archivo de texto")