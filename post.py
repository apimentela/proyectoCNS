#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import pickle

from diccionarios import *

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
        if " NP00000 " in line:
            entidad=line.split()[0]
            entidad=entidad.replace("_"," ")
            if index < len(S_texto_etiquetado_completo)-1 and re.search(" V\w[IMCG]\w{4} ",S_texto_etiquetado_completo[index+1]):
                if len(entidad.split()) > 6 or len(entidad) < 3: continue
                if re.search(s_stop_contenido,entidad): continue
                line=line.replace(" NP00000 ", " NE00P00 ")
                S_texto_etiquetado_completo[index] = ""+line+"\n"
                continue
            if entidad in S_nombres:
                line=line.replace(" NP00000 ", " NE00P00 ")
                S_texto_etiquetado_completo[index] = ""+line+"\n"
                continue
            if entidad in S_ciudades:
                line=line.replace(" NP00000 ", " NE00C00 ")
                S_texto_etiquetado_completo[index] = ""+line+"\n"
                continue
            if entidad in S_instituciones:
                line=line.replace(" NP00000 ", " NE00O00 ")
                S_texto_etiquetado_completo[index] = ""+line+"\n"
                continue
            if entidad in S_ubicaciones:
                line=line.replace(" NP00000 ", " NE00U00 ")
                S_texto_etiquetado_completo[index] = ""+line+"\n"
                continue
            if entidad in S_servicios:
                line=line.replace(" NP00000 ", " NE00S00 ")
                S_texto_etiquetado_completo[index] = ""+line+"\n"
                continue

    salida = open(s_nombre_archivo_salida, "w",encoding="utf-8") #No sirve usar with open, cuando queremos escribir archivos que no existen. Por eso lo hago así. (Windows...)
    for line in S_texto_etiquetado_completo:
        salida.write(line)
    salida.close()
    
    os.remove(s_nombre_archivo+"_diccionarioEtiquetas.pkl")
    os.remove(s_nombre_archivo+"_resultadoPre.flg")
    os.remove(s_nombre_archivo+"_resultadoFreeling.flg")
    return 0

if __name__ == '__main__':
    """
    Se debe ejecutar el código con un elemento de entrada:
        - el nombre de el archivo que se va a atrabajar
    """
    import sys
    sys.exit(main(sys.argv))
