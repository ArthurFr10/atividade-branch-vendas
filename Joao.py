def limpa():
    import os
    os.system("cls||clear")
    print("="*40)
    print(f"{"SENAI":^40}")
    print("="*40)

def gerar_nota_compra(lista_nomes, lista_valores, total):
    with open("nota_compra.txt", "w") as arquivo:
        arquivo.write("Nota de Compra\n")
        for i, nome in enumerate(lista_nomes):
            arquivo.write(f"{i + 1}º | {nome} - {lista_valores[i]:.2f} R$\n")
        arquivo.write(f"TOTAL: {total:.2f} R$\n\n\n\n")
        arquivo.write("VOLTE SEMPRE!")
    print("NOTA DE COMPRA GERADA EM 'nota_compra.txt'.")


def nota_de_compra(lista_nomes, lista_valores):
    total = sum(lista_valores)
    gerar_nota_compra(lista_nomes, lista_valores, total)

def editar_carrinho(lista_nomes, lista_valores):
    while True:
        limpa()
        print("CARRINHO DE COMPRAS:")
        for i in range(len(lista_nomes)):
            print(f"{i + 1}º | {lista_nomes[i]} - {lista_valores[i]:.2f} R$")
        
        soma_total = sum(lista_valores)
        print(f"TOTAL: {soma_total:.2f} R$")
        
        opcao_remover = input("DESEJA REMOVER ALGUM LANCHE? (S/N): ").lower()
        if opcao_remover == 's':
            indice = int(input("INFORME O NUMERO DO LANCHE: "))
            removed_lanche = lista_nomes[indice - 1]  
            lista_nomes.pop(indice - 1)  
            lista_valores.pop(indice - 1)
            print(f"{removed_lanche} REMOVIDO DO CARRINHO.")
        else:
            break
    print("CARRINHO ATUALIZADO.")


