#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def main(args):
    '''
    recibe como argumento el archivo file_out que arrojó freeling.py
    se parsea, y se escribe un archivo nuevo donde a cada palabra le sigue su etiqueta PoS. de la forma: palabra/tag
    el resultado se guarda en textoEtiquetado.txt
    '''
    s_texto_etiquetado_token_tag = [] #esta será una lista, donde cada elemento tiene la forma palabra/tag
    s_nombre_archivo = args[1]
    with open(s_nombre_archivo,"r",encoding="utf-8") as entrada:
        s_texto_etiquetado_completo = entrada.readlines() #leemos las líneas del archivo etiquetado de freeling (file_out.txt)

    for line in s_texto_etiquetado_completo:
        line = line.split(" ")
        if len(line) == 4: #cuando no mide 4, es que algo pasó con freeling. El chiste es que no tiene etiqueta, o forma, o algo importante.
            line = line[0] +"/"+ line[2] #el 1er elemento es la palabra, y el 3er elemento el tag. Los unimos con una diagonal
            s_texto_etiquetado_token_tag.append(line)

    salida = open("textoEtiquetado.txt", "w",encoding="utf-8") #No sirve usar with open, cuando queremos escribir archivos que no existen. Por eso lo hago así. (Windows...)
    for word in s_texto_etiquetado_token_tag:
        salida.write(word + " ")#Escribimos la palabra/tag seguido de un espacio.
    salida.close()
    return 0

if __name__ == '__main__':
	"""
	Se debe ejecutar el código con un elemento de entrada:
		- el nombre de el archivo que se va a atrabajar
	"""
	import sys
	sys.exit(main(sys.argv))
