#!/usr/bin/env python
# -*- coding: utf-8 -*-
y=open
F=True
import subprocess
c=subprocess.call
import re
def p(args):
 s=args[1]
 with y(s,"r",encoding="utf-8")as entrada:
  W=y("resultadoFreeling.flg","a+",encoding="utf-8")
  c("C:\\freeling\\bin\\analyzer.bat -f es.cfg",stdin=entrada,stdout=W,shell=F)
  W.close()
 return 0
if __name__=='__main__':
 import sys
 sys.exit(p(sys.argv))
