"""M de MVC (US14): modelos Pydantic de los mensajes (PASO 1).

Debe ser idéntico a Cortana_Server/bridge/protocol.py.

Mensaje base: {"id", "tipo", "datos"}
Tipos: mensaje_usuario, respuesta, orden, resultado, contexto, alerta, ping, pong

Ejemplo de orden:
    {"id": "1", "tipo": "orden",
     "datos": {"accion": "abrir_web", "parametros": {"url": "github.com"}}}

Ejemplo de respuesta:
    {"id": "2", "tipo": "respuesta",
     "datos": {"texto": "¡Claro, abriendo GitHub!", "emocion": "feliz"}}
"""

# TODO: definir los modelos.
