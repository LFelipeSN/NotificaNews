# NotificaNews
Um simples script responsável por pegar as notícias das últimas 24h do NewsletterOficial e enviar para um canal do Slack mantendo todos bem informados

![Badge concluido](http://img.shields.io/static/v1?label=STATUS&message=%20FINALIZADO&color=GREEN&style=for-the-badge)

## Indice
- [Tecnologias Utilizadas](#tecnologias-utilizadas)

- [Execução](#Execução)

- [Autores](#autores)

- [Créditos](#Créditos)

## Tecnologias Utilizadas
- API do tabnews
- API do slack

# Execução
Execute diretamente o arquivo main.py ou crie um executável

## Criando executável com pyinstaller
```bash
ps> pyinstaller --onefile --console main.py
ps> move .\dist\main.exe .
```

## Removendo pastas e arquivos desnecessárias
```bash
ps> Remove-Item -Recurse -Force build; Remove-Item -Recurse -Force dist; Remove-Item -Force main.spec
```

## Autores
<div align="left">
  <a href="https://github.com/LFelipeSN" target="_blank">
    <img src="https://github.com/LFelipeSN.png" width="64" height="64" alt="LFelipeSN" style="border-radius:50%;margin-top:8px;" />
  </a>
</div>

## Créditos
- [Tabnews](www.tabnews.com.br)
- [Slack](https://api.slack.com/)
