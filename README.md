# 🥩 Sistema para Açougue — Projeto de Observabilidade e Microsserviços

Este é um **projeto pessoal** com o objetivo de construir um sistema moderno para gestão de açougue, aplicando conceitos de **microserviços**, **Kubernetes (Kind)** e **observabilidade**.

O sistema foi idealizado tanto como um **laboratório técnico** quanto uma **solução prática**, inspirada em um caso real — o açougue dos meus pais, que atualmente usa um sistema legado e instável.

---

## 🚀 Objetivos do Projeto

- Aprender e aplicar **Git, Kubernetes e CI/CD**
- Demonstrar **boas práticas de arquitetura de microsserviços**
- Integrar **observabilidade com Datadog**
- Criar um ambiente realista de **produção simulada**

---

## 🧭 Domínios do Sistema

O sistema foi dividido em **4 domínios principais**, cada um responsável por uma área funcional:

| Domínio                      | Objetivo                                             | Exemplos de Dados                   |
| ---------------------------- | ---------------------------------------------------- | ----------------------------------- |
| 🔐 **Usuários e Autenticação**  | Gerenciar acesso, papéis e credenciais               | Usuários, Permissões, Tokens        |
| 🥩 **Catálogo e Estoque**       | Gerenciar produtos e movimentações de estoque        | Produtos, Categorias, Movimentações |
| 💳 **Pagamentos e Vendas**      | Registrar transações e processar pagamentos          | Pedidos, Itens, Pagamentos          |
| 💰 **Faturamento e Financeiro** | Consolidar receitas e despesas                       | Lançamentos, Relatórios, Saldo      |

---

## 🧩 Arquitetura de Microsserviços

Cada módulo é isolado e comunicará via HTTP e RabbitMQ (eventos assíncronos).

| Serviço                      | Linguagem         | Responsabilidade Principal                         | Banco de Dados |
| ----------------------------- | ----------------- | --------------------------------------------------- | --------------- |
| 🧑‍💼 **auth-service**        | Python (FastAPI)  | Cadastro, login, JWT, permissões                    | PostgreSQL      |
| 🥩 **product-service**        | Python (FastAPI)  | CRUD de produtos, categorias                        | PostgreSQL      |
| 📦 **inventory-service**      | Python (FastAPI)  | Movimentações e controle de estoque                 | PostgreSQL      |
| 💳 **sales-service**          | Python (FastAPI)  | Registro de pedidos, cálculo de totais              | PostgreSQL      |
| 💰 **payment-service**        | Python (FastAPI)  | Simulação e registro de pagamentos                  | PostgreSQL      |
| 📊 **finance-service**        | Python (FastAPI)  | Lançamentos e relatórios financeiros                | PostgreSQL      |
| 🌐 **frontend-gateway**       | Node.js (Next.js) | Interface web e proxy das APIs                      | —               |
| 🧠 **api-gateway (opcional)** | FastAPI/Express   | Unificação e controle global de acesso              | —               |

---

## 🔀 Fluxo de Comunicação entre Serviços

<p align="center">
  <img src="https://github.com/user-attachments/assets/ce6db163-39cb-4b0f-903f-b23b37efb5de" width="800" alt="Fluxo entre microserviços">
</p>

---

## ☸️ Infraestrutura no Kind (Kubernetes in Docker)

<p align="center">
  <img src="https://github.com/user-attachments/assets/39e8fd09-6b73-4e1a-9d36-cda4dd670d4f" width="800" alt="Infraestrutura Kind">
</p>

Cada serviço é implementado como:
- `Deployment` + `Service`  
- `Ingress Controller (NGINX)` para roteamento externo  
- `RabbitMQ` para mensageria  
- `Postgres` como `StatefulSet`  
- `Datadog Agent` como `DaemonSet`

---

### 🧱 Estrutura da Infraestrutura (Kind Cluster)

O ambiente local utiliza o **Kind** como orquestrador Kubernetes, com todos os serviços agrupados no namespace `acougue-system`.

| Tipo                | Nome do Componente        | Função Principal                           |
| ------------------- | ------------------------- | ------------------------------------------- |
| 🧩 Namespace        | `acougue-system`          | Agrupa todos os recursos do sistema         |
| 🔐 Deployment       | `auth-service`            | Autenticação e controle de acesso           |
| 🥩 Deployment       | `product-service`         | Gerenciamento de produtos                   |
| 📦 Deployment       | `inventory-service`       | Controle de estoque                         |
| 🧾 Deployment       | `sales-service`           | Processamento de vendas                     |
| 💳 Deployment       | `payment-service`         | Simulação e registro de pagamentos          |
| 💰 Deployment       | `finance-service`         | Consolidação financeira e relatórios        |
| 🌐 Deployment       | `frontend`                | Interface administrativa em Next.js         |
| 🐘 StatefulSet      | `postgres`                | Banco de dados central (PostgreSQL)         |
| 🐇 Deployment       | `rabbitmq`                | Mensageria para eventos assíncronos         |
| 🐶 DaemonSet        | `datadog-agent`           | Observabilidade (métricas, logs, traces)    |
| 🌍 Deployment       | `ingress-controller`      | Gerencia o tráfego externo (NGINX)          |


---

## ⚙️ Detalhamento dos Serviços

### 🔐 Auth Service
- CRUD de usuários  
- Login/logout com JWT  
- Controle de papéis: estoquista, vendedor, admin  
- Middleware de autenticação compartilhado  

### 🥩 Product Service
- CRUD de produtos e categorias  
- Integração com estoque  
- Eventos `product.created` / `product.updated` via RabbitMQ  

### 📦 Inventory Service
- Registro de entradas e saídas  
- Sincronização com `sales-service`  
- Endpoint `/inventory/movements`  

### 🧾 Sales Service
- Registro de pedidos e itens  
- Cálculo automático de totais  
- Evento `sale.completed` emitido ao finalizar  

### 💳 Payment Service
- Processa eventos de venda  
- Simula pagamentos (PIX, débito, crédito)  
- Atualiza status no `sales-service`  

### 💰 Finance Service
- Registra despesas e receitas  
- Gera relatórios e gráficos de lucro  
- Consolidação de dados por período  

### 🌐 Frontend Gateway
- Interface administrativa (Next.js)  
- Dashboard com **Recharts / Chart.js**  
- CRUDs completos (produtos, usuários, vendas)

---

## 📈 Observabilidade e Escalabilidade

A arquitetura foi projetada para suportar:
- 🚀 **Escalabilidade horizontal** (via HPA)  
- 🐇 **Mensageria resiliente** (RabbitMQ)  
- 📊 **Monitoramento e tracing** (Datadog)  
- 🔁 **Deploy e rollback independentes**  

---

> 💡 *"A melhor forma de aprender arquitetura é construindo algo real."*  
> — *Nicolas Costa*

