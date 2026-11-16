"""WebSocket local (127.0.0.1:8000) entre el cliente y la vista (PASO 8).

Es la única puerta de la vista, así que React y Godot usan el mismo contrato:

  Vista -> cliente : {"tipo": "mensaje_usuario", "texto": "..."}
                     {"tipo": "confirmacion", "id": "...", "aceptar": true}
  Cliente -> vista : {"tipo": "respuesta", "texto": "...", "emocion": "feliz"}
                     {"tipo": "alerta", "nivel": "amarillo", "texto": "..."}

Cambiar React por Godot (US16) no toca nada fuera de views/.
"""

# TODO: implementar.
