
# GUÍA: PLAN DE EJECUCIÓN Y OPTIMIZACIÓN (PIPELINE)


A partir de ahora, cada consulta mostrará el PLAN DE EJECUCIÓN
que visualiza el pipeline de operaciones que realiza el motor
para procesar tu consulta, incluyendo el algoritmo de búsqueda
optimizado que se utiliza.


## ¿QUÉ ES EL PLAN DE EJECUCIÓN?


Es una representación visual de las operaciones que realiza
QueryRunner en orden para ejecutar tu consulta. Incluye:

1. SCAN - Lectura del archivo de datos con algoritmo optimizado
2. FILTER - Aplicación de filtros (DONDE)
3. ORDER BY - Ordenamiento de resultados (ORDENAR)
4. LIMIT - Limitación de resultados (HASTA)
5. PROJECT - Selección de columnas (EXTRAER)
6. OPTIMIZED - Algoritmo de búsqueda utilizado

QueryRunner utiliza una arquitectura de dos niveles:

NIVEL 1: PLAN LÓGICO (Generado por el compilador)
  - Se genera al compilar la consulta
  - Siempre muestra "op": "Scan" (abstracto)
  - Se imprime en el JSON cuando usas --verbose
  - No conoce los datos ni su estructura

NIVEL 2: PLAN FÍSICO (Generado en tiempo de ejecución)
  - Se genera al ejecutar la consulta
  - Aquí se decide el algoritmo específico de búsqueda
  - Se imprime en el PLAN DE EJECUCIÓN visual
  - Elige el algoritmo basado en los datos reales

Ejemplo:
- JSON: "op": "Scan" (abstracto)
- Pipeline: "SCAN: Leer archivo 'data/ventas.json' [INDEX_SCAN]" (concreto)


## ALGORITMOS DE BÚSQUEDA


QueryRunner soporta 4 algoritmos de búsqueda diferentes:

1. FULL_SCAN
   - Escaneo completo del archivo
   - Se usa cuando no hay filtros simples
   - O cuando el filtro no cumple condiciones para otros algoritmos
   - Rendimiento: O(n) - lineal

2. INDEX_SCAN
   - Búsqueda por índice en una columna
   - Condiciones:
     * Filtro con igualdad (=)
     * UN solo filtro simple
     * La columna debe existir en los datos
   - Rendimiento: O(1) en promedio con índice
   - Ejemplo: WHERE categoria = 'Muebles'

3. HASH_LOOKUP
   - Búsqueda por tabla hash para búsquedas rápidas
   - Similar a INDEX_SCAN pero usando hash
   - Condiciones:
     * Filtro con igualdad (=)
     * UN solo filtro simple
     * La columna debe existir en los datos
   - Rendimiento: O(1) promedio
   - Ejemplo: WHERE total = 1000

4. BINARY_SEARCH
   - Búsqueda binaria en datos ordenados
   - Condiciones:
     * Hay ORDER BY
     * El filtro WHERE está en la columna del ORDER BY
     * La columna es numérica
   - Rendimiento: O(log n)
   - Ejemplo: DONDE total > 1000 ORDENAR POR total

Prioridad automática de selección:
  BINARY_SEARCH > HASH_LOOKUP > INDEX_SCAN > FULL_SCAN


### AUTO-DETECCIÓN DE ALGORITMOS


El optimizer detecta automáticamente el mejor algoritmo
basado en:

1. Estructura del plan (DONDE, ORDER BY, LIMIT)
2. Tipos de datos en las columnas
3. Operadores de comparación utilizados
4. Presencia de múltiples filtros (AND/OR)

Ejemplo 1: Detección de BINARY_SEARCH
  Consulta:
    LEER 'data/ventas.json' EXTRAER * DONDE total > 1000 ORDENAR POR total
  
  Detección:
    - Hay ORDER BY por 'total'
    - Hay WHERE con 'total' (misma columna)
    - 'total' es numérica
    - Resultado: BINARY_SEARCH

Ejemplo 2: Detección de HASH_LOOKUP
  Consulta:
    LEER 'data/productos.json' EXTRAER * DONDE categoria = 'Computo'
  
  Detección:
    - Hay WHERE con igualdad (=)
    - Solo un filtro simple
    - No hay ORDER BY o está en otra columna
    - Resultado: HASH_LOOKUP

