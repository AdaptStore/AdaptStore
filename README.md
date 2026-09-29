# 🛒 AdaptStores

Sistema de terminal para cadastro de produtos, controle de estoque e consulta por categoria, desenvolvido em Python.

> A sua organização inteligente começa aqui.

## Funcionalidades

- **Cadastrar produto**: registra nome, categoria, preço e quantidade inicial em estoque.
- **Controle de estoque**: informa o código do produto, escolhe entre entrada (1) ou saída (2) e digita a quantidade. Se a saída for maior que o estoque disponível, a operação é bloqueada, então o estoque nunca fica negativo.
- **Listar produtos por categoria**: exibe código, nome, preço e estoque de todos os produtos da categoria escolhida.
- Geração automática do código do produto a partir da categoria (ex: `FUT001`).
- Emoji temático de acordo com a categoria informada (Futebol, Basquete, Vôlei, Tênis, Escalada, Paraquedismo, Náuticos, Mergulho). Qualquer outra categoria também é aceita e recebe o emoji de pacote 📦.
- Validação das entradas numéricas (preço, quantidade e opções do menu).
- Persistência dos dados em arquivo `catalogo_produtos.json`.

## Como o código do produto é gerado

O código é formado pelas 3 primeiras letras da categoria (em maiúsculo) + um número de 3 dígitos. Esse número é a quantidade de produtos já cadastrados na mesma categoria + 1, então cada categoria tem a sua própria contagem.

Exemplos:

- primeiro produto de `futebol` → `FUT001`
- segundo produto de `futebol` → `FUT002`
- primeiro produto de `basquete` → `BAS001`

No controle de estoque, digite o código exatamente como ele foi gerado (em maiúsculo), porque a busca diferencia maiúsculas de minúsculas.

## Categorias e emojis

| Categoria    | Emoji |
|--------------|-------|
| Futebol      | ⚽    |
| Basquete     | 🏀    |
| Vôlei        | 🏐    |
| Tênis        | 🎾    |
| Escalada     | 🧗    |
| Paraquedismo | 🪂    |
| Náuticos     | ⛵    |
| Mergulho     | 🤿    |
| Outras       | 📦    |

Vôlei, tênis e náuticos também são reconhecidos sem acento (ex: `volei`, `tenis`, `nauticos`).

## Requisitos

- Python 3.10+ (o projeto usa `match/case`, disponível a partir do Python 3.10)
- Biblioteca:
  - [`emoji`](https://pypi.org/project/emoji/)
- Terminal do Windows: o script limpa a tela com `cls` ao iniciar. No Linux/macOS, troque por `clear` no começo do arquivo.

Instalação da dependência:

```bash
pip install emoji
```

## Como executar

```bash
python AdaptStore.py
```

## Estrutura do projeto

```
├── AdaptStore.py            # Arquivo principal (funções do sistema, menu e loop do programa)
└── catalogo_produtos.json   # Base de dados dos produtos (gerado automaticamente)
```

## Menu principal

```
===== AdaptStores =====
A sua organização inteligente começa aqui
1 -> Cadastrar produto
2 -> Controle de estoque
3 -> Listar produtos por categoria
4 -> Sair
=======================
```
