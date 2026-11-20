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

    return nome
    # return re.sub(
    #     r"\s*(?:;\s*)?\d+\s*(?:l|kg|g|un)\b.*$",
    #     "",
    #     valor,
    #     flags=re.I
    # ).strip()

def preparar_categoria(valor: str) -> str:
    return valor.strip().title()

def converter_valor(valor: str) -> float:
    valor = valor.strip().title()
    if not valor:
        return 0.0

    try:
        valor = valor.replace(".","").replace(",",".")
        valor_transformado = float(valor)
        if valor_transformado < 0:
            return abs(valor_transformado)
        else:
            return valor
    except ValueError:
        return 0.0

    # valor2 = float(valor.replace(",","."))
    # if valor2 < 0:
    #     return 0.0

    # return float(valor.replace(",","."))

caminho_csv = Path(__file__).parent.parent / "dados" / "brutos" / "vendas_mercadinho.csv"

with caminho_csv.open("r", encoding="utf-8-sig", newline="") as arq:
    leitor = csv.DictReader(arq, delimiter=";")

    for each_line in leitor:
        venda_id = each_line["venda_id"]
        data = each_line["data"]
        produto = ajuste_produto(each_line["produto"])
        categoria = preparar_categoria(each_line["categoria"])
        quantidade = each_line["quantidade"] if each_line["quantidade"] else "SEM QUANTIDADE"
        preco_unitario = converter_valor(each_line["preco_unitario"])
        forma_pagamento = each_line["forma_pagamento"]
        status = each_line["status"]

        # print(produto, end=" | ")
        print(venda_id, produto, categoria, quantidade, preco_unitario)

        # print(venda_id, data, produto, categoria, quantidade, preco_unitario, forma_pagamento, status)