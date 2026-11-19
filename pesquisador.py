
import json
import urllib.request
from datetime import datetime, timezone

PLATAFORMAS = [
    {
        "nome": "Clickworker",
        "tipo": "Microtarefas",
        "url": "https://www.clickworker.com/"
    },
    {
        "nome": "Toloka",
        "tipo": "Avaliação de dados",
        "url": "https://toloka.ai/"
    },
    {
        "nome": "Prolific",
        "tipo": "Pesquisas remuneradas",
        "url": "https://www.prolific.com/participants"
    },
    {
        "nome": "UserTesting",
        "tipo": "Testes de sites e aplicativos",
        "url": "https://www.usertesting.com/get-paid-to-test"
    },
    {
        "nome": "ySense",
        "tipo": "Pesquisas e ofertas",
        "url": "https://www.ysense.com/"
    }
]

relatorio = {
    "atualizado_em": datetime.now(timezone.utc).isoformat(),
    "pais": "Brasil",
    "investimento_necessario": 0,
    "aviso": "Disponibilidade e ganhos dependem das regras de cada plataforma.",
    "oportunidades": []
}

for plataforma in PLATAFORMAS:
    item = dict(plataforma)
    item["site_verificado"] = False

    try:
        req = urllib.request.Request(
            item["url"],
            headers={"User-Agent": "RobyMinerAI/1.0"}
        )
        with urllib.request.urlopen(req, timeout=15) as resposta:
            item["site_verificado"] = resposta.status == 200
    except Exception:
        pass

    relatorio["oportunidades"].append(item)

with open("relatorio.json", "w", encoding="utf-8") as arquivo:
    json.dump(relatorio, arquivo, ensure_ascii=False, indent=2)

print("=== ROBY MINER AI ===")
print("Relatório atualizado.")
print("Oportunidades cadastradas:", len(PLATAFORMAS))
print("Arquivo criado: relatorio.json")
