# M2-InputBuffer
[M2] Actividad Práctica: Implementación de un Búfer de Entrada - Diseño de Lenguajes de Programación 2025

Este código implementa un procesador de texto basado en buffers en Python. Divide una entrada en fragmentos de tamaño fijo (buffers) y procesa cada fragmento secuencialmente, identificando palabras (lexemas) separadas por espacios. Utiliza una función auxiliar cargar_buffer para cargar los fragmentos y un bucle principal que maneja el procesamiento de cada buffer. Este enfoque es útil para manejar entradas grandes sin cargar todo el contenido en memoria al mismo tiempo.

Ejemplo de salida del programa:

Entrada utilizada: "Esto es un ejemplo eof"
Tamaño del buffer: 10

Salida del programa:

```bash
Lexema procesado: Esto
Lexema procesado: es
Lexema procesado: un
Lexema procesado: ejemplo
Lexema procesado: eof
```
Este ejemplo demuestra cómo el código procesa las palabras una a una desde la entrada utilizando bloques de texto definidos por el tamaño del buffer.
