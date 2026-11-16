# control_windows

Skill de OpenClaw para manejar la PC con Windows.

## Cuándo usarla
Cuando el usuario pida abrir páginas, manejar archivos, Office, el volumen,
cerrar aplicaciones o revisar lo que hay en su pantalla.

## Cómo funciona
Manda la orden al puente local (`local_api.py`), que la reenvía al cliente
Windows. Devuelve el resultado de la ejecución.

## Acciones disponibles
(Se irán agregando una a una; empezar solo con `abrir_web`.)

| accion | parametros | US |
|---|---|---|
| `abrir_web` | `{"url": "..."}` | US21 |

> Verifica el formato exacto de skills en la documentación de tu versión de OpenClaw.
