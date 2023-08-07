nombre = "Paco"
apellido = "Delgado"
nombre_c = nombre + " " + apellido
print(nombre_c)
quote = "I'm Paco"
print(quote)
quote2 = 'He said "I become Death, the Destroyer of Worlds"'
print(quote2)

#format
template = "Hola, mi nombre es " + nombre + " y mi apellido es " + apellido + ", y quiero que sepas que " + quote2
print(template)
template= "Hola, mi nombre es {} y mi apellido es {}, y quiero que sepas que {}".format(nombre, apellido, quote2)
print(template)
template = f"Hola, mi nombre es {nombre} y mi apellido es {apellido}, y quiero que sepas que {quote2}"
print(template)