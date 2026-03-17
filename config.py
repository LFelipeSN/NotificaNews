import json

with open("config.json", "r", encoding="utf-8") as f:
    configuracoes = json.load(f)

urlNewsletter = configuracoes["urls"]["newsletter"]
urlSlack = os.getenv("URL_SLACK") or configuracoes["urls"]["slack"]
parametrosBusca = configuracoes["parametros"]
emojis = configuracoes["emojis"]
