# PFO 3 - Rediseño como Sistema Distribuido

Solución simple realizada en Python usando sockets y un pool de workers.

## Archivos

- `servidor.py`: recibe conexiones por socket y distribuye clientes entre workers.
- `cliente.py`: envía tareas al servidor y recibe resultados.
- `diagrama.md`: contiene la explicación al diagrama solicitado.

## Requisitos

Solo se necesita Python 3.

No hace falta instalar librerías externas.

## Ejecutar

### 1. Iniciar el servidor

Abrir una terminal:

```bash
python servidor.py
```

Debe aparecer:

```text
Servidor escuchando en localhost:5000
```

### 2. Ejecutar el cliente

Abrir otra terminal:

```bash
python cliente.py
```

Ejemplo:

```text
Ingrese una tarea o escriba "salir": hola mundo
Servidor: Resultado: HOLA MUNDO
```

Para terminar:

```text
salir
```

## Funcionamiento

1. El cliente se conecta al servidor mediante un socket.
2. Envía una tarea.
3. El servidor acepta la conexión.
4. La conexión se entrega a un worker del pool.
5. El worker procesa la tarea.
6. El servidor devuelve el resultado al cliente.

## Pool de workers

El servidor utiliza:

```python
ThreadPoolExecutor(max_workers=4)
```

Esto permite atender hasta 4 clientes de forma concurrente.

Cada conexión aceptada se envía al pool con:

```python
workers.submit(manejar_cliente, cliente, direccion)
```

De esta manera el servidor puede seguir aceptando nuevas conexiones mientras otros workers están procesando tareas.

## Arquitectura distribuida

El archivo `DiagramaPR.drawio.png` incluye:

- Clientes web o móviles.
- Balanceador Nginx/HAProxy.
- Servidores con pool de workers.
- RabbitMQ.
- PostgreSQL.
- S3.