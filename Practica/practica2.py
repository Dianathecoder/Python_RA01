
import json

"""horarios = {
    
     'María':  ('08:30', '16:00'),
     'Juan':   ('09:00', '17:00'),
     'Lucía':  ('07:00', '15:00'),
     'Diego':  ('10:00', '18:00'),
     'Ana':    ('08:00', '14:00'),
     'Raúl':   ('12:00', '20:00'),
    
}"""



"""def escribirJSON():
    with open('horarios.json', 'w', encoding='utf-8') as h:
        json.dump(horarios, h, indent=4)
    print("Se ha convertido correctamente") """


def leerJSON():
# Leer JSON desde un archivo
    with open('horarios.json', encoding='utf-8') as f:
       datos_cargados = json.load(f)
       return datos_cargados

def mostrar_registros():
   horarios = leerJSON()

   for i,(nombre,horas) in enumerate(horarios.items(), start=1):
      print(f"{i}. {nombre}: entrada: {horas[0]}  salida: {horas[1]}")
     

#Validar la entrada – Mejora contar_entradas() para aceptar horas con minutos ('08:30').
def Validar_entrada(hora_str):
    try:
        partes = hora_str.split(":")#hora_str es :
        if len(partes) == 1:##sino hay minutos se ausme que sera un 0
            horas = int(partes[0])
            minutos = 0

        else:#si la hota horas y minutos
            horas = int(partes[0])
            minutos= int(partes[1])


        if 0 <= horas < 24 and 0<= minutos <60:  # comprobamos que estén dentro de las horas
            return horas * 60 + minutos
        else:
           return SystemError
        
    except ValueError:
        print("Error al validar la hora")
        return None



def contar_entrada():
    horarios = leerJSON
    contador_entradas: 0
    try:

        hora_entrada=int(input("Introduce la hora de entrada(HH:MM):"))
        hora_introducida = Validar_entrada(hora_entrada)

        
        for nombre, (entrada,salida) in horarios.items():#Recorremos las tupla, nombre es la clave, entrada y salida los valores

            validar_entrada = Validar_entrada(entrada)
        
            if validar_entrada== hora_introducida:
               print("La hora de entrada es la correcta")
               contador_entradas+1
            else:
               print("La hora de entrada es a las {hora_introducida}")

        print(f"\nA las {hora_entrada} , {contador_entradas} empleados ya han llegado.\n")    

    except ValueError:
        print("Tienes que introducir un numero valido")


def menu():
  
    while True:
        print("========== MENÚ ==========")
        print("1) Mostrar registros")
        print("2) Contar entradas")
        print("3) Salir")
        opcion = input("Elige una opción (1-3): ").strip()
 
        if opcion == '1':
            mostrar_registros()
        elif opcion == '2':
            contar_entrada()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")
 
 
if __name__ == '__main__':
    leerJSON()
    menu()

