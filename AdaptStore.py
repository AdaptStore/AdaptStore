import json
import emoji

catalogo_produtos = []

# Função que carrega o arquivo .json do catálogo.
def carregarCatalogo():
    try:
        with open("catalogo.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Função que salva o catalogo no arquivo .json.
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

# localiza o produto pelo código e ajusta o estoque
def atualizarEstoque(catalogo, codigo, quantidade):
    for produto in catalogo:
        if produto["codigo"] == codigo:
            novoEstoque = produto["estoque"] + quantidade
            if novoEstoque < 0:
                print("Não dá pra deixar o estoque negativo.")
                return False
            produto["estoque"] = novoEstoque
            salvarCatalogo()
            print(f"Estoque de '{produto['nome']}' atualizado para {novoEstoque} unidades.")
            return True
    print("Produto não encontrado.")
    return False

def menuEstoque():
    print("\n--- Controle de Estoque ---")
    codigo = input("Código do produto: ")
    print("1 - Entrada de produtos")
    print("2 - Saída de produtos")
    tipo = input("Opção: ")

    try:
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Quantidade inválida.")
        return

    if tipo == "2":
        quantidade = -quantidade

    atualizarEstoque(catalogo_produtos, codigo, quantidade)