from _gclick_conn import headers
from urllib.request import Request, urlopen
import json
# import csv
import pandas as pd

# Inicializa variáveis
data_inicio = '20200101'
data_fim = '20260101'
url_base = 'https://api.beteltecnologia.com/recebimentos?data_inicio=' + data_inicio + '&data_fim=' + data_fim
url_base_for = 'https://api.beteltecnologia.com/recebimentos?data_inicio=' + data_inicio + '&data_fim=' + data_fim + '&pagina='

# Configura requisição
request = Request(url_base, headers=headers)

# Realiza a consulta e armazena em uma varíavel
response_body = urlopen(request).read().decode('utf-8')

# Converte a resposta da consulta para JSON
response_json = json.loads(response_body)

# Navega no JSON e coletando os parâmetros de consulta
total_registros = response_json["meta"]["total_registros"]
total_paginas = response_json["meta"]["total_paginas"]
pagina_atual = response_json["meta"]["pagina_atual"]
proxima_url = response_json["meta"]["proxima_url"]
result = []

# INÍCIO TESTES #
print(response_json["meta"])
# FIM TESTES #

for i in range(total_paginas):
    i += 1
    request_for = Request(url_base_for + str(i), headers=headers)
    response_body = urlopen(request_for).read().decode('utf-8')
    response_json = json.loads(response_body)
    # INÍCIO TESTES #
    # print(json.dumps(response_json, indent=4))
    # print(url_base_for + str(i))
    # print(total_paginas)
    # print(total_registros)
    # FIM TESTES #
    result.append(response_json["data"])


# Exibindo o JSON no terminal
# print(json.dumps(response_json, indent=4))

# Save to JSON
try:
    with open("gestao_click_api/recebimentos/recebimentos.json", "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"Error saving JSON: {e}")

# Convert to CSV - Está com erro
# try:
#     with open("recebimentos.csv", "w", newline="", encoding="utf-8") as csv_file:
#         if result:
#             fieldnames = result[0][0][0].keys()
#             writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(result)
# except Exception as e:
#     print(f"Error saving CSV: {e}")