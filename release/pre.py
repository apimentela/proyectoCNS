#!/usr/bin/env python
# -*- coding: utf-8 -*-
jf=open
import re
jn=re.compile
je=re.M
import pickle
jx=pickle.dump
j=["NE00C00","NE00P00","NE00O00","NE00T00","NE00I00","NE00E00","NE00M00","NE00A00","NE00L00","NE00S00","NE00U00","NE00W00"]
W={"NE00C00":[],"NE00P00":[],"NE00O00":[],"NE00T00":[],"NE00I00":[],"NE00E00":[],"NE00M00":[],"NE00A00":[],"NE00L00":[],"NE00S00":[],"NE00U00":[],"NE00W00":[]}
def d(matchobj):
 for z in j:
  if z in matchobj.group(0):
   return matchobj.group(0)
 w=matchobj.group(0).strip()
 t=w.replace(" ","_")
 W["NE00C00"].append(t)
 t=" "+"NE00C00"+" "
 return t
def F(matchobj):
 for z in j:
  if z in matchobj.group(0):
   return matchobj.group(0)
 w=matchobj.group(0).strip()
 t=w.replace(" ","_")
 W["NE00P00"].append(t)
 t=" "+"NE00P00"+" "
 return t
def E(matchobj):
 for z in j:
  if z in matchobj.group(0):
   return matchobj.group(0)
 w=matchobj.group(0).strip()
 t=w.replace(" ","_")
 W["NE00O00"].append(t)
 t=" "+"NE00O00"+" "
 return t
def M(matchobj):
 for z in j:
  if z in matchobj.group(0):
   return matchobj.group(0)
 w=matchobj.group(0).strip()
 t=w.replace(" ","_")
 W["NE00T00"].append(t)
 t=" "+"NE00T00"+" "
 return t
def b(matchobj):
 for z in j:
  if z in matchobj.group(0):
   return matchobj.group(0)
 w=matchobj.group(0).strip()
 t=w.replace(" ","_")
 W["NE00I00"].append(t)
 t=" "+"NE00I00"+" "
 return t
def H(matchobj):
 for z in j:
  if z in matchobj.group(0):
   return matchobj.group(0)
 w=matchobj.group(0).strip()
 t=w.replace(" ","_")
 W["NE00E00"].append(t)
 t=" "+"NE00E00"+" "
 return t
def jW(matchobj):
 for z in j:
  if z in matchobj.group(0):
   return matchobj.group(0)
 w=matchobj.group(0).strip()
 t=w.replace(" ","_")
 W["NE00M00"].append(t)
 t=" "+"NE00M00"+" "
 return t
def jz(matchobj):
 for z in j:
  if z in matchobj.group(0):
   return matchobj.group(0)
 w=matchobj.group(0).strip()
 t=w.replace(" ","_")
 W["NE00A00"].append(t)
 t=" "+"NE00A00"+" "
 return t
def jw(matchobj):
 for z in j:
  if z in matchobj.group(0):
   return matchobj.group(0)
 w=matchobj.group(0).strip()
 t=w.replace(" ","_")
 W["NE00W00"].append(t)
 t=" "+"NE00W00"+" "
 return t
def jt(matchobj):
 for z in j:
  if z in matchobj.group(0):
   return matchobj.group(0)
 w=matchobj.group(0).strip()
 t=w.replace(" ","_")
 W["NE00S00"].append(t)
 t=" "+"NE00S00"+" "
 return t
def jX(matchobj):
 for z in j:
  if z in matchobj.group(0):
   return matchobj.group(0)
 w=matchobj.group(0).strip()
 X=["Messenger","Twitter","Facebook","Internet","Instagram","Google","Skype","Tumblr","Pocket","Telegram","Pinterest","Reddit","Linkedin","Youtube","Síguenos","Inicio"]
 for k in X:
  if w.startswith(k):
   return matchobj.group(0)
 t=w.replace(" ","_")
 W["NE00U00"].append(t)
 t=" "+"NE00U00"+" "
 return t
