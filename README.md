# Análise de vendas de um mercadinho

> Operações numéricas e resumos simples  
> Projeto de aprendizado em Python puro (biblioteca padrão), com dados fictícios e intencionalmente imperfeitos.

## Contexto

Um pequeno mercadinho fictício exportou seu registro de vendas. Seu papel é interpretar a tabela, calcular quantidades e faturamento e investigar dados inconsistentes.

## Objetivo

Construir um programa de linha de comando que transforme os arquivos brutos em informações úteis, com critérios explícitos de tratamento de dados.

## Ferramentas previstas

- Linguagem: **Python**
- Editor: **VS Code**
- Conhecimentos praticados: `csv.DictReader` , `int/float e normalização de vírgula` , `soma e média` , `formatação no terminal` , `condicionais`.

## Arquivos de entrada

Veja os arquivos na pasta `dados/brutos/`. Leia-os como **texto CSV separado por `;`**. Não modifique o conteúdo original para fazer seu código funcionar.

## Requisitos do projeto

- [x] Conhecer quais colunas são texto e quais deveriam ser números.
- [x] Identificar registros com quantidade ou preço ausente, inválido ou negativo.
- [x] Decidir uma regra para lidar com operações canceladas e registrar a escolha.
- [ ] Calcular receita por linha utilizável e o total geral.
- [ ] Organizar um resumo por categoria e produto sem perder o arquivo original.

## Perguntas que a análise deve ajudar a responder

- Qual categoria representa o maior valor de vendas?
- Quais produtos aparecem com maior frequência?
- Qual é o impacto dos registros problemáticos sobre a análise?

## Como executar

**Depois de implementar:** abra o terminal na raiz deste projeto e execute `python src/main.py` (ou `py src/main.py` no Windows). O código inicial contém apenas TODOs e não produz análise.

## Saídas esperadas

- Um resumo legível no terminal.
- Um registro das decisões de limpeza em `docs/DIARIO.md`.

## Estrutura

```text
Código principal: src/main.py
Dados brutos: dados/brutos/
Diário de bordo: docs/DIARIO.md
```

## Aprendizados e resultados — preencher ao concluir

**O que aprendi:** uso mais aprimorado das funções  
**Problemas encontrados:** formatações incorretas, tantos em _strings_ quanto em números  
**Resultados principais:** limpesa dos daddos (_data cleasing_)
**O que melhoraria:** exportação em pdf dos dados limpos

## Nota sobre os dados

Todos os dados são sintéticos, produzidos exclusivamente para estudo. Não contêm dados reais de clientes, alunos ou empresas. Não há gabarito no repositório.
