#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def ne00u00(matchobj):
	texto_encontrado = matchobj.group(0).strip()
	texto_nuevo = texto_encontrado.replace(" ","_")
	texto_nuevo = "NE00C00_"+texto_nuevo+" "
	return texto_nuevo
