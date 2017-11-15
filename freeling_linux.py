#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Archivo para llamar a freeling
import subprocess
import re

def freeling(s_entrada):
    """
    Se pasa como parámetro el archivo que queremos analizar con freeling.
    La salida es un archivo llamado file_out.txt
    """
    subprocess.call('echo "'+ s_entrada +'" | analyze -f /usr/share/freeling/config/es.cfg',shell=True)
    return 0

if __name__ == '__main__':
    """
    Se debe ejecutar el código con un elemento de entrada:
        - el nombre de el archivo que se va a atrabajar
    """
    import sys
    sys.exit(freeling(sys.argv[1]))
