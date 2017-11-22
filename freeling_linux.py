#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Archivo para llamar a freeling
import subprocess
import re

def freeling(args):
    """
    Se pasa como parámetro el archivo que queremos analizar con freeling.
    La salida es un archivo llamado file_out.txt
    """
    s_nombre_archivo = args[1]
    with open(s_nombre_archivo+"_resultadoPre.flg","r",encoding="utf-8") as entrada:
        #no lo metí en otro with open porque daba error. Así que lo dejo así.
        salida = open(s_nombre_archivo+"_resultadoFreeling.flg", "w",encoding="utf-8")
        subprocess.call('analyzer_client 50005',stdin=entrada, stdout=salida,shell=True)
        salida.close()
    return 0

if __name__ == '__main__':
    """
    Se debe ejecutar el código con un elemento de entrada:
        - el nombre de el archivo que se va a atrabajar
    """
    import sys
    sys.exit(freeling(sys.argv))
