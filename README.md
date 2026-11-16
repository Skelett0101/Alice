# Cortana: mapa del proyecto

Dos carpetas, dos máquinas:

- `Cortana_Server/` -> Debian. Puente entre OpenClaw y el cliente.
- `Cortana_Client/` -> Windows. La "cara" (chat/avatar), las "manos" (skills) y los "ojos".

## Flujo (conversación en ambos sentidos)

```
Tú (voz/texto) -> Vista -> ws_client -> [WebSocket Tailscale] -> ws_server -> OpenClaw
                                                                         |
Vista <- router <- ws_client <- [WebSocket Tailscale] <- ws_server <-----+
          |  (respuesta: texto + emoción)  /  (orden: acción + parámetros)
          +-> skills (Playwright, Office, sistema...) -> resultado -> OpenClaw
```

El cliente Windows abre la conexión hacia Debian (conexión saliente).
OpenClaw también puede iniciar cosas: manda órdenes a Windows por esa misma conexión.

## Tipos de mensaje (se definen en protocol.py / schemas.py)

| Tipo | Dirección | Para qué |
|---|---|---|
| `mensaje_usuario` | Windows -> Debian | Lo que dices o escribes |
| `respuesta` | Debian -> Windows | Texto + emoción para la vista |
| `orden` | Debian -> Windows | Acción + parámetros a ejecutar |
| `resultado` | Windows -> Debian | Cómo salió la orden |
| `contexto` | Windows -> Debian | Texto de la ventana actual (ojos) |
| `alerta` | ambos | Confirmaciones de seguridad, errores |
| `ping` / `pong` | ambos | Mantener la conexión viva |

## Orden de armado (una cosa a la vez)

1. Protocolo (`schemas.py` y `protocol.py`)
2. Conexión Windows <-> Debian con ping/pong
3. Conectar `openclaw_adapter.py` con tu OpenClaw real
4. Una skill: `abrir_web`
5. Skill de OpenClaw `control_windows`
6. Seguridad (US17)
7. Más skills, luego ojos
8. Vista React provisional, al final Godot
