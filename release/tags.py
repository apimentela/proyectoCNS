#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
Y=["NE00C00","NE00P00","NE00O00","NE00T00","NE00I00","NE00E00","NE00M00","NE00A00","NE00L00","NE00S00","NE00U00"]
def h(matchobj):
 for X in Y:
  if X in matchobj.group(0):
   return matchobj.group(0)
 s=matchobj.group(0).strip()
 u=s.replace(" ","_")
 u=" "+"NE00C00_"+u+" "
 return u
def w(matchobj):
 for X in Y:
  if X in matchobj.group(0):
   return matchobj.group(0)
 s=matchobj.group(0).strip()
 u=s.replace(" ","_")
 u=" "+"NE00P00_"+u+" "
 return u
def C(matchobj):
 for X in Y:
  if X in matchobj.group(0):
   return matchobj.group(0)
 s=matchobj.group(0).strip()
 u=s.replace(" ","_")
 u=" "+"NE00O00_"+u+" "
 return u
def F(matchobj):
 for X in Y:
  if X in matchobj.group(0):
   return matchobj.group(0)
 s=matchobj.group(0).strip()
 u=s.replace(" ","_")
 u=" "+"NE00T00_"+u+" "
 return u
def n(matchobj):
 for X in Y:
  if X in matchobj.group(0):
   return matchobj.group(0)
 s=matchobj.group(0).strip()
 u=s.replace(" ","_")
 u=" "+"NE00I00_"+u+" "
 return u
def x(matchobj):
 for X in Y:
  if X in matchobj.group(0):
   return matchobj.group(0)
 u=" "+"NE00E00"+" "
 return u
def o(matchobj):
 for X in Y:
  if X in matchobj.group(0):
   return matchobj.group(0)
 s=matchobj.group(0).strip()
 u=s.replace(" ","_")
 u=" "+"NE00M00_"+u+" "
 return u
def E(matchobj):
 for X in Y:
  if X in matchobj.group(0):
   return matchobj.group(0)
 s=matchobj.group(0).strip()
 u=s.replace(" ","_")
 u=" "+"NE00A00_"+u+" "
 return u
def L(matchobj):
 for X in Y:
  if X in matchobj.group(0):
   return matchobj.group(0)
 s=matchobj.group(0).strip()
 u=s.replace(" ","_")
 u=" "+"NE00L00_"+u+" "
 return u
def J(matchobj):
 for X in Y:
  if X in matchobj.group(0):
   return matchobj.group(0)
 s=matchobj.group(0).strip()
 u=s.replace(" ","_")
 u=" "+"NE00S00_"+u+" "
 return u
def b(matchobj):
 for X in Y:
  if X in matchobj.group(0):
   return matchobj.group(0)
 s=matchobj.group(0).strip()
 i=["Messenger","Twitter","Facebook","Internet","Instagram","Google","Skype","Tumblr","Pocket","Telegram","Pinterest","Reddit","Linkedin","Youtube","Síguenos","Inicio"]
 for m in i:
  if s.startswith(m):
   return matchobj.group(0)
 u=s.replace(" ","_")
 u=" "+"NE00U00_"+u+" "
 return u

