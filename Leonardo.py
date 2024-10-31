from Joao import nota_de_compra, editar_carrinho, limpa

def cadastro_lanche():
    from Main import Lanche,session
    while True:
        limpa()
        lanche = Lanche(
            nome = input("NOME: "),
            preco = float(input("PREÇO: "))
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
        

def listando_lanches():
    from Main import Lanche,session
    lista_lanche = session.query(Lanche).all()
    for lanche in lista_lanche:
        print(f"{lanche.id} | {lanche.nome} {f"{lanche.preco}":.>20} R$")

def comprando():
    from Main import Lanche, session
    lista_compra = []
    lista_valores = []
    lista_nomes = []
    while True:
        limpa()
        listando_lanches()
        id_lanche = int(input("INFORME O ID DO LANCHE QUE DESEJA: "))
        lista_compra.append(id_lanche)
        opcao = int(input("DESEJA ALGUM OUTRO LANCHE ? \n1-SIM \n2-NÃO\n"))
        if opcao == 2:
            break
    for id_l in lista_compra:
        lanche = session.query(Lanche).filter(Lanche.id == id_l).first()
        if lanche:
            lista_valores.append(lanche.preco)
            lista_nomes.append(lanche.nome)
    for i, nome in enumerate(lista_nomes):
        print(f"{i + 1}º | {nome} {f"{lista_valores[i]:.2f}":.>20} R$")
    soma_total = sum(lista_valores)
    print(f"TOTAL: {soma_total:.2f} R$")
    return lista_valores, lista_nomes

def menu():
    print("""
1- CADASTRO DE LANCHE
2- SELECIONANDO LANCHE
3- NOTA DE COMPRA
4- EXCLUIR LANCHE
0- ENCERRAR
 """)

def menu_de_venda():
    lista_nomes =[]
    lista_valores = []
    while True:
        limpa()
        menu()
        opcao = int(input(": "))
        match opcao:
            case 1:
                cadastro_lanche()
            case 2:
                lista_valores, lista_nomes=comprando()
            case 3:
                nota_de_compra(lista_nomes,lista_valores)
            case 4:
                editar_carrinho(lista_nomes,lista_valores)
            case 0:
                break
