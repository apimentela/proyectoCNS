#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from multiprocessing import Pipe
from diccionarios import *

diccionarioEtiquetas = {}
for etiqueta in listaEtiquetas:
    diccionarioEtiquetas[etiqueta]=[]

def ne00c00(matchobj):
    for etiqueta in listaEtiquetas:
        if etiqueta in matchobj.group(0):
            return matchobj.group(0)
    texto_encontrado = matchobj.group(0).strip()
    texto_nuevo = texto_encontrado.replace(" ","_")
    diccionarioEtiquetas["NE00C00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00C00"+" "
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
    if len(texto_encontrado.split()) > 6 or len(texto_encontrado) < 4: return matchobj.group(0)
    stop_list=["Messenger", "Twitter", "Facebook", "Internet", "Instagram", "Google", "Skype", "Tumblr", "Pocket", "Telegram", "Pinterest", "Reddit", "Linkedin", "Youtube", "Síguenos", "Inicio","Español","la cual","el cual","el que","hd","HD","pdf","PDF","la televisión"]
    for stop in stop_list:
        if texto_encontrado.startswith(stop):
            return matchobj.group(0)
    texto_nuevo = texto_encontrado.replace(" ","_")
    diccionarioEtiquetas["NE00U00"].append(texto_nuevo)
    texto_nuevo = " "+"NE00U00"+" "
    return texto_nuevo

#### DICCIONARIOS ####

re_nombres_stop_1=re.compile(s_stop_pre+"(.*?\w.*?)[\b ]+"+s_stop_post)
re_nombres_stop_2=re.compile("^"+s_stop_pre+"(.*\w.*)")
re_nombres_stop_3=re.compile("(.*?\w.*?)[\b ]+"+s_stop_post+"[\b ]+")

def ne00p01(texto):
    if len(texto.split()) > 6 or len(texto) < 3: return False
    m_nombre_compuesto=re_nombres.search(texto)
    if m_nombre_compuesto:
        texto=texto.strip()
        texto_nuevo=texto.replace(" ","_")
        diccionarioEtiquetas["NE00P01"].append(texto_nuevo)
        return True
    return False

def ne00o01(texto):
    m_institucion=re_instituciones.search(texto)
    if m_institucion:
        texto=texto.strip()
        texto_nuevo=texto.replace(" ","_")
        diccionarioEtiquetas["NE00O01"].append(texto_nuevo)
        return True
    return False

def ne00c01(texto):
    m_ciudad=re_ciudades.search(texto)
    if m_ciudad:
        texto=texto.strip()
        texto_nuevo=texto.replace(" ","_")
        diccionarioEtiquetas["NE00C01"].append(texto_nuevo)
        return True
    return False

def ne00u01(texto):
    m_ubicacion=re_ubicaciones.search(texto)
    if m_ubicacion:
        texto=texto.strip()
        texto_nuevo=texto.replace(" ","_")
        diccionarioEtiquetas["NE00U01"].append(texto_nuevo)
        return True
    return False

def diccionarios(matchobj):
    """
    Nombres
    """
    texto=matchobj.group(0)
    m_nombre_stop_1=re_nombres_stop_1.search(texto)
    m_nombre_stop_2=re_nombres_stop_2.search(texto)
    m_nombre_stop_3=re_nombres_stop_3.search(texto)
    while True:
        if m_nombre_stop_1:
            texto_bueno=m_nombre_stop_1.group(2).strip()
            if re.search(s_stop_contenido,texto_bueno): break
            texto_nuevo=" "+m_nombre_stop_1.group(1)+" NE00P00 "+m_nombre_stop_1.group(3)+" "
            texto_bueno=texto_bueno.replace(" ","_")
            diccionarioEtiquetas["NE00P00"].append(texto_bueno)
            return texto_nuevo
        if m_nombre_stop_2:
            texto_bueno=m_nombre_stop_2.group(2).strip()
            if re.search(s_stop_contenido,texto_bueno): break
            texto_nuevo=" "+m_nombre_stop_2.group(1)+" NE00P00 "
            texto_bueno=texto_bueno.replace(" ","_")
            diccionarioEtiquetas["NE00P00"].append(texto_bueno)
            return texto_nuevo
        if m_nombre_stop_3:
            texto_bueno=m_nombre_stop_3.group(1).strip()
            if re.search(s_stop_contenido,texto_bueno): break
            texto_nuevo=" NE00P00 "+m_nombre_stop_3.group(2)+" "
            texto_bueno=texto_bueno.replace(" ","_")
            diccionarioEtiquetas["NE00P00"].append(texto_bueno)
            return texto_nuevo
        break
    """
    Diccionarios
    """
    if ne00p01(matchobj.group(0)) : return " NE00P01 "
    if ne00o01(matchobj.group(0)) : return " NE00O01 "
    if ne00u01(matchobj.group(0)) : return " NE00U01 "
    #~ if ne00c01(matchobj.group(0)) : return " NE00C01 "
    
    return matchobj.group(0)
