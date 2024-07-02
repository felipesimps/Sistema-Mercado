produtos = [
    {"codigo":1, "nome": "Carne", "preco": 38.00, "estoque": 50 },
    {"codigo":2, "nome": "Frango", "preco": 22.00, "estoque": 50 },
    {"codigo":3, "nome": "Leite", "preco": 4.50, "estoque": 60 },
    {"codigo":4, "nome": "Pão", "preco": 2.0, "estoque": 50 },
    {"codigo":5, "nome": "Queijo", "preco": 17.00, "estoque": 30 },
    {"codigo":6, "nome": "Arroz", "preco": 20.00, "estoque": 100 },
    {"codigo":7, "nome": "Feijão", "preco": 15.00, "estoque": 100 },
    {"codigo":8, "nome": "Sal", "preco": 12.00, "estoque": 110 },
    {"codigo":9, "nome": "Açucar", "preco": 10.00, "estoque": 90 },
    {"codigo":10, "nome": "Café", "preco": 18.00, "estoque": 80},
]


usuarios = []
carrinho = []

historico_compras = []

def cadastrar_usuario(nome, email, senha):
    novo_usuario = {"nome": nome, "email": email, "senha": senha, "carrinho": []}
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")


def login_usuario(email, senha):
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            return usuario
    return None
    

def mostrar_catalogo():
    print("--- Catálogo de Produtos ---")
    for produto in produtos:
        print(f"Código: {produto['codigo']} | Nome: {produto['nome']} | Preço: R${produto['preco']:.2f} | Estoque: {produto['estoque']} ")
    
    
def adicionar_produto_carrinho(usuario, codigo_produto, quantidade):
    produto = buscar_produto_por_codigo(codigo_produto)
    if produto:
        if quantidade > 0 and quantidade <= produto['estoque']:
            carrinho.append({"usuario": usuario, "produto": produto, "quantidade": quantidade})
            print(f"Produto '{produto['nome']}' adicionado ao carrinho. ")
        else:
            print("Quantidade inválida ou produto sem estoque suficiente.")
    else:
        print("Produto não encontrado.")


def remover_produto_carrinho(usuario, codigo_produto):
    for item in carrinho:
        if item["usuario"] == usuario and item["produto"]["codigo"] == codigo_produto:
            carrinho.remove(item)
            print(f"Produto removido do carrinho. ")
            return
    print("Produto não encontrado no carrinho.")


def visualizar_carrinho(usuario):
    total = 0
    print("--- Carrinho de compras ---")
    for item in carrinho:
        if item["usuario"] == usuario:
            produto = item["produto"]
            quantidade = item["quantidade"]
            subtotal = produto["preco"] * quantidade
            total += subtotal
            print(f"Produto: {produto['nome']} | Quantidade: {quantidade} | Subtotal: R${subtotal:.2f}") 
    print(f"Total do carrinho: R${total:.2f}")


def processar_compra(usuario):
    total = 0
    formas_pagamento = ["Débito", "Crédito", "Pix"]

    print("--- Formas de Pagamento ---")
    for i in range(len(formas_pagamento)):
        print(f"{i+1}. {formas_pagamento[i]}")


    while True:
        opcao = input("\nEscolha a forma de pagamento (Digite uma das opções): ")
        if opcao.isdigit() and 1 <= int(opcao) <= len(formas_pagamento):
            forma_pagamento = formas_pagamento[int(opcao) - 1]
            break
        else:
            print("Opção inválida. Escolha um número válido")


    for item in carrinho:
        if item["usuario"] == usuario:
            produto = item["produto"]
            quantidade = item["quantidade"]
            subtotal = produto["preco"] * quantidade
            total += subtotal
            produto["estoque"] -= quantidade
            historico_compras.append({"usuario": usuario["nome"], "produto": produto["nome"], "quantidade": quantidade, "subtotal": subtotal, "forma_pagamento": forma_pagamento})
    carrinho[:] = []
    print("Compra realizada com sucesso!")


def mostrar_historico_compras():
    print("--- Histórico de Compras ---")
    for compra in historico_compras:
        print(f"Usuário: {compra['usuario']} | Produto: {compra['produto']} | Quantidade: {compra['quantidade']} | Subtotal: R${compra['subtotal']:.2f} | Forma de pagamento: {compra['forma_pagamento']}")


def administrar_estoque():
    print("--- Administração de Estoque ---")
    for produto in produtos:
        print(f"Produto: {produto['nome']} | Estoque: {produto['estoque']}")


def buscar_produto_por_codigo(codigo):
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto
    return None
    

def menu_opcoes():
    while True:
        print("\n--- Menu de opções ---")
        print("1. Cadastrar Usuário ")
        print("2. Login de usuário ")
        print("3. Mostrar Catálogo de Produtos ")
        print("4. Adicionar produto ao carrinho ")
        print("5. Remover produto do carrinho ")
        print("6. Visualizar carrinho ")
        print("7. Processar compra ")
        print("8. Mostrar Histórico de compras ")
        print("9. Administração de estoque ")
        print("0. Sair do sistema ")
    
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do ususário: ")
            email = input("Digite o email do usuário: ")
            senha = input("Digite a senha do ususário: ")
            cadastrar_usuario(nome, email, senha)


        elif opcao == "2":
            email = input("Digite o email do usuário: ")
            senha = input("Digite a senha do usuário: ")
            usuario_logado = login_usuario(email, senha)
            if usuario_logado:
                print(f"Login realizado com sucesso,{usuario_logado['nome']}!")
            else:
                print("Email ou senha incorretos.")


        elif opcao == "3":
            mostrar_catalogo()


        elif opcao == "4":
            if not usuarios:
                print("Faça o login primeiro para adicionar produtos ao carrinho.")
            else:
                mostrar_catalogo()
                codigo_produto = int(input("Digite o código do produto que deseja adicionar ao carrinho: "))
                quantidade = int(input("Digite a quantidade que deseja adicionar: "))
                adicionar_produto_carrinho(usuario_logado, codigo_produto, quantidade)
        

        elif opcao == "5":
            if not usuarios:
                print("Faça login primeiro para remover produtos do carrinho.")
            else:
                visualizar_carrinho(usuario_logado)
                codigo_produto = int(input("Digite o código do produto que deseja remover do carrinho: "))
                remover_produto_carrinho(usuario_logado, codigo_produto)


        elif opcao == "6":
            if not usuarios:
                print("Faça o login primeiro para visualizar o carrinho.")
            else:
                visualizar_carrinho(usuario_logado)


        elif opcao == "7":
            if not usuarios:
                print("Faça login primeiro para processar a compra.")
            else:
                processar_compra(usuario_logado)


        elif opcao == "8":
            if not usuarios:
                print("Faça o login primeiro para visualizar o histórico de compras.")
            else:
                mostrar_historico_compras()


        elif opcao == "9":
            if not usuarios:
                print("Faça login primeiro para administrar o estoque.")
            else:
                administrar_estoque()


        elif opcao == "0":
            print("Saindo do Sistema...")
            break

        else:
            print("Opção inválida. Escolha uma opação válida. ")


menu_opcoes()




        
        