### Variables 
var_string = "hola"
var_int = 5
var_string_int = str(var_int)
var_bool = False

# Concatenación

print( var_string, var_int,var_bool)
print(type(var_string_int))

print(len(var_string))
print("Información", var_string)

# Variables en una sola línea

name, surname, edad = "Alejandro", "Gomez" , 41
print("Hola:", name, "Edad:", edad)

# Inputs
input_name = input("Cual es tu nombre") 
print("Hola", input_name)

texto = "hola"
numero = 2
suma = texto + numero # Fallará 
print(suma)

