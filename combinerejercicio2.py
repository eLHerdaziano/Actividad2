#!/usr/bin/env python

import sys

subproblema=None
Lista = []


for linea in sys.stdin:
    citado,citante = linea.split("\t")
    if subproblema == None:
        subproblema = citado
    if subproblema == citado:
        Lista.append(citante)
    else:
        print("%s\t%s" % (subproblema,",".join(Lista)))
        Lista=[]


print("%s\t%s" % (subproblema,",".join(Lista)))