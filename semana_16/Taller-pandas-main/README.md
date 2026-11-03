# Taller práctico: análisis de datos con Pandas

**Estudiante: Nicole Bolivar Hernandez**

## Ejecución en Linux
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python evidencias.py
python exploracion.py
python main.py
python bonus.py
```
En main.py selecciona, en orden: 1, 2, 3, 4, 5 y 6. Si se abren ventanas de gráficos, ciérralas para continuar. Los PNG se guardan en Data/processed/graficos incluso si el entorno no permite mostrar ventanas.

## Exploración y limpieza
Clientes tiene 60 filas y 5 columnas; ventas, 68 filas y 10 columnas. Producto tiene 67 valores no nulos antes de limpiar. No hay filas duplicadas ni nulos en clientes. Se recortan espacios, se normaliza ciudad con title, se aplica drop_duplicates y se reinician índices. El producto vacío se rellena con "Sin especificar": usar dropna eliminaría una venta real de 780000 y alteraría los ingresos. fecha_venta se convierte con formato %Y-%m-%d y errors="coerce"; no se detectan fechas inválidas. Tras limpiar hay 68 ventas, cero nulos y cero duplicados.

Después de set_index("id_venta"), V003 es la fila en posición 2. Las columnas restantes son: id_cliente (0), fecha_venta (1), producto (2), categoria (3), cantidad (4), precio_unitario (5), total (6), canal (7) y metodo_pago (8). Por eso .iloc[2, 6] devuelve 520000, el total de V003.

El merge es izquierdo y m:1: conserva las 68 ventas y agrega los datos de cada cliente sin multiplicar filas. Tiene 14 columnas porque 10 + 5 - 1 = 14; id_cliente, columna común, aparece una sola vez. No hay ventas sin cliente asociado.

## Desafío final: resultados de terminal y criterios

### 1. Categoría con más ingresos
```text
categoria
Tecnologia    14290000
Hogar          3653000
Papeleria       749000
Accesorios      484000
```
Tecnología genera más ingresos: 14290000. Criterio: suma de total por categoría, orden descendente.

### 2. Canal que más vende
```text
        ventas  ingresos
Online      35  14669000
Tienda      33   4507000
```
Online lidera por ingresos (14669000), criterio principal elegido. También lidera por número de ventas: 35 frente a 33. Una venta se cuenta por registro, no por unidades de producto.

### 3. VIP frente a Regular
```text
                  clientes  compras  gasto_total  compras_por_cliente  gasto_por_cliente
Regular                 36       39     11110000             1.083333      308611.111111
VIP                     24       29      8066000             1.208333      336083.333333
```
Sí, los VIP compran más por cliente: 1,208333 compras frente a 1,083333; su gasto promedio también es mayor: 336083,33 frente a 308611,11. Criterio: compras y gasto divididos entre clientes únicos de cada segmento, no comparación de totales. Se consideran clientes presentes en el merge; en estos datos los 60 clientes tienen compras.

### 4. Método de pago más usado
```text
Efectivo         30
Tarjeta          25
Transferencia    13
```
Efectivo es el más usado con 30 ventas. Criterio: frecuencia de registros por método de pago.

### 5. Cinco clientes con más compras
```text
id_cliente nombre_cliente       compras  gasto_total
21         Nicolas Cardona            2      2515000
35         Matias Rodriguez           2      1278000
52         Mia Quintero               2      1090000
58         Luna Montoya               2      1007000
3          Luis Perez                 2       730000
```
Estos cinco clientes encabezan el ranking. Criterio: número de compras descendente; para empates se usa gasto total descendente.

## Bonus: ventas por mes
```text
2026-04    18234000
2026-05      942000
```
Abril de 2026 tuvo más ingresos, con 18234000. Criterio: suma de total agrupada por período año-mes con dt.to_period("M"). El período de mayo solo contiene datos hasta el 4 de mayo; no se interpreta esta comparación como desempeño de dos meses completos.

## Archivos y evidencias
- main.py y Data/raw se conservan iguales a los originales.
- limpieza.py, merge.py, analisis.py y graficos.py completan las 14 tareas.
- evidencias.py agrega exploración de ambas tablas, usecols y líneas propias con loc, iloc y concat.
- bonus.py ejecuta el bonus por separado sin modificar el menú.
- Data/processed contiene el merge, la tabla mensual y los dos PNG obligatorios.
- images contiene las 12 capturas reales de ejecución organizadas por etapa.
