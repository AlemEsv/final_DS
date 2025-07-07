#!/bin/bash

echo "Desplegando aplicación..."

# Iniciar minikube
echo "Iniciando Minikube..."
minikube start --driver=docker

# Configurar Docker para Minikube
minikube -p minikube docker-env | Invoke-Expression

# Construir imágenes
echo "Construyendo imágenes..."
docker-compose build

# Aplicar configuraciones de Kubernetes
echo "Aplicando manifiestos..."
kubectl apply -f kubernetes/

# Mostrar información de acceso
minikube service apps-service --url