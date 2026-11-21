from pathlib import Path
import csv
import statistics as sc
import re
import statistics as sc

def ajuste_produto(valor):
    partes = re.split(
        r"\s+(?=\d+\s*(?:l|kg|g|un)\b)", valor, maxsplit=1, flags=re.I
    )

    nome = partes[0].strip().strip(";")
    tamanho = partes[1].strip() if len(partes) > 1 else ""

    return nome

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

def preparar_forma_pagamento(valor: str) -> str:
    return valor.strip().title()

def ajuste_status(valor: str) -> str:
    return valor.strip().title()

caminho_csv = Path(__file__).parent.parent / "dados" / "brutos" / "vendas_mercadinho.csv"

with caminho_csv.open("r", encoding="utf-8-sig", newline="") as arq:
    leitor = csv.DictReader(arq, delimiter=";")

    print(f"{"ID":<5} | {"DATA":<10} | {"PRODUTO":<13} | {"CATEGORIA":<10} | {"QUANT.":<8} | {"PREÇO":<10} | {"PAGAMENTO":<10} | {"STATUS"} ")
    print('-' * 100)
    for each_line in leitor:
        venda_id = each_line["venda_id"]
        data = each_line["data"]
        produto = ajuste_produto(each_line["produto"])
        categoria = preparar_categoria(each_line["categoria"])
        quantidade = each_line["quantidade"] if each_line["quantidade"] else "SEM INFO"
        preco_unitario = converter_valor(each_line["preco_unitario"])
        forma_pagamento = preparar_forma_pagamento(each_line["forma_pagamento"])
        status = ajuste_status(each_line["status"])

        print(f"{venda_id} | {data} | {produto:<13} | {categoria:<10} | {quantidade:8} | R${preco_unitario:>8} | {forma_pagamento:<10} | {"SEM STATUS" if not status else status}")

    print("\nESTATÍSTICAS")