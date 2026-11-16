"""Reparte lo que llega de Debian (PASO 3).

  respuesta -> ui_bridge (la vista muestra texto y emoción)
  orden     -> seguridad.py (¿necesita confirmación?) -> skill correcta
  alerta    -> ui_bridge

Después de ejecutar una orden devuelve un "resultado" a Debian.
"""

# TODO: diccionario {"abrir_web": skills.web.abrir_web, ...}
