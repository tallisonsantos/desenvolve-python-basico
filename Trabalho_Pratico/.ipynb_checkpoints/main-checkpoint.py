import os

# --- Arquivos ---
ARQUIVO_USUARIOS = 'usuarios.txt'
ARQUIVO_PRODUTOS = 'produtos.txt'

# --- Gerenciamento de Arquivos ---
def ler_usuarios():
    """Lê o arquivo de usuários e retorna uma lista de dicionários."""
    usuarios = []
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r') as f:
            for linha in f.readlines():
                username, senha, permissao = linha.strip().split(',')
                usuarios.append({'username': username, 'senha': senha, 'permissao': permissao})
    return usuarios

def salvar_usuarios(usuarios):
    """Salva a lista de usuários no arquivo."""
    with open(ARQUIVO_USUARIOS, 'w') as f:
        for user in usuarios:
            f.write(f"{user['username']},{user['senha']},{user['permissao']}\n")

def ler_produtos():
    """Lê o arquivo de produtos e retorna uma lista de dicionários."""
    produtos = []
    if os.path.exists(ARQUIVO_PRODUTOS):
        with open(ARQUIVO_PRODUTOS, 'r') as f:
            for linha in f.readlines():
                codigo, nome, tipo, preco, quantidade = linha.strip().split(',')
                produtos.append({
                    'codigo': codigo,
                    'nome': nome,
                    'tipo': tipo,
                    'preco': float(preco),
                    'quantidade': int(quantidade)
                })
    return produtos

def salvar_produtos(produtos):
    """Salva a lista de produtos no arquivo."""
    with open(ARQUIVO_PRODUTOS, 'w') as f:
        for prod in produtos:
            f.write(f"{prod['codigo']},{prod['nome']},{prod['tipo']},{prod['preco']},{prod['quantidade']}\n")

# --- Gerenciamento de Usuários (CRUD) ---
def cadastrar_usuario(usuarios):
    """(C)reate: Adiciona um novo usuário."""
    print("\n--- Cadastro de Usuário ---")
    username = input("Nome de usuário: ")
    senha = input("Senha: ")
    permissao = input("Permissão (gerente/funcionario): ")
    if permissao not in ['gerente', 'funcionario']:
        print("Permissão inválida.")
        return
    
    usuarios.append({'username': username, 'senha': senha, 'permissao': permissao})
    salvar_usuarios(usuarios)
    print(f"Usuário '{username}' cadastrado com sucesso.")

def listar_usuarios(usuarios):
    """(R)ead: Lista todos os usuários."""
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    for user in usuarios:
        print(f"Usuário: {user['username']} | Permissão: {user['permissao']}")

def atualizar_usuario(usuarios):
    """(U)pdate: Atualiza a senha ou permissão de um usuário."""
    print("\n--- Atualizar Usuário ---")
    username = input("Nome de usuário para atualizar: ")
    encontrado = False
    for user in usuarios:
        if user['username'] == username:
            nova_senha = input("Nova senha (deixe em branco para não alterar): ")
            nova_permissao = input("Nova permissão (deixe em branco para não alterar): ")
            if nova_senha:
                user['senha'] = nova_senha
            if nova_permissao:
                user['permissao'] = nova_permissao
            encontrado = True
            break
    
    if encontrado:
        salvar_usuarios(usuarios)
        print(f"Usuário '{username}' atualizado com sucesso.")
    else:
        print("Usuário não encontrado.")

def deletar_usuario(usuarios):
    """(D)elete: Remove um usuário."""
    print("\n--- Deletar Usuário ---")
    username = input("Nome de usuário para deletar: ")
    usuarios_filtrados = [user for user in usuarios if user['username'] != username]
    
    if len(usuarios) > len(usuarios_filtrados):
        salvar_usuarios(usuarios_filtrados)
        print(f"Usuário '{username}' removido com sucesso.")
    else:
        print("Usuário não encontrado.")

# --- Gerenciamento de Produtos (CRUD) ---
def cadastrar_produto(produtos):
    """(C)reate: Adiciona um novo produto."""
    print("\n--- Cadastro de Produto ---")
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    tipo = input("Tipo (Sorvete/Açaí/Picolé/Complemento): ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade em estoque: "))
    
    produtos.append({
        'codigo': codigo,
        'nome': nome,
        'tipo': tipo,
        'preco': preco,
        'quantidade': quantidade
    })
    salvar_produtos(produtos)
    print(f"Produto '{nome}' cadastrado com sucesso.")

def buscar_produto(produtos):
    """(R)ead: Busca um produto por nome ou código."""
    print("\n--- Buscar Produto ---")
    termo = input("Digite o nome ou código do produto: ")
    encontrado = False
    for prod in produtos:
        if termo.lower() in prod['nome'].lower() or termo.lower() == prod['codigo'].lower():
            print(f"Código: {prod['codigo']} | Nome: {prod['nome']} | Tipo: {prod['tipo']} | Preço: R${prod['preco']:.2f} | Quantidade: {prod['quantidade']}")
            encontrado = True
    if not encontrado:
        print("Produto não encontrado.")

