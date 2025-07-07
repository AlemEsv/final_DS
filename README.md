# Migración y orquestación de una aplicación híbrida

## Prerrequisitos

- Docker Desktop
- Minikube

## Ejecución

```bash
# Clonar el repositorio
git clone https://github.com/AlemEsv/final_DS.git
cd final_DS

# Ejecutar script de despliegue
./operate.sh
```

## Acceso a las aplicaciones

- **Aplicación Legacy**: Puerto 5000
- **Microservicio**: Puerto 5001
- **Base de datos PostgreSQL**: Puerto 5432

El script automáticamente:

1. Inicia Minikube
2. Construye las imágenes Docker
3. Despliega en Kubernetes
4. Muestra la URL de acceso

## Contenido de aplicación

### `app-legacy`

- `URL:PUERTO/app`: muestra el estado de la aplicación monolitica

- `URL:PUERTO/app/users`: muestra los usuarios de la base de datos conectada con la aplicación monolítica.

### `new-microservice`

- `URL:PUERTO/api`: muestra el estado del microservicio

- `URL:PUERTO/api/users`: Espera respuesta de la aplicación monolítica para poder usar la base de datos, conectarla y mostrar los usuarios tenidos.

Declaro que esta entrega fue realizada de forma individual, sin asistencia externa, sin herramientas de generación automática, y cumpliendo con todas las reglas del examen.
