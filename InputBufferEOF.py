def cargar_buffer(entrada, inicio, tamano_buffer):
    fin = inicio + tamano_buffer
    buffer = entrada[inicio:fin]
    es_final = fin >= len(entrada)  # Determinar si este buffer alcanza el final de la entrada
    return buffer, es_final  # Devolver tanto el buffer como el estado final

def procesar_buffer(entrada, tamano_buffer):
    entrada = list(entrada)  # Convertir la entrada a lista para manejarla fácilmente
    inicio_buffer = 0
    buffer, es_final = cargar_buffer(entrada, inicio_buffer, tamano_buffer)
    avance = 0
    lexema = []

    while True:
        while avance < len(buffer) and buffer[avance] != " ":
            lexema.append(buffer[avance])
            avance += 1

        # Debugging
        # print("Buffer actual:", buffer)
        # print("Último carácter del buffer:", buffer[-1] if buffer else None)

        # Procesar el lexema si llegamos a un espacio o al final del buffer
        if avance < len(buffer) and buffer[avance] == " ":
            if lexema:
                print("Lexema procesado:", "".join(lexema))
                lexema = []  # Limpiar el lexema después de procesarlo
            avance += 1  # Saltear el espacio

        # Si hemos alcanzado el final del buffer y no es el final de la entrada, cargar el siguiente buffer
        if avance >= len(buffer):
            if es_final:  # Si es el final de la entrada y hay un lexema no procesado
                if lexema:
                    print("Lexema procesado:", "".join(lexema))
                break
            else:
                inicio_buffer += tamano_buffer  # Avanzar el inicio del buffer
                avance = 0
                buffer, es_final = cargar_buffer(entrada, inicio_buffer, tamano_buffer)

entrada = "Esto es un ejemplo de entrada con eof"
tamano_buffer = 10
procesar_buffer(entrada, tamano_buffer)
