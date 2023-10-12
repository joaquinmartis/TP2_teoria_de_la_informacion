import numpy as np

def genera_palabras_codigo(nombre_archivo):
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
    
def genera_alfabeto_codigo(probabilidades_palabras_codigo):
    alfabeto_codigo=[]
    for palabra in probabilidades_palabras_codigo:
        for letra in palabra:
            if letra not in alfabeto_codigo:
                alfabeto_codigo.append(letra)
    alfabeto_codigo.sort()
    return alfabeto_codigo

def genera_probabilidades_simbolos(palabras_codigo,alfabeto_codigo):
    total_simbolos=0
    probabilidades_simbolos={for letra in alfabeto_codigo :0}
    for palabra in palabras_codigo:
        for letra in palabra:
            if letra in alfabeto_codigo:
                probabilidades_simbolos[letra]+=palabras_codigo[palabra]
    for letra in probabilidades_simbolos:
        total_simbolos+=probabilidades_simbolos[letra]
    for letra in probabilidades_simbolos:
        probabilidades_simbolos/=total_simbolos
    return probabilidades_simbolos

palabras_codigo=genera_palabras_codigo(r"tp2_sample0.txt") #Es diccionario
probabilidades_palabras_codigo=genera_probabilidades_palabras_codigo(palabras_codigo) #Es diccionario
print(probabilidades_palabras_codigo)
alfabeto_codigo=genera_alfabeto_codigo(probabilidades_palabras_codigo)
print(alfabeto_codigo)
probabilidades_simbolos=genera_probabilidades_simbolos(palabras_codigo,alfabeto_codigo)
print(probabilidades_simbolos)
#if len(sys.argv) >1:
#   filename = sys.argv[1]
#    mat_acum=Genera_Matriz_Acumulada(filename)
#else:
#    print("No se proporcionaron parámetros.")