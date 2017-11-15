#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
listaEtiquetas = ["NE00C00","NE00P00","NE00O00","NE00T00","NE00I00","NE00E00","NE00M00","NE00A00","NE00L00","NE00S00","NE00U00","NE00W00"]
diccionarioEtiquetas = {"NE00C00":[],"NE00P00":[],"NE00O00":[],"NE00T00":[],"NE00I00":[],"NE00E00":[],"NE00M00":[],"NE00A00":[],"NE00L00":[],"NE00S00":[],"NE00U00":[],"NE00W00":[]}

def ne00c00(matchobj):
    for etiqueta in listaEtiquetas:
        if etiqueta in matchobj.group(0):
            return matchobj.group(0)
    texto_encontrado = matchobj.group(0).strip()
    texto_nuevo = texto_encontrado.replace(" ","_")
    diccionarioEtiquetas["NE00C00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00C00"+" "
    return texto_nuevo
    
def ne00p00(matchobj):
    for etiqueta in listaEtiquetas:
        if etiqueta in matchobj.group(0):
            return matchobj.group(0)
    texto_encontrado = matchobj.group(0).strip()
    texto_nuevo = texto_encontrado.replace(" ","_")
    diccionarioEtiquetas["NE00P00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00P00"+" "
    return texto_nuevo
    
def ne00o00(matchobj):
    for etiqueta in listaEtiquetas:
        if etiqueta in matchobj.group(0):
            return matchobj.group(0)
    texto_encontrado = matchobj.group(0).strip()
    texto_nuevo = texto_encontrado.replace(" ","_")
    diccionarioEtiquetas["NE00O00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00O00"+" "
    return texto_nuevo
    
def ne00t00(matchobj):
    for etiqueta in listaEtiquetas:
        if etiqueta in matchobj.group(0):
            return matchobj.group(0)
    texto_encontrado = matchobj.group(0).strip()
    texto_nuevo = texto_encontrado.replace(" ","_")
    diccionarioEtiquetas["NE00T00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00T00"+" "
    return texto_nuevo
    
def ne00i00(matchobj):
    for etiqueta in listaEtiquetas:
        if etiqueta in matchobj.group(0):
            return matchobj.group(0)
    texto_encontrado = matchobj.group(0).strip()
    texto_nuevo = texto_encontrado.replace(" ","_")
    diccionarioEtiquetas["NE00I00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00I00"+" "
    return texto_nuevo
    
def ne00e00(matchobj):
    for etiqueta in listaEtiquetas:
        if etiqueta in matchobj.group(0):
            return matchobj.group(0)
    texto_encontrado = matchobj.group(0).strip()
    texto_nuevo = texto_encontrado.replace(" ","_")
    diccionarioEtiquetas["NE00E00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00E00"+" "
    return texto_nuevo
    
def ne00m00(matchobj):
    for etiqueta in listaEtiquetas:
        if etiqueta in matchobj.group(0):
            return matchobj.group(0)
    texto_encontrado = matchobj.group(0).strip()
    texto_nuevo = texto_encontrado.replace(" ","_")
    diccionarioEtiquetas["NE00M00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00M00"+" "
    return texto_nuevo
    
def ne00a00(matchobj):
    for etiqueta in listaEtiquetas:
        if etiqueta in matchobj.group(0):
            return matchobj.group(0)
    texto_encontrado = matchobj.group(0).strip()
    texto_nuevo = texto_encontrado.replace(" ","_")
    diccionarioEtiquetas["NE00A00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00A00"+" "
    return texto_nuevo
    
def ne00w00(matchobj):
    for etiqueta in listaEtiquetas:
        if etiqueta in matchobj.group(0):
            return matchobj.group(0)
    texto_encontrado = matchobj.group(0).strip()
    texto_nuevo = texto_encontrado.replace(" ","_")
    diccionarioEtiquetas["NE00W00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00W00"+" "
    return texto_nuevo
    
def ne00s00(matchobj):
    for etiqueta in listaEtiquetas:
        if etiqueta in matchobj.group(0):
            return matchobj.group(0)
    texto_encontrado = matchobj.group(0).strip()
    texto_nuevo = texto_encontrado.replace(" ","_")
    diccionarioEtiquetas["NE00S00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00S00"+" "
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
    diccionarioEtiquetas["NE00U00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00U00"+" "
    return texto_nuevo
