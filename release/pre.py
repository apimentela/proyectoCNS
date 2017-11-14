#!/usr/bin/env python
# -*- coding: utf-8 -*-
at=open
import re
aQ=re.compile
aH=re.M
import pickle
al=pickle.dump
a=["NE00C00","NE00P00","NE00O00","NE00T00","NE00I00","NE00E00","NE00M00","NE00A00","NE00L00","NE00S00","NE00U00","NE00W00"]
def g(matchobj):
 for s in a:
  if s in matchobj.group(0):
   return matchobj.group(0)
 o=matchobj.group(0).strip()
 G=o.replace(" ","_")
 G=" "+"NE00C00_"+G+" "
 return G
def b(matchobj):
 for s in a:
  if s in matchobj.group(0):
   return matchobj.group(0)
 o=matchobj.group(0).strip()
 G=o.replace(" ","_")
 G=" "+"NE00P00_"+G+" "
 return G
def d(matchobj):
 for s in a:
  if s in matchobj.group(0):
   return matchobj.group(0)
 o=matchobj.group(0).strip()
 G=o.replace(" ","_")
 G=" "+"NE00O00_"+G+" "
 return G
def q(matchobj):
 for s in a:
  if s in matchobj.group(0):
   return matchobj.group(0)
 o=matchobj.group(0).strip()
 G=o.replace(" ","_")
 G=" "+"NE00T00_"+G+" "
 return G
def M(matchobj):
 for s in a:
  if s in matchobj.group(0):
   return matchobj.group(0)
 o=matchobj.group(0).strip()
 G=o.replace(" ","_")
 G=" "+"NE00I00_"+G+" "
 return G
def K(matchobj):
 for s in a:
  if s in matchobj.group(0):
   return matchobj.group(0)
 G=" "+"NE00E00"+" "
 return G
def i(matchobj):
 for s in a:
  if s in matchobj.group(0):
   return matchobj.group(0)
 o=matchobj.group(0).strip()
 G=o.replace(" ","_")
 G=" "+"NE00M00_"+G+" "
 return G
def N(matchobj):
 for s in a:
  if s in matchobj.group(0):
   return matchobj.group(0)
 o=matchobj.group(0).strip()
 G=o.replace(" ","_")
 G=" "+"NE00A00_"+G+" "
 return G
def A(matchobj):
 for s in a:
  if s in matchobj.group(0):
   return matchobj.group(0)
 o=matchobj.group(0).strip()
 G=o.replace(" ","_")
 G=" "+"NE00W00_"+G+" "
 return G
def ao(matchobj):
 for s in a:
  if s in matchobj.group(0):
   return matchobj.group(0)
 o=matchobj.group(0).strip()
 G=o.replace(" ","_")
 G=" "+"NE00S00_"+G+" "
 return G
def aG(matchobj):
 for s in a:
  if s in matchobj.group(0):
   return matchobj.group(0)
 o=matchobj.group(0).strip()
 c=["Messenger","Twitter","Facebook","Internet","Instagram","Google","Skype","Tumblr","Pocket","Telegram","Pinterest","Reddit","Linkedin","Youtube","Síguenos","Inicio"]
 for Q in c:
  if o.startswith(Q):
   return matchobj.group(0)
 G=o.replace(" ","_")
 G=" "+"NE00U00_"+G+" "
 return G
