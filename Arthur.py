import os
def menu_principal():
    print("="*40)
    print("""
1 - CADASTRAR FUNCIONARIO
2 - FAZER LOGIN
3 - EXCLUIR CADASTRO
0 - SAIR
""")
    print("="*40)

def logo():
    print("="*40)
    print(f"{"SENAI":^40}")
    print("="*40)

def cadastro():
    from Main import Usuario, session
    cpf = verificando_cpf()
    funcionario = Usuario(
        cpf = cpf,
        nome = input("NOME: "),
        sobrenome = input("SOBRENOME: "),
        senha = input("SENHA: ")
    )
    session.add(funcionario)
    session.commit()

def verificando_cpf():
    from Main import Usuario, session
    while True:
        cpf = input("INFORME SEU CPF: ") 
        funcionario = session.query(Usuario).filter(Usuario.cpf == cpf).first()
        if funcionario is None: 
            break
        else:
            print("CPF JÁ CADASTRADO!")
    return cpf

def excluir_cadastro():
    from Main import session, Usuario
    cpf_login = input("INFORME O CPF DO FUNCIONÁRIO QUE DESEJA EXCLUIR: ")
    funcionario = session.query(Usuario).filter(Usuario.cpf == cpf_login).first()
    session.delete(funcionario)
    session.commit()
    print("FUNCIONÁRIO DELETADO DA BASE DE DADOS!")

def fazer_login():
    from Main import session, Usuario
    print("="*40)
    print(f"{"LOGIN":^40}")
    print("="*40)
    cpf_login = input("CPF PARA LOGIN: ")
    funcionario = session.query(Usuario).filter(Usuario.cpf == cpf_login).first()
    senha_login = input("INSIRA SUA SENHA: ")
    if senha_login == funcionario.senha:
        print("="*40)
        print(f"{"LOGIN EFETUADO COM SUCESSO!":^40}")
        print("="*40)        

def principal():
    while True:
        logo()
        menu_principal()
        while True:
            opcao = int(input(": "))
            if opcao in [1, 2, 3, 0]:
                break
        match opcao:
            case 1:
                while True:
                    cadastro()
                    while True:
                        opcao1 = int(input("DESEJA EFETUAR O CADASTRO DE UM NOVO FUNCIONÁRIO? \n1-SIM \n2-NÃO"))
                        limpar_tela()
                        if opcao1 in [1, 2]:
                            break
                    if opcao1 ==  2:
                        break
            case 2:
                fazer_login()   
            case 3:
                logo()
                excluir_cadastro()
                limpar_tela()
            case 0:
                break
