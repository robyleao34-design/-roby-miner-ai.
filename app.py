
import json
import urllib.request
from datetime import datetime

MOEDAS = ["bitcoin", "litecoin", "dogecoin"]

def consultar_precos():
    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=bitcoin,litecoin,dogecoin"
        "&vs_currencies=brl,usd"
    )

    try:
        with urllib.request.urlopen(url, timeout=15) as resposta:
            dados = json.loads(resposta.read().decode())

        print("=== ROBY MINER AI ===")
        print("Consulta:", datetime.now().isoformat())

        for moeda in MOEDAS:
            preco = dados[moeda]
            print(f"\n{moeda.upper()}")
            print(f"Preço em reais: R$ {preco['brl']:.2f}")
            print(f"Preço em dólares: US$ {preco['usd']:.2f}")

    except Exception as erro:
        print("Erro na consulta:", erro)

if __name__ == "__main__":
    consultar_precos()
