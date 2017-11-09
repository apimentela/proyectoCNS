#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
listaEtiquetas = ["NE00C00","NE00P00","NE00O00","NE00T00","NE00I00","NE00E00","NE00M00","NE00A00","NE00L00","NE00S00","NE00U00"]

def ne00c00(matchobj):
	for etiqueta in listaEtiquetas:
		if etiqueta in matchobj.group(0):
			return matchobj.group(0)
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00C00_"+texto_nuevo+" "
	return texto_nuevo
	
def ne00p00(matchobj):
	for etiqueta in listaEtiquetas:
		if etiqueta in matchobj.group(0):
			return matchobj.group(0)
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00P00_"+texto_nuevo+" "
	return texto_nuevo
	
def ne00o00(matchobj):
	for etiqueta in listaEtiquetas:
		if etiqueta in matchobj.group(0):
			return matchobj.group(0)
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00O00_"+texto_nuevo+" "
	return texto_nuevo
	
def ne00t00(matchobj):
	for etiqueta in listaEtiquetas:
		if etiqueta in matchobj.group(0):
			return matchobj.group(0)
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00T00_"+texto_nuevo+" "
	return texto_nuevo
	
def ne00i00(matchobj):
	for etiqueta in listaEtiquetas:
		if etiqueta in matchobj.group(0):
			return matchobj.group(0)
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00I00_"+texto_nuevo+" "
	return texto_nuevo
	
def ne00e00(matchobj):
	for etiqueta in listaEtiquetas:
		if etiqueta in matchobj.group(0):
			return matchobj.group(0)
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00E00_"+texto_nuevo+" "
	return texto_nuevo
	
def ne00m00(matchobj):
	for etiqueta in listaEtiquetas:
		if etiqueta in matchobj.group(0):
			return matchobj.group(0)
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00M00_"+texto_nuevo+" "
	return texto_nuevo
	
def ne00a00(matchobj):
	for etiqueta in listaEtiquetas:
		if etiqueta in matchobj.group(0):
			return matchobj.group(0)
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00A00_"+texto_nuevo+" "
	return texto_nuevo
	
def ne00l00(matchobj):
	for etiqueta in listaEtiquetas:
		if etiqueta in matchobj.group(0):
			return matchobj.group(0)
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00L00_"+texto_nuevo+" "
	return texto_nuevo
	
def ne00s00(matchobj):
	for etiqueta in listaEtiquetas:
		if etiqueta in matchobj.group(0):
			return matchobj.group(0)
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00S00_"+texto_nuevo+" "
	return texto_nuevo

def ne00u00(matchobj):
	for etiqueta in listaEtiquetas:
		if etiqueta in matchobj.group(0):
			return matchobj.group(0)
	texto_encontrado = matchobj.group(0).strip()
	stop_list=["Messenger", "Twitter", "Facebook", "Internet", "Instagram", "Google", "Skype", "Tumblr", "Pocket", "Telegram", "Pinterest", "Reddit", "Linkedin", "Youtube", "Síguenos", "Inicio"]
	for stop in stop_list:
		if texto_encontrado.startswith(stop):
			return matchobj.group(0)
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = " "+"NE00U00_"+texto_nuevo+" "
	return texto_nuevo
