import requests, json
import pandas as pd

url = 'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'
data = requests.get(url)
data_dict = json.loads(data.content)

candidato = []
votos = []
porcentagem = []

for cand in data_dict['cand']:

    candidato.append(cand['nm'])
    votos.append(int(cand['vap']))
    porcentagem.append(float(cand['pvap'].replace(',', '.')))

df = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=['Candidato', 'Votos', 'Porcentagem (%)'])

df.to_csv('dados-eleicao.csv', index=False)


