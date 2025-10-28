import clases_csv
import methods

#Menu
def Menu():

    cliente = []
    evento = []
    venta = []
    
    while True:
        print("========== MENÚ ==========")
        print("1) cargar CSV")
        print("2) Listar tablas")
        print("3) Alta de Cliente")
        print("4) Filtro de ventas por rango de fechas")
        print("5) Métricas")
        print("6) Exportar Informe")    
        print("7) Salir")
        option = input("Elige una opcion(1-7):").strip()

        if option == '1':

            cliente, evento, venta = methods.cargarDatos()
                
        elif option == '2': 

            if cliente and evento and venta:     
                   
               methods.listar_tablas(cliente, evento, venta)

            else:
               print("Aún no se han cargado las listas. Primero seleccione la opción 1 para cargar")

        elif option == '3':
             
            if cliente:     
                   
               methods.alta_cliente(cliente)

            else:
               print("Aún no se han cargado las listas. Primero seleccione la opción 1 para cargar")

        elif option == '4':

            if venta:
                methods.filtro_de_fechas(venta)
            else:
                  print("Aún no se han cargado las listas. Primero seleccione la opción 1 para cargar") 

        elif option == '5':
            if venta and evento:
                methods.estadistica(venta,evento)

            else:
                  print("Aún no se han cargado las listas. Primero seleccione la opción 1 para cargar") 

        elif option == '6':

            if cliente and evento and venta:     
                   
               methods.ExportarInforme(cliente,evento,venta)

            else:
               print("Aún no se han cargado las listas. Primero seleccione la opción 1 para cargar")

        elif option == '7':
              
              print('Saliendo...')
              break
        else:
            print('opcion no valida')



if __name__ == "__main__":
    Menu()