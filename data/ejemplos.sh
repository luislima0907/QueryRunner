#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
CSV="$DIR/ventas.csv"
JSON="$DIR/productos.json"
VENV_PYTHON="$DIR/../.venv/bin/python"
CMD="$VENV_PYTHON $DIR/../main.py"

echo "============================================"
echo "  EJEMPLOS DE CONSULTAS - QueryRunner"
echo "============================================"

echo ""
echo "--- 1. SELECT * (todas las columnas) ---"
$CMD query "LEER \"$CSV\" EXTRAER *"

echo ""
echo "--- 2. SELECT * con FILTRO (WHERE) ---"
$CMD query "LEER \"$CSV\" EXTRAER * DONDE total > 300"

echo ""
echo "--- 3. SELECT columnas especificas + WHERE compuesto (Y) ---"
$CMD query "LEER \"$CSV\" EXTRAER nombre, edad, total DONDE ciudad = \"Guatemala\" Y total > 200"

echo ""
echo "--- 4. SELECT con OR ---"
$CMD query "LEER \"$CSV\" EXTRAER nombre, ciudad DONDE ciudad = \"Antigua\" O total > 500"

echo ""
echo "--- 5. SELECT con ORDER BY ASC ---"
$CMD query "LEER \"$CSV\" EXTRAER nombre, total ORDENAR POR total ASCENDENTE"

echo ""
echo "--- 6. SELECT con ORDER BY DESC ---"
$CMD query "LEER \"$CSV\" EXTRAER * ORDENAR POR edad DESCENDENTE"

echo ""
echo "--- 7. SELECT con LIMITE (HASTA) ---"
$CMD query "LEER \"$CSV\" EXTRAER * HASTA 3"

echo ""
echo "--- 8. SELECT con WHERE + ORDER + LIMIT combinados ---"
$CMD query "LEER \"$CSV\" EXTRAER * DONDE total > 200 ORDENAR POR total DESCENDENTE HASTA 4"

echo ""
echo "--- 9. JSON: SELECT * ---"
$CMD query "LEER \"$JSON\" EXTRAER *"

echo ""
echo "--- 10. JSON: WHERE + proyeccion ---"
$CMD query "LEER \"$JSON\" EXTRAER producto, precio DONDE categoria = \"Computo\""

echo ""
echo "--- 11. JSON: ORDER BY + LIMIT ---"
$CMD query "LEER \"$JSON\" EXTRAER producto, stock ORDENAR POR stock DESCENDENTE HASTA 3"

echo ""
echo "--- 12. SALIDA JSON (--format json) ---"
$CMD query "LEER \"$CSV\" EXTRAER nombre, total DONDE total > 400" --format json

echo ""
echo "--- 13. SALIDA CSV a archivo (--format csv --target) ---"
$CMD query "LEER \"$CSV\" EXTRAER * DONDE ciudad = \"Quetzaltenango\"" --format csv --target /tmp/reporte.csv
cat /tmp/reporte.csv

echo ""
echo "============================================"
echo "  Todos los ejemplos ejecutados con exito"
echo "============================================"
