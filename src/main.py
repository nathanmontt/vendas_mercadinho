from pathlib import Path
import csv
import statistics as sc
import re

def ajuste_produto(valor):
    partes = re.split(
        r"\s+(?=\d+\s*(?:l|kg|g|un)\b)", valor, maxsplit=1, flags=re.I
    )

    nome = partes[0].strip().strip(";")
    tamanho = partes[1].strip() if len(partes) > 1 else ""

    return nome, tamanho
    # return re.sub(
    #     r"\s*(?:;\s*)?\d+\s*(?:l|kg|g|un)\b.*$",
    #     "",
    #     valor,
    #     flags=re.I
    # ).strip()

caminho_csv = Path(__file__).parent.parent / "dados" / "brutos" / "vendas_mercadinho.csv"

with caminho_csv.open("r", encoding="utf-8-sig", newline="") as arq:
    leitor = csv.DictReader(arq, delimiter=";")

    for each_line in leitor:
        venda_id = each_line["venda_id"]
        data = each_line["data"]
        produto = ajuste_produto(each_line["produto"])
        categoria = each_line["categoria"]
        quantidade = each_line["quantidade"]
        preco_unitario = each_line["preco_unitario"]
        forma_pagamento = each_line["forma_pagamento"]
        status = each_line["status"]

        # print(produto, end=" | ")
        print(venda_id, produto)

        # print(venda_id, data, produto, categoria, quantidade, preco_unitario, forma_pagamento, status)