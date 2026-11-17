from pathlib import Path
import csv
import statistics as sc
import re

def ajuste_produto(valor):
    if re.search(r"\s", valor):
        return valor

caminho_csv = Path(__file__).parent.parent / "dados" / "brutos" / "vendas_mercadinho.csv"

with caminho_csv.open("r", encoding="utf-8-sig", newline="") as arq:
    leitor = csv.DictReader(arq, delimiter=";")

    for each_line in leitor:
        venda_id = each_line["venda_id"]
        data = each_line["data"]
        produto = ajuste_produto(each_line["produto"])
        # produto = each_line["produto"]
        categoria = each_line["categoria"]
        quantidade = each_line["quantidade"]
        preco_unitario = each_line["preco_unitario"]
        forma_pagamento = each_line["forma_pagamento"]
        status = each_line["status"]

        # print(produto, end=" | ")
        print(venda_id, produto)

        # print(venda_id, data, produto, categoria, quantidade, preco_unitario, forma_pagamento, status)