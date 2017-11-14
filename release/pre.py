#!/usr/bin/env python
# -*- coding: utf-8 -*-
z=open
import re
E=re.compile
g=re.M
import pickle
R=pickle.dump
from tags import *
def b(args):
 m=r"\b(el|la|los|las|un|uno|una|unos|unas|lo|al|del)\b"
 p=r"\b(el|la|los|las|lo|al|del)\b"
 c=r"\b(mi|mis|nuestro|nuestros|nuestra|nuestras|tu|tus|vuestro|vuestros|vuestra|vuestras|su|sus)\b"
 i=r"\b(mi|mis|nuestro|nuestros|nuestra|nuestras)\b"
 d=r"\b[Ee]st(oy|ás|á|amos|áis|án|aba|abas|aba|ábamos|abais|aban|uve|uviste|uvo|uvimos|uvisteis|uvieron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|é|és|emos|éis|én|uviera|uvieras|uviéramos|uvierais|uvieran|uviese|uvieses|uviese|uviésemos|uvieseis|uviesen|uviere|uvieres|uviere|uviéremos|uviereis|uvieren)\b"
 o=r"\b[hH](e|as|a|emos|abéis|an|abía|abías|abía|abíamos|abíais|abían|ube|ubiste|ubo|ubimos|ubisteis|ubieron|abré|abrás|abrá|abremos|abréis|abrán|abría|abrías|abríamos|abríais|abrían|aya|ayas|ayamos|ayáis|ayan|ubiera|ubieras|ubiéramos|ubierais|ubieran|ubiese|ubieses|ubiésemos|ubieseis|ubiesen|ubiere|ubieres|ubiéremos|ubiereis|ubieren) +estado\b"
 T=r"\band(o|as|a|amos|áis|an|aba|abas|aba|ábamos|abais|aban|uve|uviste|uvo|uvimos|uvisteis|uvieron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|e|es|emos|éis|en|uviera|uvieras|uviéramos|uvierais|uvieran|uviese|uvieses|uviese|uviésemos|uvieseis|uviesen|uviere|uvieres|uviere|uviéremos|uviereis|uvieren)\b"
 Y=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren) +andado\b"
 y=r"\bv(oy|as|a|amos|ais|an|aya|ayas|ayamos|ayáis|ayan)|\b(i|í)(ba|bas|bamos|bais|ban|ré|rás|rá|remos|réis|rán|ría|rías|ríamos|ríais|rían)|\bfu(i|iste|e|imos|isteis|eron|era|eras|éramos|erais|eran|ese|eses|ésemos|eseis|esen|ere|eres|éremos|ereis|eren)\b"
 H=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren) +ido\b"
 X=r"\bviaj(o|as|a|amos|áis|an|aba|abas|aba|ábamos|abais|aban|é|aste|ó|amos|asteis|aron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|e|es|emos|éis|en|ara|aras|áramos|arais|aran|ase|ases|ásemos|aseis|asen|are|ares|áremos|areis|aren)\b"
 v=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren) +viajado\b"
 l=args[1]
 with z(l,"r",encoding="utf-8")as archivo:
  u=archivo.read()
 W=u
 F=p+r"( +[^A-ZÁÉÍÓÚÑ\W]+ +)*?"
 x=r"(([A-ZÁÉÍÓÚÑ]+[ \b]+)+|([A-ZÁÉÍÓÚÑ][^A-ZÁÉÍÓÚÑ\W]+[ \b]+)+)"
 q=E(r"(?<=\b[Ee]n )+("+F+x+"|"+x+")")
 W=q.sub(ne00u00,W)
 I=E(r"("+d+"|"+o+")"+" +entre +[\w ]+")
 k=E(r"("+d+"|"+o+")"+" +(cerca|lejos) +de +[\w ]+")
 S=r"[A-HJ-NPR-Z]{3}-?[0-9]{2}-?[0-9]{2}"
 r=r"[A-HJ-NPR-Z]{3}-?[0-9]{3}-?[A-HJ-NPR-Z]"
 D=r"[A-HJ-NPR-Z]-?[0-9]{2,3}-?[A-HJ-NPR-Z]{3}"
 O=r"[0-9]{3}-?[A-HJ-NPR-Z]{3}"
 M=r"[A-HJ-NPR-Z]{2}-?[0-9]{2}-?[0-9]{3}"
 Q=r"[0-9]-?[A-HJ-NPR-Z]-?[0-9]{2}-?[A-HJ-NPR-Z]{2}"
 P=r"[0-9]-?[A-HJ-NPR-Z]-?[0-9]-?[A-HJ-NPR-Z]{3}"
 K=E(r"\b("+S+"|"+r+"|"+D+"|"+O+"|"+M+"|"+Q+"|"+P+")\b")
 W=K.sub(ne00m00,W)
 J=E(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"+r'"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])')
 a=J.finditer(W)
 L=[]
 for t in a:
  L.append(t.group(0))
 with z("lista_correos.pkl","wb")as f:
  R(L,f)
 W=J.sub(ne00e00,W)
 h=E(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",g)
 W=h.sub(ne00i00,W)
 f=E(r"\b(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})\b")
 W=f.sub(ne00t00,W)
 B=E(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
 W=B.sub(ne00w00,W)
 V=z("resultadoPre.flg","a+",encoding="utf-8")
 V.write(W)
 V.close()
 return 0
if __name__=='__main__':
 import sys
 sys.exit(b(sys.argv))
