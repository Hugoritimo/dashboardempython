def exibir_menu():
    print("Dashboard Simples")
    print("1. Exibir gráfico de barras")
    print("2. Exibir gráfico de pizza")
    print("3. Sair")

def exibir_grafico_de_barras():
   
    print("Gráfico de Barras")

def exibir_grafico_de_pizza():
   
    print("Gráfico de Pizza")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_grafico_de_barras()
        elif opcao == '2':
            exibir_grafico_de_pizza()
        elif opcao == '3':
            print("Saindo do Dashboard...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
