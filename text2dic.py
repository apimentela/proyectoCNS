#!/usr/bin/env python
# -*- coding: utf-8 -*-

archivo_ciudades="DICCIONARIOS/ciudades.txt"
archivo_apellinos="DICCIONARIOS/apellidos.txt"
archivo_bancos="DICCIONARIOS/bancos.txt"
archivo_hipocoristicos="DICCIONARIOS/hipocoristicos.txt"
archivo_nombres="DICCIONARIOS/nombres.txt"
archivo_servicios="DICCIONARIOS/servicios.txt"
archivo_paises="DICCIONARIOS/paises.txt"

nombres=[archivo_nombres,archivo_apellinos,archivo_hipocoristicos]
servicios=[archivo_servicios]
ciudades=[archivo_ciudades,archivo_paises]
instituciones=[archivo_bancos]

S_nombres=[]
for archivo in nombres:
	with open(archivo,"r",encoding="utf-8") as archivo_lectura:
		S_nombres=S_nombres+[line.strip() for line in archivo_lectura.readlines() if len(line) > 1]

S_servicios=[]
for archivo in servicios:
	with open(archivo,"r",encoding="utf-8") as archivo_lectura:
		S_servicios=S_servicios+[line.strip() for line in archivo_lectura.readlines() if len(line) > 1]

S_ciudades=[]
for archivo in ciudades:
	with open(archivo,"r",encoding="utf-8") as archivo_lectura:
		S_ciudades=S_ciudades+[line.strip() for line in archivo_lectura.readlines() if len(line) > 1]

S_instituciones=[]
for archivo in instituciones:
	with open(archivo,"r",encoding="utf-8") as archivo_lectura:
		S_instituciones=S_instituciones+[line.strip() for line in archivo_lectura.readlines() if len(line) > 1]

S_nombres=sorted(set(S_nombres),reverse=True)
S_servicios=sorted(set(S_servicios),reverse=True)
S_ciudades=sorted(set(S_ciudades),reverse=True)
S_instituciones=sorted(set(S_instituciones),reverse=True)

s_nombres="r'''\\b("+"|".join(S_nombres)+")\\b'''\n"
s_NOMBRES="['''"+"''','''".join(S_nombres)+"''']\n"
s_servicios="r'''\\b("+"|".join(S_servicios)+")\\b'''\n"
s_SERVICIOS="['''"+"''','''".join(S_servicios)+"''']\n"
s_ciudades="r'''\\b("+"|".join(S_ciudades)+")\\b'''\n"
s_CIUDADES="['''"+"''','''".join(S_ciudades)+"''']\n"
s_instituciones="r'''\\b("+"|".join(S_instituciones)+")\\b'''\n"
s_INSTITUCIONES="['''"+"''','''".join(S_instituciones)+"''']\n"

archivo_diccionarios="diccionarios.py"
with open(archivo_diccionarios,"r",encoding="utf-8") as archivo_lectura:
	lineas_edicion=archivo_lectura.readlines()
archivo_edicion=open(archivo_diccionarios,"w",encoding="utf-8")

lineas_edicion[5]=lineas_edicion[5][:lineas_edicion[5].find("=")+1]+s_nombres
lineas_edicion[6]=lineas_edicion[6][:lineas_edicion[6].find("=")+1]+s_servicios
lineas_edicion[7]=lineas_edicion[7][:lineas_edicion[7].find("=")+1]+s_ciudades
lineas_edicion[8]=lineas_edicion[8][:lineas_edicion[8].find("=")+1]+s_instituciones

lineas_edicion[10]=lineas_edicion[10][:lineas_edicion[10].find("=")+1]+s_NOMBRES
lineas_edicion[11]=lineas_edicion[11][:lineas_edicion[11].find("=")+1]+s_SERVICIOS
lineas_edicion[12]=lineas_edicion[12][:lineas_edicion[12].find("=")+1]+s_CIUDADES
lineas_edicion[13]=lineas_edicion[13][:lineas_edicion[13].find("=")+1]+s_INSTITUCIONES

archivo_edicion.writelines(lineas_edicion)
archivo_edicion.close
