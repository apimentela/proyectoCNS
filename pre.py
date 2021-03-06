#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pickle
from multiprocessing import Process, Pipe
from diccionarios import re_servicios
from tags import *

def proceso_en(s_texto,conn):
    """
    Patrones para lugares encontrados con "en"
    """
    articulos_en=r"\b(el|la|los|las|lo|al|del)\b"
    # TODO : al parecer, aún se puede filtrar mucho si se fijan en las palabras funcionales en los extremos de las supuestas ubicaciones, además, hay que buscar cosas parecidas a "la cual, el cual, el que..." que tampoco dan buenos resultados, y se necesita también una lista de idiomas, por cosas como "en Español..." y cosas como "en HD, en PDF, en la televisión,...", y categorías de periódicos. Además de colocaciones como "en buscda de...."
    # TODO : verificar expresiones de tiempo como "en el siglo.."
    # TODO : verificar tambián partes del cuerpo "en el pecho.."
    # TODO : entidades con mayúsculas pueden tener palabras con minúsculas en medio, aunque no he encontrado que haya más de dos, revisar expresión regular.
    # TODO : hay que analizar lo de las palabras funcional en los extremos de las entidades, muchas veces solo marcan el final, no que no lo sea. (quitar "en" de esas palabras y agregar "leer", y quizá se tenga que revisar verbos en general, palabras como "te" parecen ser terminantes)
    # TODO : varias entidades que van en mayúsculas y minúsculas si terminan o comienzan con UNA sigla en puras mayúsculas, revisar expresión regular. *revisar que no sea peor el resultado, hay siglas que son seguidas de mayúsculas pero no tienen nada que ver
    # TODO : algunos lugares son seguidos de un lugar más general en paréntesis. (no son tan comúnes)
    en_articulos=articulos_en+r"( +[^A-ZÁÉÍÓÚÑ\W]+ +)*?"    # Se muestran dos patrones principalmente, uno comienza con artículos
    en_mayusculas=s_patrones_mayusculas
    expresion_en=re.compile(r"(?<=\b[Ee]n )+("+en_articulos+en_mayusculas+"|"+en_mayusculas+")")    # esta expresión encuentra todo lo que comienza con en, y le sigue un artículo con alguna mayúscula en algún punto, o puras mayúsculas. A los artículos, se les quitan los "un" y derivados, no parecen dar ningún buen resultado
    s_texto=expresion_en.sub(ne00u00,s_texto)
    conn.send([s_texto,diccionarioEtiquetas])
    conn.close()

def proceso_diccionarios(s_texto,conn):
    """
    Diccionarios
    """
    # TODO: Muchos nombres parecen traer un inicio de conversación al final que comienza con mayúsculas, la mayoría parece ser una palabra funcional.
    expresion_diccionarios=re.compile(s_patrones_mayusculas)
    s_texto=expresion_diccionarios.sub(diccionarios,s_texto)
    conn.send([s_texto,diccionarioEtiquetas])
    conn.close()
    #~ resultados_diccionarios=expresion_diccionarios.finditer(s_texto)
    #~ for resultado in resultados_diccionarios:
        #~ print(resultado.group(0))

def main(args):
    """
    Constantes útiles
    """
    articulos=r"\b(el|la|los|las|un|uno|una|unos|unas|lo|al|del)\b"
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
    s_texto=s_texto_original

    """
    Aquí comienzan los patrones de verdad
    """
    
    """
    Diccionarios
    """
    parent_conn, child_conn = Pipe()
    proceso=Process(target=proceso_diccionarios, args=(s_texto,child_conn,))
    proceso.start()
    s_texto_recv,diccionarioEtiquetas_recv=parent_conn.recv()
    proceso.join(10)
    if proceso.is_alive():
        proceso.terminate()
    else:
        s_texto=s_texto_recv
        for etiqueta in listaEtiquetas:
                diccionarioEtiquetas[etiqueta]+=diccionarioEtiquetas_recv[etiqueta]

    """
    Ubicaciones con "en"
    """
    parent_conn, child_conn = Pipe()
    proceso=Process(target=proceso_en, args=(s_texto,child_conn,))
    proceso.start()
    s_texto_recv,diccionarioEtiquetas_recv=parent_conn.recv()
    proceso.join(10)
    if proceso.is_alive():
        proceso.terminate()
    else:
        s_texto=s_texto_recv
        for etiqueta in listaEtiquetas:
                diccionarioEtiquetas[etiqueta]+=diccionarioEtiquetas_recv[etiqueta]

    """
    Servicios
    """
    s_texto=re_servicios.sub(ne00s00,s_texto)

    """
    Patrones para lugares encontrados con "entre"
    """
    expresion_entre=re.compile(r"("+verbo_estar+"|"+verbo_estar_perfecto+")"+" +entre +[\w ]+")

    """
    Patrones para lugares encontrados con "cerca/lejos"
    """
    expresion_cerca_lejos=re.compile(r"("+verbo_estar+"|"+verbo_estar_perfecto+")"+" +(cerca|lejos) +de +[\w ]+")

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
    expresion_placas = re.compile(r"\b("+placas_1+"|"+placas_2+"|"+placas_3+"|"+placas_4+"|"+placas_5+"|"+placas_6+"|"+placas_7+r")\b")
    s_texto=expresion_placas.sub(ne00m00,s_texto)

    """
    Patrón para correo electrónico
    """
    #Encontré esa expresión regular en internet.
    #https://stackoverflow.com/questions/201323/using-a-regular-expression-to-validate-an-email-address
    #Me pareció una buena explicación. Tiene hasta el autómata con el que generaron la expresión.
    expresion_correo = re.compile(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|" + r'"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])')
    s_texto=expresion_correo.sub(ne00e00,s_texto)

    """
    Patrón de Direcciones IP
    """
    expresion_IPv4 = re.compile(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", re.M)
    s_texto=expresion_IPv4.sub(ne00i00,s_texto)

    """
    Patrón de números telefónicos
    """
    expresion_telefono = re.compile(r"\b(\d{3}[- ]*\d{3}[- ]*\d{4}|\(\d{3}\)\s*\d{3}[- ]*\d{4}|\d{3}[- ]*\d{4})\b")
    s_texto=expresion_telefono.sub(ne00t00,s_texto)

    """
    Patrón de sitios web
    """
    expresion_url = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|\w(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\.com(\.[a-z]+)?")
    s_texto=expresion_url.sub(ne00w00,s_texto)

    """
    Salida
    """
    salida = open(s_nombre_archivo+"_resultadoPre.flg","w",encoding="utf-8")
    salida.write(s_texto)
    salida.close()

    with open(s_nombre_archivo+"_diccionarioEtiquetas.pkl","wb") as pickle_dump:
        pickle.dump(diccionarioEtiquetas,pickle_dump)
    return 0


if __name__ == '__main__':
    """
    Se debe ejecutar el código con un elemento de entrada:
        - el nombre de el archivo que se va a atrabajar
    """
    import sys
    sys.exit(main(sys.argv))
