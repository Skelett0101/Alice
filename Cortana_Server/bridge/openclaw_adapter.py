"""Unión entre el puente y OpenClaw (PASO 3).

Dirección Windows -> OpenClaw:
  Recibe el mensaje_usuario del cliente y se lo entrega a OpenClaw.

Dirección OpenClaw -> Windows:
  Cuando OpenClaw contesta, arma una "respuesta" (texto + emoción) y,
  si OpenClaw decidió hacer algo en la PC, una "orden".

Qué falta decidir (revisar la documentación de tu versión de OpenClaw):
  - Cómo se le entrega un mensaje (API/gateway, CLI, canal propio como el de WhatsApp).
  - Cómo se le pide que conteste en JSON con emoción (US09).
"""

# TODO: implementar cuando el protocolo y la conexión ya funcionen.
