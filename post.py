#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import pickle
from tags import listaEtiquetas

def main(args):
    '''
    recibe como argumento el archivo .flg que arrojó freeling
    Busca línea por línea a nuestra etiqueta, si la encuentra, reescribe
    la línea así como la daría freeling.
    '''
    S_texto_etiquetado_token_tag = [] #esta será una lista, donde cada elemento tiene la forma palabra/tag
    s_nombre_archivo = args[1]
    s_nombre_archivo_salida=args[2]
    with open(s_nombre_archivo+"_resultadoFreeling.flg","r",encoding="utf-8") as entrada:
        S_texto_etiquetado_completo = entrada.readlines() #leemos las líneas del archivo etiquetado de freeling
    with open(s_nombre_archivo+"_diccionarioEtiquetas.pkl","rb") as pickle_file:
        diccionarioEtiquetas=pickle.load(pickle_file)

    for index, line in enumerate(S_texto_etiquetado_completo):
        line = line.strip()
        for etiqueta in listaEtiquetas:
            if etiqueta in line:
                line = line.replace(etiqueta,diccionarioEtiquetas[etiqueta].pop(0))
                line = line.replace(" Z "," " + etiqueta[:-1] + "0 ")
                S_texto_etiquetado_completo[index] = ""+line+"\n"

    salida = open(s_nombre_archivo_salida, "w",encoding="utf-8") #No sirve usar with open, cuando queremos escribir archivos que no existen. Por eso lo hago así. (Windows...)
    for line in S_texto_etiquetado_completo:
        salida.write(line)
    salida.close()
    
    os.remove(s_nombre_archivo+"_diccionarioEtiquetas.pkl")
    os.remove(s_nombre_archivo+"_resultadoPre.flg")
    os.remove(s_nombre_archivo+"_resultadoFreeling.flg")
    return 0

"""
        if len(S_tags) == 4: #cuando no mide 4, es que algo pasó con freeling. El chiste es que no tiene etiqueta, o forma, o algo importante.
            s_token_tag = S_tags[0] +"/"+ S_tags[2] #el 1er elemento es la palabra, y el 3er elemento el tag. Los unimos con una diagonal
            S_texto_etiquetado_token_tag.append(s_token_tag)

    salida = open("textoEtiquetado.txt", "w",encoding="utf-8") #No sirve usar with open, cuando queremos escribir archivos que no existen. Por eso lo hago así. (Windows...)
    for word in S_texto_etiquetado_token_tag:
        salida.write(word + " ")#Escribimos la palabra/tag seguido de un espacio.
    salida.close()
"""

if __name__ == '__main__':
    """
    Se debe ejecutar el código con un elemento de entrada:
        - el nombre de el archivo que se va a atrabajar
    """
    import sys
    sys.exit(main(sys.argv))
