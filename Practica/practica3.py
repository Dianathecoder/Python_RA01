
import csv;



class RegistroHorario:


    def __init__(self, empleado: str, dia: str, entrada: int, salida: int):
        self.empleado = empleado
        self.dia = dia
        self.entrada = entrada
        self.salida = salida

#Duracion del turno
    def duracion(self) -> int:
        """Devuelve la cantidad de horas trabajadas en este registro"""
        return self.salida - self.entrada
    

def convertir_hora_a_decimal(hora_str):
    """Convierte 'HH:MM' a horas decimales"""
    h, m = map(int, hora_str.split(':'))
    return h + m / 60


def leerregistro():
    registros = []
    with open('horarios.csv', newline='', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',', quotechar='"')
        next(lector)  # saltar cabecera
        for fila in lector:
           if not fila or len(fila) < 4:
                continue
        # Cada fila es una lista de cadenas: [nombre, dia, entrada, salida]
           nombre_empleado,dia,hora_entrada,hora_salida= fila
        # Convertimos las horas a enteros
           hora_entrada = convertir_hora_a_decimal(hora_entrada)
           salida=  convertir_hora_a_decimal(hora_salida)
           registro = RegistroHorario(nombre_empleado, dia, hora_entrada, salida)
           registros.append(registro)
    print(f"Se han leído {len(registros)} registros")   
    return registros


def coleccionregistro(registros):

    empleados_por_dia = {}
    for registro in registros:
    # Creamos el conjunto para el día si no existe
       if registro.dia not in empleados_por_dia:
        empleados_por_dia[registro.dia] = set()
    # Añadimos el empleado al conjunto del día
        empleados_por_dia[registro.dia].add(registro.empleado)

# Mostrar empleados por día
    for dia, empleados in empleados_por_dia.items():
        print(f"{dia}: {empleados}")

    # lista de empleados que han trabajado al menos 8 horas en algún día
    empleados_turno_largo = {r.empleado for r in registros if r.duracion() >= 8}
    print(f"Empleados con turno largo: {empleados_turno_largo}")



    # Operaciones con conjuntos ejemplo lunes y martes
    if 'Lunes' in empleados_por_dia and 'Martes' in empleados_por_dia:
        union = empleados_por_dia['Lunes'] | empleados_por_dia['Martes']
        interseccion = empleados_por_dia['Lunes'] & empleados_por_dia['Martes']
        diferencia = empleados_por_dia['Lunes'] - empleados_por_dia['Martes']
        diferencia_simetrica = empleados_por_dia['Lunes'] ^ empleados_por_dia['Martes']

        print(f"Empleados que trabajaron lunes o martes: {union}")
        print(f"Empleados que trabajaron lunes y martes: {interseccion}")
        print(f"Empleados que trabajaron lunes pero no martes: {diferencia}")
        print(f"Empleados que trabajaron exactamente en uno de los días: {diferencia_simetrica}")

    return empleados_por_dia

  
def Compararempleado(registros):

