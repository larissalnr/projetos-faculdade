import sys
import string

print("======== SISTEMA DE INSCRIÇÕES ========")

opcao = ''
usuarios = [
    {"nome": "João Silva", "email": "joaosilva@email.com"}, 
    {"nome": "Caroline Santos", "email": "carolinesantos@email.com"}
]

def mostrar_menu():
    print ("\n O que deseja fazer?\n")

    print("1. Novo cadastro")
    print("2. Listar usuários por ordem de cadastro")
    print("3. Listar usuários por ordem alfabética")
    print("4. Buscar usuário por nome")
    print("5. Remover usuário cadastrado")
    print("6. Alterar nome de um usuário")
    print("7. Fechar")

    global opcao
    opcao = input("\nDigite o número correspondente a ação que deseja realizar: ")

mostrar_menu()

def cadastro():
    nome = input("\nDigite o nome completo do usuário: ")
    email = input ("Digite o email do usuário: ")

    nome_maiusculo = string.capwords(nome)
    email_minusculo = email.lower()

    usuarios.append({'nome': nome_maiusculo, 'email': email_minusculo})

    print("\n-------- USUÁRIO CADASTRADO COM SUCESSO -------- ")
    mostrar_menu()

def mostrar_usuarios_por_cadastro():
    if len(usuarios) >= 1:
        for usuario in usuarios:
            print("Nome: " + usuario['nome'] + "  Email: " + usuario['email']) 
    else:
        print("Não há usuários cadastrados")
        
    mostrar_menu()

def mostrar_usuarios_por_ordem_alfabetica():
    usuarios_alfabeticos = sorted(usuarios, key=lambda obj: obj['nome'])
    if len(usuarios) >= 1:
        for usuario in usuarios_alfabeticos:
            print("Nome: " + usuario['nome'] + "  Email: " + usuario['email'])
    else:
        print("Não há usuários cadastrados")

    mostrar_menu()


def buscar_usuario_pelo_nome():
    nome_busca = input(
        "\nQual usuário deseja buscar? Favor digitar nome completo: ")
    nome_maiusculo = string.capwords(nome_busca)
    usuario_encontrado = False
    for usuario in usuarios:
        if usuario['nome'] == nome_maiusculo:
            resultado = "\nNome: " + \
                usuario['nome'] + "  Email: " + usuario['email']
            print(resultado)
            usuario_encontrado = True
    if usuario_encontrado == False:
        print("\nUsuário não encontrado")
    mostrar_menu()

def remover_usuario_por_email():
    email_usuario_a_ser_removido = input(
        "\nQual usuário deseja remover? Favor digitar o email do usuário: ")
    email_minusculo = email_usuario_a_ser_removido.lower()
    usuario_encontrado = False
    for usuario in usuarios:
        if usuario['email'] == email_minusculo:
            posicao = usuarios.index(usuario)
            usuarios.pop(posicao)
            print("\nUsuário removido com sucesso!")
            usuario_encontrado = True
    if usuario_encontrado == False:
        print("\nUsuário não encontrado")
    mostrar_menu()
    
    
def alterar_nome_por_email():
    email_usuario_a_ser_alterado = input(
        "\nQual usuário deseja alterar o nome? Favor digitar o email do usuário: ")
    email_minusculo = email_usuario_a_ser_alterado.lower()
    usuario_encontrado = False
    for usuario in usuarios:
        if usuario['email'] == email_minusculo:
            resultado = "\nNome: " + \
                usuario['nome'] + "  Email: " + usuario['email']
            usuario_encontrado = True
            print(resultado)
            novo_nome = input(
                '\nComo deseja que o nome do usuário seja salvo? ')
            nome_maiusculo = string.capwords(novo_nome)
            usuario['nome'] = nome_maiusculo
            print("\nSalvo com sucesso!")
    if usuario_encontrado == False:
        print('\nUsuário não encontrado')
    mostrar_menu()



def encerrar():
    sys.exit()


def default():
    print("\nOPÇÃO INVÁLIDA")
    mostrar_menu()


while True:
    if opcao == "1":
        cadastro()
    elif opcao == "2":
        mostrar_usuarios_por_cadastro()
    elif opcao == "3":
        mostrar_usuarios_por_ordem_alfabetica()
    elif opcao == "4":
        buscar_usuario_pelo_nome()
    elif opcao == "5":
        remover_usuario_por_email()
    elif opcao == "6":
        alterar_nome_por_email()
    elif opcao == "7":
        encerrar()
    else:
        default()