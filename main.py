import requests
from config import *
from datetime import datetime, timezone

resposta = requests.get(urlNewsletter, parametrosBusca)
dataAtual = datetime.now(timezone.utc)
mensagem = f"{emojis['relógio_3']} *Notícias das últimas 24 horas:*"

if resposta.status_code != 200: 
    input("Parece que ocorreu um erro ao se conectar com o servidor", resposta.status_code)
    exit()

posts = resposta.json()
for post in posts:
    data_criacao = datetime.fromisoformat(post["created_at"].replace("Z", "+00:00"))
    horas_de_publicacao = int((dataAtual - data_criacao).total_seconds()/3600)
    
    if (horas_de_publicacao) <= 24:#posts das ultimas 24h  
        mensagem += f"""\n
            {emojis['jornal']} *{post['title']}*\n
            {emojis['link']} mais informações: <https://www.tabnews.com.br/{post['owner_username']}/{post['slug']} | {post['slug']}>\n\n
            """

print(f"Mensagem:\n {mensagem}")     
payload = {"text": mensagem}
resposta_mensagem = requests.post(urlSlack, json=payload)
input(f"Reposta :: {resposta_mensagem.text}")