# Python_Final — Sistema de Gestión de Eventos, Clientes y Ventas

##  Descripción general
**Python_Final** es una aplicación de consola desarrollada en **Python** que permite gestionar **clientes, eventos y ventas** mediante archivos CSV.  
El sistema ofrece un menú interactivo con funciones como carga de datos, alta de clientes, filtrado por fechas, métricas y exportación de informes.

---

## Funcionalidades principales

### Menú principal
```
========== MENÚ ==========
1) Cargar CSV
2) Listar tablas
3) Alta de Cliente
4) Filtro de ventas por rango de fechas
5) Métricas
6) Exportar Informe
7) Salir
```

| Opción | Descripción |
|---------|--------------|
| **1** | Carga los datos de los archivos CSV (`clientes.csv`, `eventos.csv`, `ventas.csv`). |
| **2** | Muestra por consola el contenido de cada tabla (clientes, eventos y ventas). |
| **3** | Permite dar de alta un nuevo cliente y actualizar el CSV. |
| **4** | Filtra ventas dentro de un rango de fechas. |
| **5** | Calcula métricas: ingresos totales, ingresos por evento, categorías, próximo evento y estadísticas de precios. |
| **6** | Exporta un informe resumen consolidado a `resumen_informe.csv`. |
| **7** | Finaliza el programa. |

---

## Estructura del proyecto
```
Python_Final/
│
├── main.py              # Menú principal
├── clases_csv.py        # Clases Cliente, Evento y Ventas + carga de CSV
├── methods.py           # Lógica del programa (listar, filtrar, métricas, exportar)
│
├── data/                # Carpeta con archivos CSV
│   ├── clientes.csv
│   ├── eventos.csv
│   └── ventas.csv
│
└── resumen_informe.csv  # Archivo generado con el informe
```

---

## Archivos CSV requeridos

### clientes.csv
| idcliente | nombre | email | fecha_alta |
|------------|--------|--------|-------------|
| 1 | Juan Pérez | juan@example.com | 2023-05-10 |

### eventos.csv
| idevento | nombre_evento | categoria | fecha_evento |
|-----------|----------------|------------|---------------|
| 1 | Concierto Rock | Música | 2025-07-20 |

### ventas.csv
| idventa | idcliente | idevento | fecha_venta | cantidad | total |
|----------|------------|-----------|--------------|-----------|--------|
| 1 | 1 | 1 | 2025-06-10 | 2 | 500 |

---

## Clases principales

### `Cliente`
- `idcliente`, `nombre`, `email`, `fecha_alta`
- Método: `antiguedad_dias()` → días desde el alta.

### `Evento`
- `idevento`, `nombre_evento`, `categoria`, `fecha_evento`
- Método: `dias_hasta_evento()` → días restantes hasta el evento.

### `Ventas`
- `idventas`, `idcliente`, `idevento`, `fecha_venta`, `cantidad`, `total`

---

##  Funciones destacadas

- `listar_tablas(cliente, evento, venta)` → Muestra los registros de cada tabla.
- `alta_cliente(cliente)` → Permite crear un cliente nuevo y actualizar CSV.
- `filtro_de_fechas(venta)` → Filtra y muestra ventas por rango de fechas.
- `estadistica(ventas, evento)` → Calcula ingresos totales, ingresos por evento, categorías, próximo evento y precios (min, max, promedio).
- `ExportarInforme(cliente, evento, venta)` → Genera `resumen_informe.csv` con toda la información.

---

## Ejecución

### Requisitos
- Python 3.8+
- Archivos CSV en la carpeta `data/`  
- Codificación UTF-8

### Comando
```bash
python main.py
```
Luego, seguir las opciones del menú.

---

##  Mejoras futuras
- Validación más robusta de CSV.
- Interfaz gráfica (Tkinter, PyQt).
- Exportación a PDF o Excel.
- Integración con bases de datos.

---

##  Autor
**[Diana cañas]**  
Proyecto final de Python — Gestión de datos con CSV  
 Año: 2025
