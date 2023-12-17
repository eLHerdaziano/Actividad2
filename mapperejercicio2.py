#!/usr/bin/env python

import sys
primera_linea=True

for linea in sys.stdin:
  if primera_linea == True:
    primera_linea = False
    continue
  else:

    citante,citado = linea.split(",")

    print("%s\t%s" % (citado, citante))
