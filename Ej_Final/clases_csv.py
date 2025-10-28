import csv
from datetime import datetime, date


class Evento:
   
   def __init__(self, idevento: int, nombre_evento: str, categoria: str, fecha_evento: str):
        self.idevento= idevento
        self.nombre_evento = nombre_evento
        self.categoria = categoria
        self.fecha_evento = datetime.strptime(fecha_evento, "%Y-%m-%d").date()#lo transforma a un numero entero

   def dias_hasta_evento(self) -> int:
       return (self.fecha_evento - date.today()).days

def CargarCSVEvento():
   
    try:
        eventos = []
        with open('data/eventos.csv', newline='', encoding='utf-8') as f:
          lector = csv.reader(f,delimiter=',', quotechar='"')
          next(lector)

          for fila in lector:
              if not fila or len(fila)<4:
                  continue
              idevento,nombre_evento,categoria,fecha_evento=fila[:4]
              evento = Evento(idevento,nombre_evento,categoria,fecha_evento)
              eventos.append(evento)
        print("Archivo leido con exito de evento.csv")

    except FileNotFoundError:
           print("Archivo no encontrado")
    except Exception as e:
           print("Error al leer el archivo")
    return eventos   


class Cliente:

    def __init__(self, idcliente: int, nombre: str, email: str, fecha_alta: int):
        self.idcliente= idcliente
        self.nombre = nombre
        self.email = email
        #Convertimos el texto en objeto date
        self.fecha_alta = datetime.strptime(fecha_alta, "%Y-%m-%d").date()

   
    def antiguedad_dias(self) -> int:
       return (date.today() - self.fecha_alta).days


def CargarCSVCliente():
   
    try: 
        cliente = []

        with open('data/clientes.csv', newline='', encoding='utf-8') as f:
            lector = csv.reader(f,delimiter=',', quotechar='"')
            next(lector)

            for fila in lector:
                if not fila or len(fila) < 4:
                    continue
                idcliente,nombre,email,fecha_alta=fila[:4]# ignorar columnas de más
                cliente= Cliente(int(idcliente),nombre,email,fecha_alta)
                cliente.append(cliente)
        print("Archivo leido con exito de cliente.csv")

    except FileNotFoundError:
           print("Archivo no encontrado")
    except Exception as e:
           print("Error al leer el archivo")
    return cliente   

class Ventas():

    def __init__(self, idventas: int, idcliente: int, idevento: int, fecha_venta: str,cantidad: int,total :int):
        self.idventas= idventas
        self.idcliente= idcliente
        self.idevento= idevento
        self.fecha_venta = datetime.strptime(fecha_venta, "%Y-%m-%d").date()#lo transforma a un numero entero
        self.cantidad = cantidad
        self.total = total
   


def CargarCSVVenta():
   
    try:
        ventas = []
        with open('data/ventas.csv', newline='', encoding='utf-8') as f:
           lector = csv.reader(f,delimiter=',', quotechar='"')
           next(lector)

           for fila in lector:
             if not fila or len(fila)<6:
                 continue          
             idventa,idcliente,idevento,fecha_venta,cantidad,total=fila[:6]
             ventas= Ventas(idventa,idcliente,idevento,fecha_venta,cantidad,total)
             ventas.append(ventas)
        print("Archivo leido con exito de venta.csv")

    except FileNotFoundError:
           print("Archivo no encontrado")
    except Exception as e:
           print("Error al leer el archivo")
    return ventas  

           

