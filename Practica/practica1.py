

#Variables incializar
salida_temprana= 20
contador_entradas =0
nombre_persona_temprana=""


#Numero de trabajadores
trabajadores = input("Bienvenido. Numero de  trabajadores: ")

#almacenar la hora de referecia
num_trabajadores = int(trabajadores)
print(trabajadores)
hora_referencia=int(input("Selecciona la hora de referencia que quiere aplicar(0-23):"))
print(hora_referencia)
 


#Bucle con contador 5 donde se introduce los datos
x=5
while num_trabajadores  > 0:#validamos si hay empleados
    num_trabajadores = num_trabajadores-1
    nombre_empleado= input("nombre empleado:")

    hora_entrada=int(input("hora de entrada(0-23):"))
    hora_salida=int(input("hora de salida(0-23):"))


#Validar hora de entrada y salida
    if not (0 <= hora_entrada <= 23) or not (0 <= hora_salida <= 23):
      print("La hora esta fuera del rango.")
      continue#permite repetirlo sin avanzar al contador

#validar si la entrada no supera a la salida
    if hora_entrada<hora_salida:
      print("La hora de salida deber ser mayor que la de la entrada")
      continue

#Contar los empleados que llegaron antes a la hora de referencia
    if hora_entrada<=hora_referencia:
       contador_entradas +1


#Para saber cuantos empleados llegaron a la hora más teamprana
    if hora_entrada <=hora_referencia:
       salida_temprana = hora_salida
       nombre_persona_temprana= nombre_empleado
    

    
    num_trabajadores += 1 


print("Numeros de empleados que entraron antes o la hora de referencia: {contador_entradas} ")
print("Persona que llego más teamprano: Nombre{nombre_persona_temprana} Hora de salida: {salida_temprana}")





