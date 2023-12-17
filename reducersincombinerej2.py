#!/usr/bin/env python
  
import sys

subproblema=None
Lista_Citantes=[]


for linea in sys.stdin:
    citado,citantes = linea.split("\t")
    if subproblema == None:
        subproblema = citado
    if subproblema == citado:
        Lista_Citantes.append(citantes)
    else:
        Lista_Citantes=sorted(Lista_Citantes)
        print("%s\t%s" % (subproblema,",".join(Lista_Citantes)))
        Lista_Citantes=[]
        
print("%s\t%s" % (subproblema,",".join(Lista_Citantes)))
