"""
  Módulo para la creación y gestión de la terminal interactiva  usando  typer y shlex
  Se crea un bucle de lectura desde el teclado usando shlex desde un prompt personalizado
  nombrado como  qrunner> , recibe las instrucciones y las va ejecutando según corresponda
  el bucle finaliza cuando el usuairo ingresa la palabra exit  o quit para finalizar la sesión

  utiliza un archivo llamado  .qureyrunner_history  para guardar un historial de comando usados por el usuario
  y poder reutilizarlos usando las flechas arriba y abajo del teclado

"""
import readline
import shlex

from cli.commands import run_query

# Nombre para archivo de historico de comandos
HISTORY_FILE = ".queryrunner_history"

"""
    Construcción del bucle infinito de lectura desde teclado
"""
def start_repl():
    print("Welcome to QueryRunner app (type 'exit' to quit the app)")
    print("Type ':help' for more information")

    # Lectura del historico de comandos
    try:
        readline.read_history_file(HISTORY_FILE)
    except FileNotFoundError:
        pass

    # Proceso de lectura de instrucciones desde terminal interactiva
    while True:
        try:
            line = input("qrunner> ").strip()

            if not line:
                continue

            tokens = shlex.split(line)

            query, opts = parse_repl_input(tokens)

            # Comandos para salida del programa
            if query.lower() in ("exit", "quit"):
                break

            # si query es vacío solo sigue esperando
            if not query:
                continue

            if query.startswith(":"):
                handle_meta_command(query)
                continue

            print("Execute command: " + query)

            run_query(sql=query,file=opts["file"],format=opts["format"],verbose=opts["verbose"],
                      optimize=opts["optimize"],target=opts["target"])

        except KeyboardInterrupt:
            print("\nInterrupted")
        except Exception as e:
            print(f"Error: {e}")

    readline.write_history_file(HISTORY_FILE)


"""
    Método para imprimir un texto de ayuda cuando el usuario ingresa el comando :help
    le dará información básica del uso de la herramienta
"""
def handle_meta_command(cmd):
    if cmd == ":help":
        print("""
            [COMMANDS]:
                :help           -> Mostrar ayuda
                exit            -> Salir
                query           -> Query para consula sobre archivos
            [OPTIONS]:
                --file      -f  -> Archivo fuente para consulta
                --format    -f  -> Format de salida consulta
                --target    -t  -> Destino de salida para consulta
                --verbose   -v  -> Verbosidad de salida
                --optimize  -o  -> Optimize de salida
            [EXAMPLE]:]
                qrunner> LEER ventas.csv EXTRAER * DONDE total > 500 Y categoria = "electronica" --target salida.json --format json
            """)


"""
    Método para separar las posibles opciones que el usuario ingrese en el prompt junto al query que necesita ejecutar
    similar a como lo hace invocando la herramienta desde el exterior de la terminal interactiva
"""
def parse_repl_input(tokens):

    args = {"file": None,"format": "table","verbose": False,"optimize": True,"target": None}

    query_tokens = []

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token == "--file":
            args["file"] = tokens[i + 1]
            i += 2

        elif token == "--format":
            args["format"] = tokens[i + 1]
            i += 2

        elif token == "--target":
            args["target"] = tokens[i + 1]
            i += 2

        elif token == "--verbose":
            args["verbose"] = True
            i += 1

        elif token == "--optimize":
            args["optimize"] = True
            i += 1

        else:
            query_tokens.append(token)
            i += 1

    query = " ".join(query_tokens)

    return query, args