from _gclick_conn import headers
from urllib.request import Request, urlopen
import json

# Inicializa variáveis
url_base = 'https://api.beteltecnologia.com/recebimentos?data_inicio=20210101&data_fim=20210201&pagina=1'

# Configura requisição
request = Request(url_base, headers=headers)

# Realiza a consulta e armazena em uma varíavel
response_body = urlopen(request).read().decode('utf-8')

# Converte a resposta da consulta para JSON
response_json = json.loads(response_body)

response_json_meta = response_json["meta"]
response_json_data = response_json["data"]

print (response_json)
print (response_json_meta)

# Exibindo o JSON no terminal
print(json.dumps(response_json_meta, indent=4))


# Exibindo o JSON no terminal
# print(json.dumps(response_json, indent=4))

# Save to JSON
try:
    with open("recebimentos_teste.json", "w", encoding="utf-8") as json_file:
        json.dump(response_json_data, json_file, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"Error saving JSON: {e}")
