#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Archivo para llamar a freeling
import subprocess
import re

def main(args):
    s_nombre_archivo = args[1]
    with open(s_nombre_archivo+"_resultadoPre.flg","r",encoding="utf-8") as entrada:
        #no lo metí en otro with open porque daba error. Así que lo dejo así.
        salida = open(s_nombre_archivo+"_resultadoFreeling.flg", "w",encoding="utf-8")
        subprocess.call("C:\\freeling\\bin\\analyzer.bat -f es.cfg", stdin=entrada, stdout=salida, shell=True)
        salida.close()
    return 0

if __name__ == '__main__':
    """
    Se debe ejecutar el código con un elemento de entrada:
        - el nombre de el archivo que se va a atrabajar
    """
    import sys
    sys.exit(main(sys.argv))
