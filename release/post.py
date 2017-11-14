#!/usr/bin/env python
# -*- coding: utf-8 -*-
n=open
M=enumerate
import re
import os
import pickle
I=pickle.load
def l(args):
 i=["NE00C00","NE00P00","NE00O00","NE00T00","NE00I00","NE00E00","NE00M00","NE00A00","NE00L00","NE00S00","NE00U00"]
 D=[]
 x=args[1]
 with n(x,"r",encoding="utf-8")as entrada:
  f=entrada.readlines()
 with n("lista_correos.pkl","rb")as pkl:
  j=I(pkl)
 for O,k in M(f):
  k=k.strip()
  for b in i:
   if b=="NE00E00" and b in k:
    k=k.replace(b,j.popleft())
    k=k.replace(" Z "," "+b+" ")
    f[O]=""+k+"\n"
   if b in k:
    k=k.replace(""+b+"_","")
    k=k.replace(" Z "," "+b+" ")
    f[O]=""+k+"\n"
 h=n("resultado.flg","a+",encoding="utf-8")
 for k in f:
  h.write(k)
 h.close()
 os.remove("lista_correos.pkl")
 os.remove("resultadoPre.flg")
 os.remove("resultadoFreeling.flg")
 return 0

if __name__=='__main__':
 import sys
 sys.exit(l(sys.argv))

