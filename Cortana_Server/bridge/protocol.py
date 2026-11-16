"""Formato de los mensajes entre Debian y Windows (PASO 1).

Debe ser idéntico a Cortana_Client/models/schemas.py.

Todo mensaje es un JSON con al menos:
    {"id": "<uuid>", "tipo": "<tipo>", "datos": {...}}

Tipos:
    mensaje_usuario  Windows -> Debian   lo que dices o escribes
    respuesta        Debian  -> Windows  {"texto": ..., "emocion": ...}
    orden            Debian  -> Windows  {"accion": ..., "parametros": {...}}
    resultado        Windows -> Debian   {"ok": bool, "datos": ..., "error": ...}
    contexto         Windows -> Debian   texto de la ventana actual (ojos)
    alerta           ambos               confirmaciones de seguridad y errores
    ping / pong      ambos               mantener la conexión viva
"""

# TODO: definir los modelos (Pydantic) de cada tipo de mensaje.
