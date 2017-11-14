#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
c=["NE00C00","NE00P00","NE00O00","NE00T00","NE00I00","NE00E00","NE00M00","NE00A00","NE00L00","NE00S00","NE00U00","NE00W00"]
def A(matchobj):
 for U in c:
  if U in matchobj.group(0):
   return matchobj.group(0)
 u=matchobj.group(0).strip()
 o=u.replace(" ","_")
 o=" "+"NE00C00_"+o+" "
 return o
def F(matchobj):
 for U in c:
  if U in matchobj.group(0):
   return matchobj.group(0)
 u=matchobj.group(0).strip()
 o=u.replace(" ","_")
 o=" "+"NE00P00_"+o+" "
 return o
def h(matchobj):
 for U in c:
  if U in matchobj.group(0):
   return matchobj.group(0)
 u=matchobj.group(0).strip()
 o=u.replace(" ","_")
 o=" "+"NE00O00_"+o+" "
 return o
def L(matchobj):
 for U in c:
  if U in matchobj.group(0):
   return matchobj.group(0)
 u=matchobj.group(0).strip()
 o=u.replace(" ","_")
 o=" "+"NE00T00_"+o+" "
 return o
def N(matchobj):
 for U in c:
  if U in matchobj.group(0):
   return matchobj.group(0)
 u=matchobj.group(0).strip()
 o=u.replace(" ","_")
 o=" "+"NE00I00_"+o+" "
 return o
def a(matchobj):
 for U in c:
  if U in matchobj.group(0):
   return matchobj.group(0)
 o=" "+"NE00E00"+" "
 return o
def e(matchobj):
 for U in c:
  if U in matchobj.group(0):
   return matchobj.group(0)
 u=matchobj.group(0).strip()
 o=u.replace(" ","_")
 o=" "+"NE00M00_"+o+" "
 return o
def D(matchobj):
 for U in c:
  if U in matchobj.group(0):
   return matchobj.group(0)
 u=matchobj.group(0).strip()
 o=u.replace(" ","_")
 o=" "+"NE00A00_"+o+" "
 return o
def n(matchobj):
 for U in c:
  if U in matchobj.group(0):
   return matchobj.group(0)
 u=matchobj.group(0).strip()
 o=u.replace(" ","_")
 o=" "+"NE00W00_"+o+" "
 return o
def C(matchobj):
 for U in c:
  if U in matchobj.group(0):
   return matchobj.group(0)
 u=matchobj.group(0).strip()
 o=u.replace(" ","_")
 o=" "+"NE00S00_"+o+" "
 return o
def Y(matchobj):
 for U in c:
  if U in matchobj.group(0):
   return matchobj.group(0)
 u=matchobj.group(0).strip()
 m=["Messenger","Twitter","Facebook","Internet","Instagram","Google","Skype","Tumblr","Pocket","Telegram","Pinterest","Reddit","Linkedin","Youtube","Síguenos","Inicio"]
 for k in m:
  if u.startswith(k):
   return matchobj.group(0)
 o=u.replace(" ","_")
 o=" "+"NE00U00_"+o+" "
 return o
