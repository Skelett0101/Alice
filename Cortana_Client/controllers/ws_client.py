"""US14 - Conexión del cliente Windows al WebSocket de Debian (PASO 2).

  - Abre la conexión saliente a SERVER_WS_URL y se autentica con el token.
  - Reconecta solo si se cae la red.
  - Lo que llega (respuesta / orden / alerta) se entrega al router.
  - Envía mensaje_usuario, contexto y resultado hacia Debian.
"""

# TODO: implementar con `websockets`.
