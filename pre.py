#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def main(args):
	s_nombre_archivo=args[1]
	with open(s_nombre_archivo,"r") as archivo:
		s_texto_original=archivo.read()
	
	expresion_derecha=re.compile(r"([^\w\s][^A-Z\d])")
	expresion_izquierda=re.compile(r"([^A-Z\d][^\w\s])")
	s_texto=expresion_derecha.sub(r" \1",s_texto_original)
	s_texto=expresion_izquierda.sub(r"\1 ",s_texto)
	s_texto=expresion_derecha.sub(r" \1",s_texto)
	
	expresion_media=re.compile(r"(?<! )[^\w\s](?! )")
	s_texto=expresion_media.sub("",s_texto)
	
	expresion_en=re.compile(r"\ben [\w\s]*")
	resultados_en=expresion_en.finditer(s_texto)
	for resultado in resultados_en:
		print(resultado.group(0))
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
