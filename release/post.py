#!/usr/bin/env python
# -*- coding: utf-8 -*-
i=open
u=enumerate
import re
import os
T=os.remove
import pickle
H=pickle.load
d=["NE00C00","NE00P00","NE00O00","NE00T00","NE00I00","NE00E00","NE00M00","NE00A00","NE00L00","NE00S00","NE00U00","NE00W00","NE00C01"]
def e(args):
 C=[]
 W=args[1]
 G=args[2]
 with i(W+"_resultadoFreeling.flg","r",encoding="utf-8")as entrada:
  s=entrada.readlines()
 with i(W+"_diccionarioEtiquetas.pkl","rb")as pickle_file:
  m=H(pickle_file)
 for b,t in u(s):
  t=t.strip()
  for w in d:
   if w in t:
    t=t.replace(w,m[w].pop(0))
    t=t.replace(" Z "," "+w[:-1]+"0 ")
    s[b]=""+t+"\n"
 n=i(G,"w",encoding="utf-8")
 for t in s:
  n.write(t)
 n.close()
 T(W+"_diccionarioEtiquetas.pkl")
 T(W+"_resultadoPre.flg")
 T(W+"_resultadoFreeling.flg")
 return 0
"""
        if len(S_tags) == 4: #cuando no mide 4, es que algo pasó con freeling. El chiste es que no tiene etiqueta, o forma, o algo importante.
            s_token_tag = S_tags[0] +"/"+ S_tags[2] #el 1er elemento es la palabra, y el 3er elemento el tag. Los unimos con una diagonal
            S_texto_etiquetado_token_tag.append(s_token_tag)
    salida = open("textoEtiquetado.txt", "w",encoding="utf-8") #No sirve usar with open, cuando queremos escribir archivos que no existen. Por eso lo hago así. (Windows...)
    for word in S_texto_etiquetado_token_tag:
        salida.write(word + " ")#Escribimos la palabra/tag seguido de un espacio.
    salida.close()
"""
if __name__=='__main__':
 import sys
 sys.exit(e(sys.argv))
