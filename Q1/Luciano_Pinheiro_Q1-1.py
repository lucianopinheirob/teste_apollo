import json
import csv
import requests

Parametros = {'Host': 'pypi.org', 'Accept': 'application/json'}

Linhas_CSV = []
Projetos = []
Offset = 0

with open('packages.json') as json_file:
    Pacotes = json.load(json_file)
    for row in Pacotes['rows']:
        Projetos.append(row['project'])

for Projeto in Projetos:
    
    Req = requests.get(f'https://pypi.python.org/pypi/{Projeto}/json')
    Req_json = Req.json()
    
    Nome = Req_json['info']['name']
    Versao = Req_json['info']['version']
    Downloads = Req_json['info']['downloads']['last_month']
    Data = Req_json['releases'][Versao][1]['upload_time']
    Linha_CSV = [Nome, Versao, Downloads, Data]
    Linhas_CSV.append(Linha_CSV)
    
    Offset += 1
    if Offset == 50:
        break

with open('Dados_Pacotes.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Nome', 'Versao', 'Downloads', 'Data'])
    for Linha in Linhas_CSV:
        writer.writerow(Linha)


