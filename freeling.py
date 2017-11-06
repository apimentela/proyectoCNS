#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Archivo para llamar a freeling
import subprocess
import re

def main(args):
    """
    Se pasa como parámetro el archivo que queremos analizar con freeling.
    La salida es un archivo llamado file_out.txt
    Asumí que freeling está a través de Dockers escuchando en el puerto 50005, ip 172.17.0.2
    Este es el comando para levantar el servidor:
    docker run -it --rm -p 50005:50005 freeling analyze -f es.cfg --outlv tagged --ner --nec --date --server -p 50005
    """
    s_nombre_archivo = args[1]
    with open(s_nombre_archivo,"r",encoding="utf-8") as entrada:
        #no lo metí en otro with open porque daba error. Así que lo dejo así.
        salida = open("file_out.txt", "w")
        subprocess.call("docker run -i --rm freeling analyzer_client 172.17.0.2:50005", stdin=entrada, stdout=salida, shell=True)
        salida.close()
    return 0

if __name__ == '__main__':
	"""
	Se debe ejecutar el código con un elemento de entrada:
		- el nombre de el archivo que se va a atrabajar
	"""
	import sys
	sys.exit(main(sys.argv))