Ejemplo 3: Detección de FULL_SCAN
  Consulta:
    LEER 'data/ventas.json' EXTRAER * DONDE total > 500 Y cantidad > 2
  
  Detección:
    - Hay filtros múltiples (Y)
    - No cumple condiciones para otros algoritmos
    - Resultado: FULL_SCAN


## ESPECIFICAR ALGORITMO MANUALMENTE


Puedes forzar un algoritmo específico con --algorithm o -a:

Sintaxis:
  qrunner> Tu consulta --algorithm ALGORITHM_NAME
  qrunner> Tu consulta -a ALGORITHM_NAME

Algoritmos disponibles:
  - FULL_SCAN
  - INDEX_SCAN
  - HASH_LOOKUP
  - BINARY_SEARCH

Ejemplos:

1. Forzar INDEX_SCAN:
   LEER 'data/productos.json' EXTRAER * DONDE precio = 100 --algorithm INDEX_SCAN

2. Forzar BINARY_SEARCH:
   LEER 'data/ventas.json' EXTRAER * DONDE total > 1000 ORDENAR POR total -a BINARY_SEARCH

3. Forzar FULL_SCAN (sin optimización):
   LEER 'data/datos.json' EXTRAER * DONDE total > 500 Y cantidad > 2 --algorithm FULL_SCAN

Nota: Si especificas un algoritmo incompatible con la consulta,
el sistema intentará usarlo igual (útil para testing).


EJEMPLO: SIMPLE SCAN (FULL_SCAN)


Consulta:
qrunner> LEER 'data/ventas_masivas_100k.json' EXTRAER *

## Salida:

### PLAN DE EJECUCIÓN

1. SCAN: Leer archivo 'data/ventas_masivas_100k.json' (JSON)
2. PROJECT: Seleccionar todas las columnas (*)
=

Interpretación:
- No hay filtros, por lo que usa FULL_SCAN
- Lee todo el archivo
- Selecciona todas las columnas
- Retorna todos los registros


EJEMPLO: CON FILTRO SIMPLE (AUTO-DETECTA HASH_LOOKUP)


Consulta:
qrunner> LEER 'data/ventas_masivas_100k.json' EXTRAER * DONDE categoria = 'Muebles'


## Salida:

### PLAN DE EJECUCIÓN
1. SCAN: Leer archivo 'data/ventas_masivas_100k.json' (JSON) [HASH_LOOKUP]
  -> Hash lookup en columna 'categoria' para valor 'Muebles'
2. FILTER: Aplicar condición WHERE -> categoria = Muebles
3. PROJECT: Seleccionar todas las columnas (*)
4. OPTIMIZED: Usando algoritmo HASH_LOOKUP
=

Interpretación:
- Detecta filtro de igualdad en una sola columna
- Elige HASH_LOOKUP automáticamente
- Aplica el filtro de forma optimizada
- Muestra OPTIMIZED porque no es FULL_SCAN


EJEMPLO: CON FILTRO COMPLEJO (FULL_SCAN)


Consulta:
qrunner> LEER 'data/ventas_masivas_100k.json' EXTRAER * DONDE categoria = 'Muebles' Y cantidad > 2 O total > 2000


## Salida:

### PLAN DE EJECUCIÓN
1. SCAN: Leer archivo 'data/ventas_masivas_100k.json' (JSON)
2. FILTER: Aplicar condición WHERE -> categoria = Muebles Y cantidad > 2 O total > 2000
3. PROJECT: Seleccionar todas las columnas (*)
=

Interpretación:
- Hay múltiples filtros con AND/OR
- No cumple condiciones para algoritmos optimizados
- Usa FULL_SCAN
- No aparece OPTIMIZED (solo aparece para algoritmos != FULL_SCAN)


EJEMPLO: CON FILTRO Y ORDENAMIENTO (BINARY_SEARCH)


Consulta:
qrunner> LEER 'data/ventas_masivas_100k.json' EXTRAER id_venta, cliente, total DONDE total > 1000 ORDENAR POR total DESCENDENTE


## Salida:

### PLAN DE EJECUCIÓN
1. SCAN: Leer archivo 'data/ventas_masivas_100k.json' (JSON) [BINARY_SEARCH]
  -> Búsqueda binaria en 'total' (DESCENDENTE) con condición 'total > 1000'
2. FILTER: Aplicar condición WHERE -> total > 1000
3. ORDER BY: Ordenar por total (DESCENDENTE)
4. PROJECT: Seleccionar columnas -> id_venta, cliente, total
5. OPTIMIZED: Usando algoritmo BINARY_SEARCH
=

