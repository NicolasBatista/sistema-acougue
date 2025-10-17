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

---
#### Passo 4
Mapear os serviços no Ingress

Utilizar o arquivo ingress-mult.yaml e se estiver usando kind no windows, não se esquecer de editar o C:\Windows\System32\drivers\etc, ex.:

127.0.0.1 web1.local
127.0.0.1 web2.local
127.0.0.1 api.local
