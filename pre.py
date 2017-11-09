#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from replaces import *

def main(args):
	"""
	Constantes útiles
	"""
	articulos=r"\b(el|la|los|las|un|uno|una|unos|unas|lo|al|del)\b"
	articulos_en=r"\b(el|la|los|las|lo|al|del)\b"
	adj_posesivos=r"\b(mi|mis|nuestro|nuestros|nuestra|nuestras|tu|tus|vuestro|vuestros|vuestra|vuestras|su|sus)\b"
	adj_posesivos_1era_persona=r"\b(mi|mis|nuestro|nuestros|nuestra|nuestras)\b"
	verbo_estar=r"\b[Ee]st(oy|ás|á|amos|áis|án|aba|abas|aba|ábamos|abais|aban|uve|uviste|uvo|uvimos|uvisteis|uvieron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|é|és|emos|éis|én|uviera|uvieras|uviéramos|uvierais|uvieran|uviese|uvieses|uviese|uviésemos|uvieseis|uviesen|uviere|uvieres|uviere|uviéremos|uviereis|uvieren)\b"
	verbo_estar_perfecto=r"\b[hH](e|as|a|emos|abéis|an|abía|abías|abía|abíamos|abíais|abían|ube|ubiste|ubo|ubimos|ubisteis|ubieron|abré|abrás|abrá|abremos|abréis|abrán|abría|abrías|abríamos|abríais|abrían|aya|ayas|ayamos|ayáis|ayan|ubiera|ubieras|ubiéramos|ubierais|ubieran|ubiese|ubieses|ubiésemos|ubieseis|ubiesen|ubiere|ubieres|ubiéremos|ubiereis|ubieren) +estado\b"
	verbo_andar=r"\band(o|as|a|amos|áis|an|aba|abas|aba|ábamos|abais|aban|uve|uviste|uvo|uvimos|uvisteis|uvieron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|e|es|emos|éis|en|uviera|uvieras|uviéramos|uvierais|uvieran|uviese|uvieses|uviese|uviésemos|uvieseis|uviesen|uviere|uvieres|uviere|uviéremos|uviereis|uvieren)\b"
	verbo_andar_perfecto=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren) +andado\b"
	verbo_ir=r"\bv(oy|as|a|amos|ais|an|aya|ayas|ayamos|ayáis|ayan)|\b(i|í)(ba|bas|bamos|bais|ban|ré|rás|rá|remos|réis|rán|ría|rías|ríamos|ríais|rían)|\bfu(i|iste|e|imos|isteis|eron|era|eras|éramos|erais|eran|ese|eses|ésemos|eseis|esen|ere|eres|éremos|ereis|eren)\b"
	verbo_ir_perfecto=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren) +ido\b"
	verbo_viajar=r"\bviaj(o|as|a|amos|áis|an|aba|abas|aba|ábamos|abais|aban|é|aste|ó|amos|asteis|aron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|e|es|emos|éis|en|ara|aras|áramos|arais|aran|ase|ases|ásemos|aseis|asen|are|ares|áremos|areis|aren)\b"
	verbo_viajar_perfecto=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren) +viajado\b"
	"""
	Esta sección del código simplemente lee el texto
	"""
	s_nombre_archivo=args[1]
	with open(s_nombre_archivo,"r",encoding="utf-8") as archivo:
		s_texto_original=archivo.read()

	#~ """
	#~ Aquí pongo unas cuantas expresiones regulares para quitar símbolos que estén separando:
		#~ siglas, números, direcciones web o cualquier otra cosa,
		#~ para que sea más fácil hacer pruebas sin tener que tomar eso en cuenta,
		#~ esa medida es MOMENTANEA, más adelante hay que trabajar en las expresiones con todo detalle
		#~ y quitar las de este bloque, porque estas modifican el texto original
		#~ y es preferible no hacer eso al final
	#~ """
	#~ expresion_derecha=re.compile(r"([^\w\s][^A-ZÁÉÍÓÚÑ\d])")			# La expresión está separada en dos partes, una para cada lado de los signos de puntuación
	#~ expresion_izquierda=re.compile(r"([^A-ZÁÉÍÓÚÑ\d][^\w\s])")		# la primera para el lado derecho, y esta para el lado izquierdo
	#~ s_texto=expresion_derecha.sub(r" \1",s_texto_original)			# se reemplaza, según el lado, por espacio
	#~ s_texto=expresion_izquierda.sub(r"\1 ",s_texto)					# para que todo lo que no está entre mayúsculas o números se separe entre espacios y sea más fácil de tratar
	#~ s_texto=expresion_derecha.sub(r" \1",s_texto)					# esto se hace dos veces, por si el segundo afectó el texto de modo que se limpie por completo.
	#~ expresion_media=re.compile(r"(?<! )[^\w\s](?! )")				# esta expresión buscará todos los símbolos que no fueron separados con espacios
	#~ s_texto=expresion_media.sub("",s_texto)							# para eliminarlos y que el texto quede como si las entidades que separaban fueran una sola.
	s_texto=s_texto_original
	"""
	Aquí comienzan los patrones de verdad
	"""
	"""
	Patrones para lugares encontrados con "en"
	"""
	en_articulos=articulos_en+r"( +[^A-ZÁÉÍÓÚÑ\W]+ +)*?"	# Se muestran dos patrones principalmente, uno comienza con artículos
	en_mayusculas=r"(([A-ZÁÉÍÓÚÑ]+ +)+|([A-ZÁÉÍÓÚÑ][^A-ZÁÉÍÓÚÑ\W]+ +)+)"		# y otro con mayúsculas
	expresion_en=re.compile(r"(?<=\b[Ee]n )+("+en_articulos+en_mayusculas+"|"+en_mayusculas+")")	# esta expresión encuentra todo lo que comienza con en, y le sigue un artículo con alguna mayúscula en algún punto, o puras mayúsculas. A los artículos, se les quitan los "un" y derivados, no parecen dar ningún buen resultado
	s_texto_nuevo=expresion_en.sub(ne00u00,s_texto)
	print(s_texto_nuevo)
	#~ resultados_en=expresion_en.finditer(s_texto)
	#~ for resultado in resultados_en:
		#~ if " que " in resultado.group(0): continue
		#~ if len(resultado.group(0).split()) > 6 :continue
		#~ print(resultado.group(0))
	"""
	Patrones para lugares encontrados con "entre"
	"""
	expresion_entre=re.compile(r"("+verbo_estar+"|"+verbo_estar_perfecto+")"+" +entre +[\w ]+")
	#~ resultados_entre=expresion_entre.finditer(s_texto)
	#~ for resultado in resultados_entre:
		#~ print(resultado.group(0))
	"""
	Patrones para lugares encontrados con "cerca/lejos"
	"""
	expresion_cerca_lejos=re.compile(r"("+verbo_estar+"|"+verbo_estar_perfecto+")"+" +(cerca|lejos) +de +[\w ]+")
	#~ resultados_cerca_lejos=expresion_cerca_lejos.finditer(s_texto)
	#~ for resultado in resultados_cerca_lejos:
		#~ print(resultado.group(0))
	"""
	Patrón para placas.
	"""
	placas_1=r"[A-HJ-NPR-Z]{3}-?[0-9]{2}-?[0-9]{2}"
	placas_2=r"[A-HJ-NPR-Z]{3}-?[0-9]{3}-?[A-HJ-NPR-Z]"
	placas_3=r"[A-HJ-NPR-Z]-?[0-9]{2,3}-?[A-HJ-NPR-Z]{3}"
	placas_4=r"[0-9]{3}-?[A-HJ-NPR-Z]{3}"
	placas_5=r"[A-HJ-NPR-Z]{2}-?[0-9]{2}-?[0-9]{3}"
	placas_6=r"[0-9]-?[A-HJ-NPR-Z]-?[0-9]{2}-?[A-HJ-NPR-Z]{2}"
	placas_7=r"[0-9]-?[A-HJ-NPR-Z]-?[0-9]-?[A-HJ-NPR-Z]{3}"
	expresion_placas = re.compile(r"("+placas_1+"|"+placas_2+"|"+placas_3+"|"+placas_4+"|"+placas_5+"|"+placas_6+"|"+placas_7+")")
	#~ resultados_placas=expresion_placas.finditer(s_texto)
	#~ for resultado in resultados_placas:
		#~ print(resultado.group(0))

	"""
	Patrón para correo electrónico
	"""
	#Encontré esa expresión regular en internet.
	#https://stackoverflow.com/questions/201323/using-a-regular-expression-to-validate-an-email-address
	#Me pareció una buena explicación. Tiene hasta el autómata con el que generaron la expresión.
	expresion_correo = re.compile(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|" + r'"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])')
	#~ resultados_correo=expresion_correo.finditer(s_texto)
	#~ for resultado in resultados_correo:
		#~ print(resultado.group(0))
	"""
	Patrón de Direcciones IP
	"""
	expresion_IPv4 = re.compile(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", re.M)
	#~ resultados_IPv4 = expresion_IPv4.finditer(s_texto)
	#~ for resultado in resultados_IPv4:
			#~ print(resultado.group(0))

	"""
	Patrón de números telefónicos
	"""
	expresion_telefono = re.compile(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")
	#~ resultados_telefono = expresion_telefono.finditer(s_texto)
	#~ for resultado in resultados_telefono:
		#~ print(resultado.group(0))

	"""
	Patrón de sitios web
	"""
	expresion_url = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
	#~ resultados_url = expresion_url.finditer(s_texto)
	#~ for resultado in resultados_url:
		#~ print(resultado.group(0))

	return 0


if __name__ == '__main__':
	"""
	Se debe ejecutar el código con un elemento de entrada:
		- el nombre de el archivo que se va a atrabajar
	"""
	import sys
	sys.exit(main(sys.argv))
