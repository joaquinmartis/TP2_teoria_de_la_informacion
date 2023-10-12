import numpy as np
import math
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

def genera_probabilidades_palabras_codigo(palabras_codigo):
    total_palabras=0
    for palabra in palabras_codigo:
        total_palabras+=palabras_codigo[palabra]
    probabilidades_palabras_codigo={}
    for palabra in palabras_codigo:
        probabilidades_palabras_codigo[palabra]=palabras_codigo[palabra]/total_palabras
    return probabilidades_palabras_codigo   
    
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

def calcular_entropia (palabras_codigo, cant_simbolos):
    entropia = 0
    for palabra, probabilidad in palabras_codigo.items():
        print("palabra: ",palabra," probabilidad: ",probabilidad)
        if probabilidad > 0:
            entropia += probabilidad * math.log(1 / probabilidad) /math.log(cant_simbolos)
    return entropia

def calcular_longitud_media(probabiliad_palabras):
    longitud_media=0
    for palabra in probabiliad_palabras:
        longitud_media += probabiliad_palabras[palabra]*len(palabra)
    return longitud_media
    
def KraftyMcMillan(palabras_codigo,cant_simbolos):
    K=0
    for palabra in palabras_codigo.items():
        K+= cant_simbolos ** (-len(palabra))
    return K<=1

def is_codigo_compacto(palabras_codigo,cant_simbolos):
    for palabra,probabilidad in palabras_codigo.items():
        if(len(palabra)<= round(math.log(1/probabilidad)/math.log(cant_simbolos))):
            return False
    return True

def is_codigo_instantaneo(palabras_codigo):
    for palabra1 in palabras_codigo:
        for palabra2 in palabras_codigo:
            if palabra1 != palabra2 and palabra1.startswith(palabra2):
                return False
    return True

if len(sys.argv) ==2:
    palabras_codigo= cuenta_palabras_codigo(sys.argv[1])
    probabilidad_palabras=genera_probabilidades_palabras_codigo(palabras_codigo)
    print("Las probabilidades de las palabras contenidas en el archivo son:")
    for palabra, probabilidad in probabilidad_palabras.items():
        print(f"Palabra: {palabra} = {probabilidad:.2f}")
    alfabeto_codigo= genera_alfabeto_codigo(probabilidad_palabras)
    print("El alfabeto resulta: ",alfabeto_codigo)
    entropia=calcular_entropia(probabilidad_palabras,len(alfabeto_codigo))
    print("La entropia resulta: ",entropia)
    longitud_media= calcular_longitud_media(probabilidad_palabras)
    print("La longitud media resulta: ",longitud_media)
    if(KraftyMcMillan(probabilidad_palabras,len(alfabeto_codigo))):
        print("La codificación cumple con las inecuaciones de Kraft y McMillan")
        if is_codigo_instantaneo(palabras_codigo):
            print("Las longitudes de las palabras constituyen un codigo instantaneo")
    else:
        print("La codificación NO cumple con las inecuaciones de Kraft y McMillan ")
    if is_codigo_compacto(palabras_codigo,len(alfabeto_codigo)):
        print("El codigo es compacto")
  
else:
    print("Error: no se ha ingresado el nombre del archivo de texto")