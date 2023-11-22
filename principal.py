import funcoes


clientes = []
menu = 0

while menu == 0:
    option = int(input("1- Deseja fazer o login? \n2- Deseja fazer o cadastro?\n"))

    if option == 1:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        acesso_permitido, nome_usuario, usuario_id = funcoes.verificar_login_senha(email, senha)

        if acesso_permitido:
            print(f"\nAcesso permitido! Bem-vindo, {nome_usuario}!\n")
            menu = 1
        else:
            print(f"\nAcesso negado: {nome_usuario}\n\n")
    
    elif option == 2:
        print("Bem-vindo! Por favor, faça o seu registro!\n")
        nome = input("Por favor, informe seu nome:\n")
        email = input("Digite o e-mail:\n")
        senha = input("Digite sua senha!\n")
        senha2 = input("Confirme sua senha!\n")

        #chama a function que valida as informações e faz as devidas checagens
        if funcoes.validar_informacoes(nome, email):
            if senha != senha2 :
                print("Por favor, verifique as informações e tente novamente.")
            else:
                print("Informações válidas. Registro concluído!")
                print("Faça o login!\n\n")
                funcoes.clientes_global(clientes, nome, email, senha)
                option = 1 #Abre o menu principal


while menu == 1:
    print(f"\n\n------Bem vindo a nossa Homepage {nome_usuario}!,Quais dos serviços disponiveis você deseja acessar------")
    option = int(input("1- Verificar monitoramento do sono \n2- Ver recomendações para Melhorar Sono\n3- Log-out\n"))

    if option == 1:
        print("--- Últimos monitoramentos: ---")

        #Faz uma simulação de dados dos últimos 7 dias
        decisao = funcoes.MonitoramentoSono(usuario_id)

        if decisao == 1:
            menu = 1
        elif decisao == 2:
            funcoes.Recomendacoes()
        else:
            print("Tchau, até logo!")
            break
    
    elif option == 2:
        decisao = funcoes.Recomendacoes()

        if decisao == 1:
            menu = 1
        else:
            print("Tchau, até logo!")
            break
    
    elif option == 3:
        print("Tchau, até logo!")
        break
