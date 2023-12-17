#!/usr/bin/env python
  
import sys

subproblema=None
Lista_Citantes=[]
Lista_Total_Citantes=[]

for linea in sys.stdin:
    citado,citantes_str = linea.split("\t")
    citantes=citantes_str.split(",")
    if subproblema == None:
        subproblema = citado
    if subproblema == citado:
        Lista_Total_Citantes.extend(citantes)
    else:
        print("%s\t%s" % (subproblema,",".join(Lista_Total_Citantes)))
        Lista_Total_Citantes=[]
        
print("%s\t%s" % (subproblema,",".join(Lista_Total_Citantes)))