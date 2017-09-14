
print("     adivinanza     ")
palabrasecreta = "HOLA"

for x in range(3):

 #while  x == True:
     nombre = input("ingrese palabra secreta:")

     if nombre.upper() == palabrasecreta:
         print("felicidades lo adivinastes: ")
         break
     elif nombre.upper() == palabrasecreta:
         print("felicidades lo adivinastes")
         break
     else:
         print("!fallastes¡  intente de nuevo")

