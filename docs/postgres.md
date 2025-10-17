# 🧩 Testar Conexão no Postgres de Dentro do Cluster

## Passo 1
kubectl run -it --rm psql-client --image=postgres:15 --namespace=postgres -- bash

## Passo 2
De dentro do pod execute o comando:

psql -h postgres -U <user> -d <nome_do_database>
# senha: admin

---
# 🧩 Acessando do Windows

## Opção 1
Adicione NodePort ou Port Forward:

kubectl port-forward svc/postgres 5432:5432 -n postgres

Ai você consegue:
psql -h localhost -U admin -d acougue

### OBS.: ⚠️ Não é recomendável usar Ingress para PostgreSQL, pois o Ingress só funciona com HTTP/HTTPS.