def jk(args):
 n=r"\b(el|la|los|las|un|uno|una|unos|unas|lo|al|del)\b"
 e=r"\b(el|la|los|las|lo|al|del)\b"
 x=r"\b(mi|mis|nuestro|nuestros|nuestra|nuestras|tu|tus|vuestro|vuestros|vuestra|vuestras|su|sus)\b"
 f=r"\b(mi|mis|nuestro|nuestros|nuestra|nuestras)\b"
 K=r"\b[Ee]st(oy|ás|á|amos|áis|án|aba|abas|aba|ábamos|abais|aban|uve|uviste|uvo|uvimos|uvisteis|uvieron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|é|és|emos|éis|én|uviera|uvieras|uviéramos|uvierais|uvieran|uviese|uvieses|uviese|uviésemos|uvieseis|uviesen|uviere|uvieres|uviere|uviéremos|uviereis|uvieren)\b"
 Y=r"\b[hH](e|as|a|emos|abéis|an|abía|abías|abía|abíamos|abíais|abían|ube|ubiste|ubo|ubimos|ubisteis|ubieron|abré|abrás|abrá|abremos|abréis|abrán|abría|abrías|abríamos|abríais|abrían|aya|ayas|ayamos|ayáis|ayan|ubiera|ubieras|ubiéramos|ubierais|ubieran|ubiese|ubieses|ubiésemos|ubieseis|ubiesen|ubiere|ubieres|ubiéremos|ubiereis|ubieren) +estado\b"
 y=r"\band(o|as|a|amos|áis|an|aba|abas|aba|ábamos|abais|aban|uve|uviste|uvo|uvimos|uvisteis|uvieron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|e|es|emos|éis|en|uviera|uvieras|uviéramos|uvierais|uvieran|uviese|uvieses|uviese|uviésemos|uvieseis|uviesen|uviere|uvieres|uviere|uviéremos|uviereis|uvieren)\b"
 P=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren) +andado\b"
 r=r"\bv(oy|as|a|amos|ais|an|aya|ayas|ayamos|ayáis|ayan)|\b(i|í)(ba|bas|bamos|bais|ban|ré|rás|rá|remos|réis|rán|ría|rías|ríamos|ríais|rían)|\bfu(i|iste|e|imos|isteis|eron|era|eras|éramos|erais|eran|ese|eses|ésemos|eseis|esen|ere|eres|éremos|ereis|eren)\b"
 R=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren) +ido\b"
 G=r"\bviaj(o|as|a|amos|áis|an|aba|abas|aba|ábamos|abais|aban|é|aste|ó|amos|asteis|aron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|e|es|emos|éis|en|ara|aras|áramos|arais|aran|ase|ases|ásemos|aseis|asen|are|ares|áremos|areis|aren)\b"
 a=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren) +viajado\b"
 h=args[1]
 with jf(h,"r",encoding="utf-8")as archivo:
  S=archivo.read()
 A=S
 m=e+r"( +[^A-ZÁÉÍÓÚÑ\W]+ +)*?"
 p=r"(([A-ZÁÉÍÓÚÑ]+[ \b]+)+|([A-ZÁÉÍÓÚÑ][^A-ZÁÉÍÓÚÑ\W]+[ \b]+)+)"
 o=jn(r"(?<=\b[Ee]n )+("+m+p+"|"+p+")")
 A=o.sub(jX,A)
 C=jn(re_servicios)
 N=C.finditer(A)
 A=C.sub(jt,A)
 u=jn(r"("+K+"|"+Y+")"+" +entre +[\w ]+")
 T=jn(r"("+K+"|"+Y+")"+" +(cerca|lejos) +de +[\w ]+")
 U=r"[A-HJ-NPR-Z]{3}-?[0-9]{2}-?[0-9]{2}"
 g=r"[A-HJ-NPR-Z]{3}-?[0-9]{3}-?[A-HJ-NPR-Z]"
 I=r"[A-HJ-NPR-Z]-?[0-9]{2,3}-?[A-HJ-NPR-Z]{3}"
 V=r"[0-9]{3}-?[A-HJ-NPR-Z]{3}"
 v=r"[A-HJ-NPR-Z]{2}-?[0-9]{2}-?[0-9]{3}"
 s=r"[0-9]-?[A-HJ-NPR-Z]-?[0-9]{2}-?[A-HJ-NPR-Z]{2}"
 q=r"[0-9]-?[A-HJ-NPR-Z]-?[0-9]-?[A-HJ-NPR-Z]{3}"
 Q=jn(r"\b("+U+"|"+g+"|"+I+"|"+V+"|"+v+"|"+s+"|"+q+")\b")
 A=Q.sub(jW,A)
 L=jn(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"+r'"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])')
 A=L.sub(H,A)
 O=jn(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",je)
 A=O.sub(b,A)
 B=jn(r"\b(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})\b")
 A=B.sub(M,A)
 D=jn(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\.com(\.[a-z]+)?")
 A=D.sub(jw,A)
 """
    Salida
    """
 c=jf("resultadoPre.flg","a+",encoding="utf-8")
 c.write(A)
 c.close()
 with jf("diccionarioEtiquetas.pkl","wb")as pickle_dump:
  jx(W,pickle_dump)
 return 0
if __name__=='__main__':
 import sys
 sys.exit(jk(sys.argv))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