Interpretación:
- Detecta ORDER BY en 'total' y WHERE en 'total' (misma columna)
- Columna es numérica
- Elige BINARY_SEARCH automáticamente
- Más eficiente que FULL_SCAN para datos ordenados


EJEMPLO: FORZAR ALGORITMO MANUALMENTE


Consulta 1: Especificar INDEX_SCAN
qrunner> LEER 'data/productos.json' EXTRAER * DONDE precio = 100 --algorithm INDEX_SCAN


## Salida:

### PLAN DE EJECUCIÓN
1. SCAN: Leer archivo 'data/productos.json' (JSON) [INDEX_SCAN]
  -> Indice en columna 'precio' buscando valor '100'
2. FILTER: Aplicar condición WHERE -> precio = 100
3. PROJECT: Seleccionar todas las columnas (*)
4. OPTIMIZED: Usando algoritmo INDEX_SCAN
=

Consulta 2: Especificar HASH_LOOKUP con -a
qrunner> LEER 'data/productos.json' EXTRAER * DONDE categoria = 'Computo' -a HASH_LOOKUP


## Salida:

### PLAN DE EJECUCIÓN
1. SCAN: Leer archivo 'data/productos.json' (JSON) [HASH_LOOKUP]
  -> Hash lookup en columna 'categoria' para valor 'Computo'
2. FILTER: Aplicar condición WHERE -> categoria = Computo
3. PROJECT: Seleccionar todas las columnas (*)
4. OPTIMIZED: Usando algoritmo HASH_LOOKUP
=


## ORDEN DE OPERACIONES


El pipeline siempre sigue este orden:

1. SCAN - Leer datos del archivo con algoritmo optimizado
2. FILTER - Aplicar condiciones WHERE
3. ORDER BY - Ordenar resultados
4. LIMIT - Limitar cantidad de registros
5. PROJECT - Seleccionar columnas finales
6. Retornar resultados

Este orden es ESTÁNDAR en sistemas de bases de datos
y optimiza el rendimiento de las consultas.


## OPTIMIZACIONES APLICADAS


QueryRunner aplica las siguientes optimizaciones:

1. Selección automática de algoritmo
   - Elige el mejor algoritmo según el plan
   - Prioriza BINARY_SEARCH > HASH_LOOKUP > INDEX_SCAN > FULL_SCAN

2. Uso de columnas selectivas
   - Si no usas SELECT *, solo carga las columnas necesarias
   - Reduce uso de memoria

3. Chunk processing (archivos grandes)
   - Para archivos > 50MB, procesa por chunks de 50,000 registros
   - Evita saturar la memoria

4. Lazy filtering
   - Aplica filtros durante la lectura cuando es posible
   - Reduce cantidad de registros en memoria

El flag --optimize true está activo por defecto y aplica
todas estas optimizaciones automáticamente.

## MODO VERBOSE (DEBUG)


Para ver detalles completos incluyendo el plan JSON:
qrunner> consulta --verbose

Esto mostrará:
- SQL utilizado
- Archivo cargado
- Optimizaciones activadas
- Algoritmo especificado (si aplica)
- Plan completo en JSON (plan lógico del compilador)
- PLAN DE EJECUCIÓN visual (plan físico con algoritmo)
- Resultados de la consulta
- Algoritmo utilizado finalmente

Ejemplo:
qrunner> LEER 'data/productos.json' EXTRAER * DONDE precio > 100 --verbose --algorithm HASH_LOOKUP

## CASOS DE USO POR ALGORITMO


FULL_SCAN - Usar cuando:
- No hay filtros
- Hay múltiples filtros con AND/OR
- Necesitas escanear todo el dataset
- Filtros no cumplen condiciones de otros algoritmos

INDEX_SCAN - Usar cuando:
- Necesitas buscar por igualdad exacta
- Tienes un índice en la columna
- Solo una condición simple
- Quieres búsqueda determinística

HASH_LOOKUP - Usar cuando:
- Necesitas búsqueda rápida por igualdad
- La tabla hash se mantendrá en memoria
- Solo una condición simple
- Datos sin estructura particular

BINARY_SEARCH - Usar cuando:
- Los datos están ordenados o necesitas ordenarlos
- Filtro está en la columna de ordenamiento
- Columna es numérica
- Quieres O(log n) en lugar de O(n)
