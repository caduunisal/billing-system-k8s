# billing-system-k8s
Sistema de Billing de Telefonia com Kubernetes e Docker

Este projeto simula um ambiente de produção com Docker e Kubernetes, utilizando Flask como backend e MongoDB como banco de dados.


## Funcionalidades
- API simples que retorna fatura de cliente
- Backend containerizado com Docker
- Orquestração de pods com Kubernetes (Minikube)
- Serviço exposto via NodePort

## Como executar
1. Subir cluster local com Minikube
2. Rodar:
```bash
kubectl apply -f k8s/
minikube service backend-service
```

3. Acessar rota `/billing`



docker build -t caduunisal/billing-backend:v1 .
docker push caduunisal/billing-backend:v1
docker login
docker push caduunisal/billing-backend:v1
