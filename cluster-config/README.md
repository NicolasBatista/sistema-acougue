# 🧩 Instalar o NGINX Ingress Controller (no Kind)

O Kind não cria LoadBalancer automaticamente, então o NGINX precisa ser exposto via NodePort.

---
#### Passo 1
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

---
#### Passo 2
kubectl get pods -n ingress-nginx

Deve aparecer algo assim:
NAME                                        READY   STATUS    RESTARTS   AGE
ingress-nginx-controller-xxxxx              1/1     Running   0          1m

---
#### Passo 3
Teste o Ingress:
kubectl get svc -n ingress-nginx

Procure por:
ingress-nginx-controller   NodePort   80:xxxxx/TCP   443:yyyyy/TCP

💡 Esses números são as portas que você usará no localhost para acessar seus serviços no Kind (geralmente 8080 → 80).