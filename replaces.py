#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
listaEtiquetas = ["NE00U00","NE00T00","NE00I00","NE00E00","NE00M00"]

def ne00u00(matchobj):
	for etiqueta in listaEtiquetas:
		if etiqueta in matchobj.group(0):
			return matchobj.group(0)
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00U00_"+texto_nuevo+" "
	return texto_nuevo

def ne00t00(matchobj):
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00T00_"+texto_nuevo+" "
	return texto_nuevo


def ne00i00(matchobj):
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00I00_"+texto_nuevo+" "
	return texto_nuevo


def ne00e00(matchobj):
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00E00_"+texto_nuevo+" "
	return texto_nuevo


def ne00m00(matchobj):
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00M00_"+texto_nuevo+" "
	return texto_nuevoS
