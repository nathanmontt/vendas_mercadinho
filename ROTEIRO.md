# Roteiro orientado — Projeto 02: Análise de vendas de um mercadinho

## Situação

Um pequeno mercadinho fictício exportou seu registro de vendas. Seu papel é interpretar a tabela, calcular quantidades e faturamento e investigar dados inconsistentes.

## Antes de programar

- [ ] Abrir o(s) CSV(s) em um editor de texto e identificar delimitador, cabeçalhos e codificação.
- [ ] Anotar o significado de cada coluna e seu tipo de dado esperado.
- [ ] Visualizar poucas linhas, inclusive algumas que parecem problemáticas.
- [ ] Definir o objetivo da análise em uma frase, no diário de bordo.

## Missões em ordem

- [ ] Ler o CSV preservando os campos entre aspas corretamente.
- [ ] Conhecer quais colunas são texto e quais deveriam ser números.
- [ ] Identificar registros com quantidade ou preço ausente, inválido ou negativo.
- [ ] Decidir uma regra para lidar com operações canceladas e registrar a escolha.
- [ ] Calcular receita por linha utilizável e o total geral.
- [ ] Organizar um resumo por categoria e produto sem perder o arquivo original.

## Perguntas de investigação

- Qual categoria representa o maior valor de vendas?
- Quais produtos aparecem com maior frequência?
- Qual é o impacto dos registros problemáticos sobre a análise?

## Dicas de estudo — sem código-resposta

- Separe **leitura**, **validação**, **cálculo** e **apresentação** em etapas claras.
- Lembre-se de que leitura de CSV normalmente gera textos; para calcular, verifique tipos e valores.
- Use a documentação oficial de `csv` e `open` quando não entender os argumentos.
- Não descarte uma linha problemática sem registrar por quê.
- Considere se campos vazios podem ser tratados sem inventar dados.
- Evite Pandas neste primeiro ciclo: o objetivo é exercitar Python puro.

## Perguntas para a revisão do próprio código

- [ ] O programa funciona se for executado de novo na mesma pasta?
- [ ] O arquivo original permaneceu intacto?
- [ ] Fiz o cálculo somente com registros permitidos pela regra que defini?
- [ ] Se alterarem a ordem das linhas, meu programa continua correto?
- [ ] Consigo explicar cada função, variável e decisão sem ler uma solução pronta?
- [ ] O que o programa faz quando encontra valores vazios ou incoerentes?

## O que publicar no GitHub

1. `README.md` preenchido com problema e aprendizados reais.
2. Código criado por você em `src/`.
3. CSV(s) fictícios da pasta `dados/brutos/`.
4. Pequena descrição das decisões de tratamento.
5. Quando estiverem prontos, relatórios gerados por seu programa (sem inventar números).

## Atenção

Pré-requisito: concluir o projeto 1. Há textos com ponto e vírgula dentro de campos entre aspas.
