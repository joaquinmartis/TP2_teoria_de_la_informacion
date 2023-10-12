import numpy as np

def Genera_Matriz_Acumulada(nombre_archivo):
    
    with open(nombre_archivo,"rt") as archivo: #se abre el archivo en modo de lectura binaria
        for linea in archivo:     # reading each line 
            for palabra in linea.split():    # reading each word            
                print(palabra)
    
    archivo.close()
    return mat


Genera_Matriz_Acumulada(r"C:\Users\Admin\Documents\GitHub\TP2_teoria_de_la_informacion\tp2_sample0.txt")

if len(sys.argv) >1:
    filename = sys.argv[1]
    mat_acum=Genera_Matriz_Acumulada(filename)
else:
    print("No se proporcionaron parámetros.")