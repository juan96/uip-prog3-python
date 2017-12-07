
#
import re

pat = '[a-z1-9]||[1-9a-z]||[a-z]\w'
palabras = ['rap them' , 'tapeth' , 'apth' , 'wrap/try' , 'sap try' , '87ap9th' , 'apothecary']
pat1 = '[.AA]\S'
palabras1 = ['aleht' , 'happy them' , 'tarpth' , 'apt' , 'peth' , 'tarreth' , 'ddpdg']


for palabra in palabras:
    if re.search(pat, palabra):
                print("La palabra " + palabra + " cumple.")

    else:
                print("La palabra " + palabra + " no cumple.")

for palabra1 in palabras1:
    if re.search(pat1, palabra1):
                print("La palabra " + palabra1 + " cumple.")

    else:
                print("La palabra " + palabra1 + " no cumple.")