def listar_produtos(produtos):
    """(R)ead: Lista todos os produtos."""
    print("\n--- Lista de Produtos ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
    for prod in produtos:
        print(f"Código: {prod['codigo']} | Nome: {prod['nome']} | Preço: R${prod['preco']:.2f} | Estoque: {prod['quantidade']}")

def listar_produtos_ordenados_nome(produtos):
    """(R)ead: Lista produtos ordenados por nome."""
    print("\n--- Produtos por Nome ---")
    produtos_ordenados = sorted(produtos, key=lambda p: p['nome'])
    for prod in produtos_ordenados:
        print(f"Nome: {prod['nome']} | Preço: R${prod['preco']:.2f}")

def listar_produtos_ordenados_preco(produtos):
    """(R)ead: Lista produtos ordenados por preço."""
    print("\n--- Produtos por Preço ---")
    produtos_ordenados = sorted(produtos, key=lambda p: p['preco'])
    for prod in produtos_ordenados:
        print(f"Preço: R${prod['preco']:.2f} | Nome: {prod['nome']}")

def atualizar_produto(produtos):
    """(U)pdate: Atualiza o preço ou quantidade de um produto."""
    print("\n--- Atualizar Produto ---")
    codigo = input("Código do produto para atualizar: ")
    encontrado = False
    for prod in produtos:
        if prod['codigo'] == codigo:
            novo_preco = input("Novo preço (deixe em branco para não alterar): ")
            nova_quantidade = input("Nova quantidade (deixe em branco para não alterar): ")
            if novo_preco:
                prod['preco'] = float(novo_preco)
            if nova_quantidade:
                prod['quantidade'] = int(nova_quantidade)
            encontrado = True
            break
    if encontrado:
        salvar_produtos(produtos)
        print("Produto atualizado com sucesso.")
    else:
        print("Produto não encontrado.")

def deletar_produto(produtos):
    """(D)elete: Remove um produto."""
    print("\n--- Deletar Produto ---")
    codigo = input("Código do produto para deletar: ")
    produtos_filtrados = [p for p in produtos if p['codigo'] != codigo]
    if len(produtos) > len(produtos_filtrados):
        salvar_produtos(produtos_filtrados)
        print("Produto removido com sucesso.")
    else:
        print("Produto não encontrado.")

# --- Menus ---
def menu_gerente(produtos, usuarios):
    """Menu para usuários com permissão de gerente."""
    while True:
        print("\n--- Menu Gerente ---")
        print("1. Gerenciar Produtos")
        print("2. Gerenciar Usuários")
        print("0. Fazer Logout")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            menu_gerenciar_produtos(produtos, True)
        elif opcao == '2':
            menu_gerenciar_usuarios(usuarios)
        elif opcao == '0':
            print("Fazendo logout...")
            break
        else:
            print("Opção inválida.")

def menu_funcionario(produtos):
    """Menu para usuários com permissão de funcionário."""
    while True:
        print("\n--- Menu Funcionário ---")
        print("1. Gerenciar Produtos")
        print("0. Fazer Logout")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_gerenciar_produtos(produtos, False)
        elif opcao == '0':
            print("Fazendo logout...")
            break
        else:
            print("Opção inválida.")

def menu_gerenciar_usuarios(usuarios):
    """Sub-menu para gerenciar usuários (acessível apenas para gerentes)."""
    while True:
        print("\n--- Gerenciar Usuários ---")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_usuario(usuarios)
        elif opcao == '2':
            listar_usuarios(usuarios)
        elif opcao == '3':
            atualizar_usuario(usuarios)
        elif opcao == '4':
            deletar_usuario(usuarios)
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

def menu_gerenciar_produtos(produtos, is_gerente):
    """Sub-menu para gerenciar produtos."""
    while True:
        print("\n--- Gerenciar Produtos ---")
        print("1. Listar todos os produtos")
        print("2. Buscar produto")
        print("3. Listar por nome")
        print("4. Listar por preço")
        if is_gerente:
            print("5. Adicionar produto")
            print("6. Atualizar produto")
            print("7. Deletar produto")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_produtos(produtos)
        elif opcao == '2':
            buscar_produto(produtos)
        elif opcao == '3':
            listar_produtos_ordenados_nome(produtos)
        elif opcao == '4':
            listar_produtos_ordenados_preco(produtos)
        elif is_gerente and opcao == '5':
            cadastrar_produto(produtos)
        elif is_gerente and opcao == '6':
            atualizar_produto(produtos)
        elif is_gerente and opcao == '7':
            deletar_produto(produtos)
        elif opcao == '0':
            break
        else:
            print("Opção inválida ou não permitida.")

def main():
    """Função principal do programa."""
    while True:
        print("\n--- Sorveteria Doce Vida ---")
        print("1. Fazer Login")
        print("2. Sair do sistema")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            usuarios = ler_usuarios()
            produtos = ler_produtos()
            username = input("Nome de Usuário: ")
            senha = input("Senha: ")
            
            usuario_logado = None
            for user in usuarios:
                if user['username'] == username and user['senha'] == senha:
                    usuario_logado = user
                    break
            
            if usuario_logado:
                print(f"Login bem-sucedido! Olá, {usuario_logado['username']}!")
                if usuario_logado['permissao'] == 'gerente':
                    menu_gerente(produtos, usuarios)
                elif usuario_logado['permissao'] == 'funcionario':
                    menu_funcionario(produtos)
            else:
                print("Usuário ou senha incorretos.")
        elif opcao == '2':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()