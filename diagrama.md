## Explicación simple

- **Clientes:** envían tareas al sistema.
- **Balanceador:** distribuye las conexiones entre los servidores.
- **Servidores:** reciben las tareas y las entregan a sus workers.
- **Pool de workers:** permite procesar varias tareas en paralelo.
- **RabbitMQ:** se utiliza para la comunicación y el intercambio de mensajes entre servidores.
- **PostgreSQL / S3:** se utilizan para almacenar datos.