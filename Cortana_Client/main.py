"""Arranca todo el cliente en Windows (US14).

Orden de arranque:
  1. Cargar .env
  2. Levantar ui_bridge (WebSocket local para la vista)
  3. Conectar ws_client al servidor Debian (con reconexión automática)
  4. Dejar el router escuchando órdenes
"""

# TODO: implementar con asyncio cuando existan ws_client y ui_bridge.
