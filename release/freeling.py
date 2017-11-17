#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def main(args):
    s_nombre_archivo = args[1]
    with open(s_nombre_archivo+"_resultadoPre.flg","r",encoding="utf-8") as entrada:
        salida = open(s_nombre_archivo+"_resultadoFreeling.flg", "w",encoding="utf-8")
        subprocess.call("C:\\freeling\\bin\\analyzer_client.exe localhost:50005", stdin=entrada, stdout=salida, shell=True)
        salida.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
