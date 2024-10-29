def limpa():
    import os
    os.system("cls||clear")

def cadastro_lanche():
    from Main import Lanche,session
    while True:
        lanche = Lanche(
            nome = input("Nome: "),
            preco = float(input("Valor: "))
        )
        session.add(lanche)
        session.commit()
        print("LANCHE ADICIONADO COM SUCESSO.")
        while True:
            opcao1 = int(input("Deseja adicionar outro lanche ? \n1-SIM \n2-NÂO"))
            if opcao1 in [1, 2]:
                break
        if opcao1 == 2:
            break
        limpa()

def listando_lanches():
    limpa()
    from Main import Lanche,session
    lista_lanche = session.query(Lanche).all()
    for lanche in lista_lanche:
        print(f"{lanche.id} | {lanche.nome}     -     {lanche.preco}R$")

def comprando():
    from Main import Lanche, session
    lista_compra = []
    lista_valores = []
    lista_nomes = []
    while True:
        listando_lanches()
        id_lanche = int(input("INFORME O ID DO LANCHE QUE DESEJA: "))
        lista_compra.append(id_lanche)
        opcao = int(input("DESEJA ALGUM OUTRO LANCHE ? \n1-SIM \n2-NÃO\n"))
        if opcao == 2:
            break
        limpa()
    for id_l in lista_compra:
        lanche = session.query(Lanche).filter(Lanche.id == id_l).first()
        if lanche:
            lista_valores.append(lanche.preco)
            lista_nomes.append(lanche.nome)
    for i, nome in enumerate(lista_nomes):
        print(f"{i + 1}º | {nome} - {lista_valores[i]:.2f} R$")
    soma_total = sum(lista_valores)
    print(f"TOTAL: {soma_total:.2f} R$")

def menu():
    print("""
1- CADASTRO DE LANCHE
2- CARRINHO DE LANCHE
3- NOTA DE COMPRA
4- EXCLUIR LANCHE
5- EDITAR LANCHE
0- ENCERRAR
 """)

def menu_de_venda():
    while True:
        menu()
        opcao = int(input(": "))
        match opcao:
            case 1:
                cadastro_lanche()
            case 2:
                    comprando()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 0:
                break
