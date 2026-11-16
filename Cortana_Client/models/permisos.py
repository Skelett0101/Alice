"""US17 - Qué acciones son seguras y cuáles piden confirmación (PASO 6).

Tres niveles:
  - seguro     (verde)    se ejecuta directo: abrir_web, subir_volumen...
  - cuidado    (amarillo) pide confirmación: mover archivos, cerrar apps...
  - peligroso  (rojo)     pide confirmación explícita: borrar, ejecutar código...

Regla de oro: solo existen acciones con nombre. Nunca se ejecuta un
comando arbitrario que mande la IA.
"""

# TODO: lista blanca de acciones con su nivel.
