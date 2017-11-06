#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def main(args):
	"""
	Constantes útiles
	"""
	articulos=r"(el|la|los|las|un|uno|una|unos|unas|lo|al|del)"
	adj_posesivos_1=r"\b(mi|mis|nuestro|nuestros|nuestra|nuestras|tu|tus|vuestro|vuestros|vuestra|vuestras|su|sus)\b"
	adj_posesivos_1=r"\b(mi|mis|nuestro|nuestros|nuestra|nuestras)\b"
	verbo_estar=r"\best(oy|ás|á|amos|áis|án|aba|abas|aba|ábamos|abais|aban|uve|uviste|uvo|uvimos|uvisteis|uvieron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|é|és|emos|éis|én|uviera|uvieras|uviéramos|uvierais|uvieran|uviese|uvieses|uviese|uviésemos|uvieseis|uviesen|uviere|uvieres|uviere|uviéremos|uviereis|uvieren)\b"
	verbo_estar_perfecto=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren)\bestado\b"
	#~ verbo_andar
	#~ verbo_ir
	#~ verbo_viajar
	"""
	Esta sección del código simplemente lee el texto
	"""
	s_nombre_archivo=args[1]
	with open(s_nombre_archivo,"r",encoding="utf-8") as archivo:
		s_texto_original=archivo.read()

	"""
	Aquí pongo unas cuantas expresiones regulares para quitar símbolos que estén separando:
		siglas, números, direcciones web o cualquier otra cosa,
		para que sea más fácil hacer pruebas sin tener que tomar eso en cuenta,
		esa medida es MOMENTANEA, más adelante hay que trabajar en las expresiones con todo detalle
		y quitar las de este bloque, porque estas modifican el texto original
		y es preferible no hacer eso al final
	"""
	expresion_derecha=re.compile(r"([^\w\s][^A-ZÁÉÍÓÚÑ\d])")		# La expresión está separada en dos partes, una para cada lado de los signos de puntuación
	expresion_izquierda=re.compile(r"([^A-ZÁÉÍÓÚÑ\d][^\w\s])")	# la primera para el lado derecho, y esta para el lado izquierdo
	s_texto=expresion_derecha.sub(r" \1",s_texto_original)	# se reemplaza, según el lado, por espacio
	s_texto=expresion_izquierda.sub(r"\1 ",s_texto)			# para que todo lo que no está entre mayúsculas o números se separe entre espacios y sea más fácil de tratar
	s_texto=expresion_derecha.sub(r" \1",s_texto)			# esto se hace dos veces, por si el segundo afectó el texto de modo que se limpie por completo.
	expresion_media=re.compile(r"(?<! )[^\w\s](?! )")		# esta expresión buscará todos los símbolos que no fueron separados con espacios
	s_texto=expresion_media.sub("",s_texto)					# para eliminarlos y que el texto quede como si las entidades que separaban fueran una sola.
	"""
	Aquí comienzan los patrones de verdad
	"""
	expresion_en=re.compile(r"\ben\b "+ articulos +"+([a-zA-ZáÁéÉíÍoÓÚuÑñ ]+){2}")	# Encuentra: en artículo palabra1 palabra2
	resultados_en=expresion_en.finditer(s_texto)
	for resultado in resultados_en:
		print(resultado.group(0))
	return 0

if __name__ == '__main__':
	"""
	Se debe ejecutar el código con un elemento de entrada:
		- el nombre de el archivo que se va a atrabajar
	"""
	import sys
	sys.exit(main(sys.argv))