def ac(args):
 H=r"\b(el|la|los|las|un|uno|una|unos|unas|lo|al|del)\b"
 l=r"\b(el|la|los|las|lo|al|del)\b"
 t=r"\b(mi|mis|nuestro|nuestros|nuestra|nuestras|tu|tus|vuestro|vuestros|vuestra|vuestras|su|sus)\b"
 E=r"\b(mi|mis|nuestro|nuestros|nuestra|nuestras)\b"
 W=r"\b[Ee]st(oy|ás|á|amos|áis|án|aba|abas|aba|ábamos|abais|aban|uve|uviste|uvo|uvimos|uvisteis|uvieron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|é|és|emos|éis|én|uviera|uvieras|uviéramos|uvierais|uvieran|uviese|uvieses|uviese|uviésemos|uvieseis|uviesen|uviere|uvieres|uviere|uviéremos|uviereis|uvieren)\b"
 J=r"\b[hH](e|as|a|emos|abéis|an|abía|abías|abía|abíamos|abíais|abían|ube|ubiste|ubo|ubimos|ubisteis|ubieron|abré|abrás|abrá|abremos|abréis|abrán|abría|abrías|abríamos|abríais|abrían|aya|ayas|ayamos|ayáis|ayan|ubiera|ubieras|ubiéramos|ubierais|ubieran|ubiese|ubieses|ubiésemos|ubieseis|ubiesen|ubiere|ubieres|ubiéremos|ubiereis|ubieren) +estado\b"
 e=r"\band(o|as|a|amos|áis|an|aba|abas|aba|ábamos|abais|aban|uve|uviste|uvo|uvimos|uvisteis|uvieron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|e|es|emos|éis|en|uviera|uvieras|uviéramos|uvierais|uvieran|uviese|uvieses|uviese|uviésemos|uvieseis|uviesen|uviere|uvieres|uviere|uviéremos|uviereis|uvieren)\b"
 C=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren) +andado\b"
 z=r"\bv(oy|as|a|amos|ais|an|aya|ayas|ayamos|ayáis|ayan)|\b(i|í)(ba|bas|bamos|bais|ban|ré|rás|rá|remos|réis|rán|ría|rías|ríamos|ríais|rían)|\bfu(i|iste|e|imos|isteis|eron|era|eras|éramos|erais|eran|ese|eses|ésemos|eseis|esen|ere|eres|éremos|ereis|eren)\b"
 I=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren) +ido\b"
 y=r"\bviaj(o|as|a|amos|áis|an|aba|abas|aba|ábamos|abais|aban|é|aste|ó|amos|asteis|aron|aré|arás|ará|aremos|aréis|arán|aría|arías|aríamos|arían|e|es|emos|éis|en|ara|aras|áramos|arais|aran|ase|ases|ásemos|aseis|asen|are|ares|áremos|areis|aren)\b"
 w=r"\b(he|has|ha|hemos|habéis|han|había|habías|había|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren) +viajado\b"
 v=args[1]
 with at(v,"r",encoding="utf-8")as archivo:
  D=archivo.read()
 r=D
 j=l+r"( +[^A-ZÁÉÍÓÚÑ\W]+ +)*?"
 O=r"(([A-ZÁÉÍÓÚÑ]+[ \b]+)+|([A-ZÁÉÍÓÚÑ][^A-ZÁÉÍÓÚÑ\W]+[ \b]+)+)"
 S=aQ(r"(?<=\b[Ee]n )+("+j+O+"|"+O+")")
 r=S.sub(aG,r)
 Y=aQ(r"("+W+"|"+J+")"+" +entre +[\w ]+")
 B=aQ(r"("+W+"|"+J+")"+" +(cerca|lejos) +de +[\w ]+")
 f=r"[A-HJ-NPR-Z]{3}-?[0-9]{2}-?[0-9]{2}"
 U=r"[A-HJ-NPR-Z]{3}-?[0-9]{3}-?[A-HJ-NPR-Z]"
 L=r"[A-HJ-NPR-Z]-?[0-9]{2,3}-?[A-HJ-NPR-Z]{3}"
 V=r"[0-9]{3}-?[A-HJ-NPR-Z]{3}"
 x=r"[A-HJ-NPR-Z]{2}-?[0-9]{2}-?[0-9]{3}"
 p=r"[0-9]-?[A-HJ-NPR-Z]-?[0-9]{2}-?[A-HJ-NPR-Z]{2}"
 P=r"[0-9]-?[A-HJ-NPR-Z]-?[0-9]-?[A-HJ-NPR-Z]{3}"
 X=aQ(r"\b("+f+"|"+U+"|"+L+"|"+V+"|"+x+"|"+p+"|"+P+")\b")
 r=X.sub(i,r)
 k=aQ(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"+r'"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])')
 T=k.finditer(r)
 h=[]
 for n in T:
  h.append(n.group(0))
 with at("lista_correos.pkl","wb")as f:
  al(h,f)
 r=k.sub(K,r)
 m=aQ(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",aH)
 r=m.sub(M,r)
 u=aQ(r"\b(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})\b")
 r=u.sub(q,r)
 R=aQ(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
 r=R.sub(A,r)
 F=at("resultadoPre.flg","a+",encoding="utf-8")
 F.write(r)
 F.close()
 return 0
if __name__=='__main__':
 import sys
 sys.exit(ac(sys.argv))
