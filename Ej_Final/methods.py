import clases_csv
import csv
from datetime import datetime, date




def cargarDatos():
    cliente = clases_csv.CargarCSVCliente()
    evento= clases_csv.CargarCSVEvento()
    venta = clases_csv.CargarCSVVenta()
    return cliente, evento, venta

             
def listar_tablas(cliente, evento, venta):
       
    try:      
          print("\n----Clientes----")
          for c in cliente:
             print(f"{c.idcliente}: {c.nombre}, {c.email}, alta desde hace {c.antiguedad_dias()} dias")

          print("\n----Eventos----")
          for e in evento:
             print(f"{e.idevento}: {e.nombre_evento}, {e.categoria}, dias_hasta_evento {e.dias_hasta_evento()} dias")

          print("\n----Ventas----")
          for v in venta:
             print(f"{v.idventas}: {v.idcliente}, {v.idevento},  {v.fecha_venta} dias, {v.cantidad}, {v.total}")
      

    except Exception as e:
          print("Error al listar el contenido")


def alta_cliente(cliente):



    while True:
        try:
                idcliente=int(input("Introduce el id del cliente:").strip())
                for c in cliente:
                   
                   if (c.idcliente == idcliente for c in cliente):
                      print("Ese id ya existe")
                      continue
                break
        except ValueError:
            print("Error tiene que ser numero entero")
        

    nombre=input("Introduce el nombre:").strip()

    while True:
               email = input("Introduce el el email:").strip()
               if "@" in email and "." in email.split("@")[-1]:#toma lo que esta despues del @
                   break
               else:
                   print("Pon @ y .")
 

    while True:
        fecha_val = input("Fecha de alta (YYYY-MM-DD): ").strip()
        try:
           datetime.strptime(fecha_val, "%Y-%m-%d")
           break
        except ValueError:
           print('Formato incorrecto. Usa el formato YYYY-MM-DD')
        
    
   #Crear cliente y añadirlo
    Cliente = clases_csv.Cliente
    nuevo_cliente = Cliente(int(idcliente), nombre, email, fecha_val)
    cliente.append(nuevo_cliente)

    with open('data/clientes.csv', 'a', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escritor.writerow([nuevo_cliente.idcliente, nuevo_cliente.nombre, nuevo_cliente.email, nuevo_cliente.fecha_alta.strftime("%Y-%m-%d")])


    print(f"Cliente '{nombre}' agregado correctamente.\n")





def filtro_de_fechas(venta):
   
   #leemos y validamos las fechas
    while True:
        fecha_inicio_val= input("Fecha del incio de la fecha(YYYY-MM-DD)::")
        try:
           fecha_inicio= datetime.strptime(fecha_inicio_val, "%Y-%m-%d").date()
           break
        except ValueError:
           print('Formato incorrecto. Usa el formato YYYY-MM-DD')
       

    while True:
        fecha_final_val= input("Fecha final de la venta (YYYY-MM-DD):")
        try:
           fecha_final= datetime.strptime(fecha_final_val, "%Y-%m-%d").date()

           if fecha_final < fecha_inicio :
               print('La fecha inicial no puede ser mayor que la inicial')
               continue
           break
        except ValueError:
           print('Formato incorrecto. Usa el formato YYYY-MM-DD')
             

    print(f"\nRango de fechas válido: {fecha_inicio} hasta {fecha_final}")



   
    ventas_filtradas = []

    for v in venta:
        #Estamos indicando si la fecha_venta esta dentro del rango de fechas que el usuario introduzco
        if fecha_inicio <= v.fecha_venta <=fecha_final:
            ventas_filtradas.append(v)
            print(f"Venta {v.idventas}: Cliente {v.idcliente}, Evento {v.idevento}, , Fecha: {v.fecha_venta}, Cantidad: ${v.cantidad}, Total: ${v.total}")
    

    #Mostrar un resumen
    if not ventas_filtradas:
        print("No hay ventas en el rango indicado.")
    else:
        print(f"\nTotal de ventas encontradas: {len(ventas_filtradas)}")

    return ventas_filtradas


def estadistica(ventas, evento):


    #Ingresar totales
    ingresos_totales = 0
    ingresos_por_evento = {}
    
    for v in ventas:

        total = int(v.total)
        ingresos_totales += total
        
        if v.idevento not in ingresos_por_evento:
            ingresos_por_evento[v.idevento] = 0
        ingresos_por_evento[v.idevento] += total

    print(f"\nIngresos totales: {ingresos_totales}")

    print("\nIngresos por evento:")

    for evento_id, total_evento in ingresos_por_evento.items():#obtener tanto las claves como los valores del diccionario al mismo tiempo.
        print(f"   Evento {evento_id}: {total_evento}")
     
    #set de categorias existentes
    categorias_existentes = [e.categoria for e in evento]
    
    if not categorias_existentes:
        print("\nNo se ha encontrado ninguna categoría.")
    else:
        print('\n Categorias encontradas:')    
        for c in set(categorias_existentes):#El set es para evitar duplicados
            print({c})


   #dias hasta el evento
    evento_proximo = []
    
    for e in evento:
        if e.dias_hasta_evento() >= 0:
            evento_proximo.append(e)


    if evento_proximo:
        proximo_evento = evento_proximo[0]#filtrar elemenos que aun no ha pasado

        if e.fecha_evento <= proximo_evento.fecha_evento:

            dias_restantes = proximo_evento.dias_hasta_evento()

            print(f"\nPróximo evento: {proximo_evento.nombre_evento} en {dias_restantes} días (Fecha: {proximo_evento.fecha_evento})")

    
    '''for e in evento:
         if e.fecha_evento >= hoy:
             evento_proximo.append(e)


    if evento_proximo:

        proximo_evento = evento_proximo[0]
        
        if e.fecha_evento <= proximo_evento.fecha_evento:

            dias_restantes = (proximo_evento.fecha_evento - hoy).days

            print(f"\nPróximo evento: {proximo_evento.nombre_evento} en {dias_restantes} días (Fecha: {proximo_evento.fecha_evento})")'''


    #tupla de precios
    tupla_precios=[]
    lista_precios = []
    

    for p in ventas:
         lista_precios.append(int(p.total))

     
    
    if not lista_precios:
        print("No hay lista de precios")
        tupla_precios(0,0,0)
    
    #Calcular
    minimo = min(lista_precios)
    maximo = max(lista_precios)
    media = sum(lista_precios)/len(lista_precios)

    tupla_precios = (minimo, maximo, media)

    print(f"\nTupla de precios (min, max, media): {tupla_precios}")
   
  
    return ingresos_totales, ingresos_por_evento, categorias_existentes,evento_proximo,tupla_precios


def ExportarInforme(cliente,evento,venta):

    clientes_totales = []
    eventos_totales = []
    ventas_totales = []

    for c in cliente :
        clientes_totales.append([c.idcliente,c.nombre, c.email,c.fecha_alta])

    for e in evento:
        eventos_totales.append([e.idevento, e.nombre_evento,e.categoria, e.fecha_evento])

  
    for v in venta: 
        ventas_totales.append([v.idventas, v.idcliente,  v.idevento, v.fecha_venta, v.cantidad, v.total])


    with open('resumen_informe.csv','w', newline= '' , encoding= 'utf-8') as f:


        escritor= csv.writer(f, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        escritor.writerow(['Clientes registrados'])
        escritor.writerow(['ID Cliente', 'Nombre', 'Email', 'Fecha de alta'])
        escritor.writerows(clientes_totales)

        escritor.writerow(['Eventos'])
        escritor.writerow(['ID Evento', 'Nombre del evento', 'Categoría', 'Fecha del evento'])
        escritor.writerows(eventos_totales)

            
        escritor.writerow(['Ventas'])
        escritor.writerow(['ID Venta', 'ID Cliente', 'ID Evento', 'Fecha venta', 'Cantidad', 'Total'])
        escritor.writerows(ventas_totales)


    print("Archivo 'resumeninforme.csv' exportado correctamente.")