#!/usr/bin/env python
# -*- coding: utf-8 -*-
g=open
P=True
import subprocess
K=subprocess.call
import re
def V(args):
 I=args[1]
 with g(I,"r",encoding="utf-8")as entrada:
  i=g("resultadoFreeling.flg","a+",encoding="utf-8")
  K("docker run -i --rm freeling analyzer_client 172.17.0.2:50005",stdin=entrada,stdout=i,shell=P)
  i.close()
 return 0
if __name__=='__main__':
 import sys
 sys.exit(V(sys.argv))