# Calcular horas totales por empleado
    horas_totales = {}
    for registro in registros:
       horas_totales.setdefault(registro.empleado, 0)
       horas_totales[registro.empleado] += registro.duracion()

   # Guardar CSV
    with open('resumen_horarios.csv', 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Cabecera
        escritor.writerow(['Empleado', 'Horas totales'])
    # Filas con los datos acumulados
        for empleado, total in horas_totales.items():
            escritor.writerow([empleado, total])

    print("Se ha generado el fichero resumen_horarios.csv")





def madrugadores(registros,hora_referencia=7.0):
    
    empleados_madrugadores = {}

    for r in registros:
        if r.entrada < hora_referencia:
    # Añadimos el empleado al conjunto del día
            
           empleados_madrugadores[r.empleado] = r.entrada

    #Guardar CSV
    with open('madrugadores.csv', 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Cabecera
        escritor.writerow(['Empleados_madrugadores', 'hora_entrada'])

        for   empleado,entrada in  empleados_madrugadores.items():
             h = int(entrada)
             m = int((entrada - h) * 60)
             hora_str = f"{h:02d}:{m:02d}"
             escritor.writerow([empleado, hora_str])
             print(f"{empleado}: {hora_str}")


    print("Se ha generado el fichero horarios_madrugadores.csv")



def dosdias(registros):
    # 1Agrupar empleados por día
    empleados_por_dia = {}

    for r in registros:
        if r.dia not in empleados_por_dia:
            empleados_por_dia[r.dia] = set()
        empleados_por_dia[r.dia].add(r.empleado)

    # Intersección: empleados que trabajaron Lunes y Viernes
    empleados_lunes = empleados_por_dia.get('Lunes', set())
    empleados_viernes = empleados_por_dia.get('Viernes', set())
    empleados_dosdias = empleados_lunes.intersection(empleados_viernes)

    # Guardar en CSV
    with open('en_dos_dias.csv', 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escritor.writerow(['Empleado'])
        for empleado in empleados_dosdias:
            escritor.writerow([empleado])
            print(empleado)

    print("Se ha generado el fichero en_dos_dias.csv")


def emplesdosexclusivos(registros):
    # 1Agrupar empleados por día
    empleados_por_dia = {}

    for r in registros:
        if r.dia not in empleados_por_dia:
            empleados_por_dia[r.dia] = set()
        empleados_por_dia[r.dia].add(r.empleado)

    # Intersección: empleados que trabajaron Lunes y Viernes
    empleados_sabado = empleados_por_dia.get('Lunes', set())
    empleados_domingo = empleados_por_dia.get('Viernes', set())
    empleadosexclusivos = empleados_sabado.difference(empleados_domingo)

    # Guardar en CSV
    with open('EmpleadosExclusivos.csv', 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escritor.writerow(['Empleado'])
        for empleado in empleadosexclusivos:
            escritor.writerow([empleado])
            print(empleado)

print("Se ha generado el fichero en_dos_dias.csv")

def resumensemanal(registros):
    horas_totales = {}
    dias_trabajados={}

    for r in registros:
       horas_totales.setdefault(r.empleado, 0)
       horas_totales[r.empleado] += r.duracion()

     # Registrar días trabajados (usando set para evitar duplicados)
       dias_trabajados.setdefault(r.empleado, set())
       dias_trabajados[r.empleado].add(r.dia)

     # Guardar en CSV
    with open('Conjuntoempleados.csv', 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escritor.writerow(['empleado', 'dias_trabajados', 'horas_totales'])


        for empleado in horas_totales:
            escritor.writerow([empleado,dias_trabajados[r.empleado],horas_totales[r.empleado]])
          
print("Se ha generado el Conjuntoempleados.csv")




def Filtroduracion(registros,horas_trabajadas=6.0):
    
    filtroduracion = {}

    for r in registros:
        #Comprobamos si el empleado ha trabajado al menos las horas requeridas
        if r.salida - r.entrada >= horas_trabajadas:
          
            filtroduracion.setdefault(r.entrada.date(), set()).add(r.empleado)
       

    return filtroduracion



class Empleado:


    def __init__(self, empleado: str, nombre: str):
        self.empleado = empleado
        self.nombre = nombre
        self.registros = []#Lista de registros


#Agregarregistro
    def Agregar_registro(self,registro: RegistroHorario):
        self.registros.append(registro)
    
    def horas_totales(self):
        total=0

        for r in self.registros:
            total += r.salida -r.entrada
        return total
    
    def dias_trabajados(self):

        dias = set()#inicializamos el set

        for r in self.registros:
            dias.add(r.dia)

        return len(dias)#devuleve la cantidad de eelementos por conjunto
    
    def Fila(self):
        return [self.empleado, self.nombre, self.dias_trabajados(), self.horas_totales()]



if __name__== "__main__":
   
   registros = leerregistro()
   empleados_por_dia = coleccionregistro(registros)
   Compararempleado(registros)
   madrugadores(registros, hora_referencia=8.0)
   dosdias(registros)
   emplesdosexclusivos(registros)
   resumensemanal(registros)
   Filtroduracion(registros,horas_trabajadas=6.0)

   #Creamos el empleado
   emp = Empleado("E001", "Juan Pérez")

   emp.agregar_registro(RegistroHorario("Juan Pérez", "Lunes", 8, 17))
   emp.agregar_registro(RegistroHorario("Juan Pérez", "Martes", 8, 16))
   emp.agregar_registro(RegistroHorario("Juan Pérez", "Lunes", 9, 12))

   print(emp.dias_trabajados())

   print(emp.fila_csv())