"""US05 - Servidor WebSocket en Debian (puerto 8765).

Qué hace:
  - Espera la conexión saliente del cliente Windows (por Tailscale).
  - Autentica al cliente con TOKEN_CLIENTE del .env.
  - Reenvía mensaje_usuario / contexto / resultado hacia OpenClaw (openclaw_adapter).
  - Reenvía respuesta / orden de OpenClaw hacia Windows.
  - US06: transmite los logs de error al cliente como mensajes "alerta".

PASO 2: que conecte y responda ping/pong.
"""

# TODO: implementar con la librería `websockets`.
