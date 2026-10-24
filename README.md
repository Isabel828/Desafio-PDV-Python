# Desafio Nível 1 — PDV com Descontos (Python)

**Participante:** Isabel Conceição Sousa  
**Trilha:** Desenvolvimento Backend  
**GitHub:** [Isabel828](https://github.com/Isabel828)

## O que o código faz
O programa simula um ponto de venda que registra compras, aplica descontos progressivos conforme a idade do cliente e o valor da compra e apresenta um resumo financeiro ao encerrar.

## Como ele faz
1. Recebe o valor da compra; zero encerra o programa.
2. Solicita a idade e valida entradas negativas.
3. Aplica 20% de desconto se a idade for maior ou igual a 65.
4. Aplica 10% extra se o valor já descontado for maior que R$ 100,00.
5. Exibe o valor final com duas casas decimais.
6. Guarda cada compra em uma lista usando `.append()`.
7. Ao terminar, soma o total bruto, descontos e total final.

Usa `while`, `if`, `continue`, `for` e lista, sem `def` ou `try/except`.

## Como rodar
No terminal, dentro da pasta `nivel_1`:

```bash
python pdv.py
```

Digite o valor e a idade para cada compra. Digite `0` como valor para terminar.

## Casos de teste oficiais

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|---:|---:|---:|---:|---:|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

### Casos-limite
- R$ 125,00, idade 70: resultado R$ 100,00 (sem desconto extra).
- R$ 101,00, idade 30: resultado R$ 90,90.
- R$ 200,00, idade 64: resultado R$ 180,00.

## Estrutura de entrega
```text
nivel_1/
├── pdv.py
└── README.md
```
