import json
import os
import emoji

catalogo_produtos = []

def carregarCatalogo():
    global catalogo_produtos
    if os.path.exists("catalogo_produtos.json"):
        with open("catalogo_produtos.json", "r", encoding="utf-8") as arquivo:
            catalogo_produtos = json.load(arquivo)


def salvarCatalogo():
    with open("catalogo_produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(catalogo_produtos, arquivo, ensure_ascii=False, indent=4)

# gera um código pro produto, ex: VOL001, TEN002...
def geradorCodigo(categoria):
    prefixo = (categoria[:3]).upper()
    contador = 1
    for produto in catalogo_produtos:
        if produto["categoria"].lower() == categoria.lower():
            contador += 1
    return f"{prefixo}{contador:03d}"

# categoria do produto
def geraMensagemCategoria(categoria):
    categoria = categoria.lower()
    match categoria:
        case "futebol":
            icone = emoji.emojisize(":soccer_ball:")
        case "vôlei" | "volei":
            icone = emoji.emojize(":volleyball:")
        case "tênis" | "tenis":
            icone = emoji.emojize(":tennis:")
        case "escalada":
            icone = emoji.emojize(":person_climbing:")
        case "paraquedismo":
            icone = emoji.emojize(":parachute:")
        case "náuticos" | "nauticos" | "náutico" | "nautico":
            icone = emoji.emojize(":sailboat:")
        case "mergulho":
            icone = emoji.emojize(":diving_mask:")
        case _:
            icone = emoji.emojize(":package:")
    return f"{categoria.capitalize()} {icone}"

def cadastrarProduto():
    print("\n--- Cadastro de Produto ---")
    nome = input("Nome do produto: ")
    categoria = input("Categoria (futebol, vôlei, tênis, escalada, paraquedismo, náuticos, mergulho): ")

    try:
        preco = float(input("Preço (ex: 99.90): "))
        quantidade = int(input("Quantidade inicial em estoque: "))
    except ValueError:
        print("Preço ou quantidade inválidos, cadastro cancelado.")
        return

    codigo = geradorCodigo(categoria)

    produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": quantidade
    }

    catalogo_produtos.append(produto)
    salvarCatalogo()

    print(f"\nProduto cadastrado! Código: {codigo}")
    print(f"Categoria: {geraMensagemCategoria(categoria)}")