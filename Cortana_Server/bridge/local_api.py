"""API local en Debian (solo loopback, puerto LOCAL_API_PORT).

La usa la skill `control_windows` de OpenClaw para mandar una orden al
cliente Windows sin hablar WebSocket:

    POST http://127.0.0.1:8766/orden   {"accion": "...", "parametros": {...}}
    -> el puente la envía por el WebSocket y devuelve el "resultado".

Es opcional: si tu OpenClaw ya soporta conectar dispositivos/nodos,
quizá no necesites esta pieza.
"""

# TODO: implementar en el PASO 5.
