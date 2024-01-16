estoque = {}

def registrar_entrada():
    codigo = input("Digite o código da mercadoria: ")
    quantidade = int(input("Digite a quantidade de mercadorias entrando: "))
    
    if codigo in estoque:
        estoque[codigo] += quantidade
    else:
        estoque[codigo] = quantidade

    print(f"Entrada registrada. Estoque atual para o código {codigo}: {estoque[codigo]}")

def registrar_saida():
    codigo = input("Digite o código da mercadoria: ")
    quantidade = int(input("Digite a quantidade de mercadorias saindo: "))
    
    if codigo in estoque:
        if quantidade <= estoque[codigo]:
            estoque[codigo] -= quantidade
            print(f"Saida registrada. Estoque atual para o código {codigo}: {estoque[codigo]}")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Código de mercadoria não encontrado.")

def verificar_estoque():
    print("\nEstoque Atual:")
    for codigo, quantidade in estoque.items():
        print(f"Código: {codigo}, Quantidade: {quantidade}")
    print("\n")

def menu():
    while True:
        print("Controle de Mercadorias")
        print("1 - Registrar Entrada")
        print("2 - Registrar Saída")
        print("3 - Verificar Estoque")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            registrar_entrada()
        elif opcao == '2':
            registrar_saida()
        elif opcao == '3':
            verificar_estoque()
        elif opcao == '4':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
