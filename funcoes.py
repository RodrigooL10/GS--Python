import json, random, re, simulacoes

def verificar_login_senha(email, senha):
    with open('db.json', 'r', encoding='utf-8') as f:
        clientes = json.load(f)
        for cliente in clientes['clientes']:
            if cliente['email'] == email:
                if cliente['senha'] == senha:
                    return True, cliente['nome'], cliente['id']
                else:
                    return False, "Senha incorreta", None

        return False, "Usuário inexistente", None
    

#Recebe dados do json e atualiza com novo cliente
def clientes_global(clientes, nome, email, senha):
    try:
        with open('db.json', 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:  # Verifica se o conteúdo do arquivo está vazio
                clientes = {'clientes':[]}
                cliente_id = 1
            else:
                f.seek(0)  # Volta para o início do arquivo
                clientes = json.load(f)   
                cliente_id = len(clientes['clientes']) + 1  # Gere um ID único

    
    except FileNotFoundError:
        clientes = {'clientes':[]}
        cliente_id = 1

    cliente = {
        'id': cliente_id,
        'nome': nome,
        'email': email,
        'senha': senha,
    }

    clientes['clientes'].append(cliente)


    with open('db.json', 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)


#Function para validar as informações obtidas do cliente
def validar_informacoes(nome, email):
    if not re.match("^[a-zA-Z\s\w~]*$", nome, re.UNICODE):
        print("Nome só pode conter letras")
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("O e-mail está inválido")
        return False
    return True

def Recomendacoes():
    print("\n---- RECOMENDAÇÕES PARA MELHORAR QUALIDADE DO SONO ----\n")

    print("1. Mantenha um Horário Regular de Sono:")
    print("- Estabeleça uma rotina de sono consistente.")

    print("\n2. Crie um Ambiente Propício para Dormir:")
    print("- Mantenha o quarto escuro, silencioso e fresco.")

    print("\n3. Limite a Exposição à Luz antes de Dormir:")
    print("- Evite dispositivos eletrônicos brilhantes antes de dormir.")
    print("- Ambientes mais escuros tendem a melhorar a qualidade do sono.")

    print("\n4. Evite Cafeína e Estímulos antes de Dormir:")
    print("- Evite cafeína e alimentos estimulantes antes de dormir.")

    print("\n5. Faça Atividades Relaxantes antes de Dormir:")
    print("- Pratique atividades relaxantes antes de dormir.")

    print("\n6. Mantenha uma Rotina de Exercícios Regular:")
    print("- Exercite-se regularmente, mas evite atividades intensas à noite.")

    print("\n7. Limite Sestas durante o Dia:")
    print("- Se tirar sestas, limite-as a 20-30 minutos durante o dia.")

    print("\n8. Ajuste a Alimentação Noturna:")
    print("- Evite refeições pesadas antes de dormir.")

    print("\n9. Consulte um Profissional de Saúde:")
    print("- Se problemas persistentes de sono persistirem, consulte um profissional.")

    option = int(input("\n1- Deseja voltar ao menu principal?\n2- Deseja fazer Log-out?\n"))
    
    return option


#Recomendacoes()







def simulador_batimentos_cardiacos(numSimulacoes, frequencia_cardiaca_min, frequencia_cardiaca_max, id):
    count = 1
    info = []

    while count <= numSimulacoes:
        batimentos_cardiacos = random.randint(frequencia_cardiaca_min, frequencia_cardiaca_max)
        #print(f"Batimentos Cardíacos: {batimentos_cardiacos} BPM")

        rotacoes = []
        aceleracoes_x = []
        aceleracoes_y = []
        aceleracoes_z = []
        iluminacoes = []
        #Se estiver abaixo de 60BPM, está dormindo
        if batimentos_cardiacos < 60:

            for _ in range (10):
                rota = simulacoes.simulador_rotacao()
                acel_x, acel_y, acel_z = simulacoes.simulador_aceleracao()
                ilum = simulacoes.simulador_iluminacao()

                rotacao = format(rota, '.2f')
                iluminacao = format(ilum, '.2f')
                aceleracao_x = format(acel_x, '.2f')
                aceleracao_y = format(acel_y, '.2f')
                aceleracao_z = format(acel_z, '.2f')


                rotacoes.append(rotacao)
                aceleracoes_x.append(aceleracao_x)
                aceleracoes_y.append(aceleracao_y)
                aceleracoes_z.append(aceleracao_z)
                iluminacoes.append(iluminacao)
            
            dados = {
                "rotacoes": rotacoes,
                "aceleracoes_x": aceleracoes_x,
                "aceleracoes_y": aceleracoes_y,
                "aceleracoes_z": aceleracoes_z,
                "iluminacoes": iluminacoes
            }
            

            info.append({f'Dia {count}' : {'dados dos sensores': dados}})

        #joga os dados simulados num json exclusivo para cada cliente
        with open(f"dadoscli{id}.json", "w", encoding='utf-8') as f:
            json.dump(info, f, indent=4, ensure_ascii=False )
        
        count += 1


# Exemplo de uso: pessoa dormindo (frequência de 40 a 60 BPM)
#simulador_batimentos_cardiacos(7, 40, 60, 2)


def MonitoramentoSono(id):
    try:
        with open(f"dadoscli{id}.json", "r", encoding='utf-8') as f:
            dados = json.load(f)

    except FileNotFoundError:   
        simulador_batimentos_cardiacos(7, 40, 60, id)
        with open(f"dadoscli{id}.json", "r", encoding='utf-8') as f:
            dados = json.load(f)

    for i in range (0, len(dados), 1):
        print(f"\n---- Dia {i+1} ----\n")
        valores_rotacoes = dados[i][f'Dia {i+1}']['dados dos sensores']["rotacoes"]
        valores_aceleracao_x = dados[i][f'Dia {i+1}']['dados dos sensores']["aceleracoes_x"]
        valores_aceleracao_y = dados[i][f'Dia {i+1}']['dados dos sensores']["aceleracoes_y"]
        valores_aceleracao_z = dados[i][f'Dia {i+1}']['dados dos sensores']["aceleracoes_z"]
        valores_iluminacao = dados[i][f'Dia {i+1}']['dados dos sensores']["iluminacoes"]

        contador_rotacao = contador_acel1 = contador_acel2 = contador_acel3 = contador_ilum = 0
        limiar = 2

        valores_rotacoes = [float(valor) for valor in valores_rotacoes]
        valores_aceleracao_x = [float(valor) for valor in valores_aceleracao_x]
        valores_aceleracao_y = [float(valor) for valor in valores_aceleracao_y]
        valores_aceleracao_z = [float(valor) for valor in valores_aceleracao_z]
        valores_iluminacao = [float(valor) for valor in valores_iluminacao]

        #Conta quantidade de vezes que o sensor de rotação detectou uma movimentação "brusca"
        for i in range(1, len(valores_rotacoes)):
            diferenca_percentual = (valores_rotacoes[i] - valores_rotacoes[i - 1]) / valores_rotacoes[i - 1] * 100
            if diferenca_percentual > 40 or diferenca_percentual < -40:
                contador_rotacao += 1
        
        #Conta quantidade de vezes que o sensor de aceleração (eixo x) detectou uma movimentação "brusca"
        for i in range(1, len(valores_aceleracao_x)):
           diferenca = abs(valores_aceleracao_x[i] - valores_aceleracao_x[i - 1])
           if diferenca > limiar or diferenca < -limiar:
            contador_acel1 += 1
        
        #Conta quantidade de vezes que o sensor de aceleração (eixo y) detectou uma movimentação "brusca"
        for i in range(1, len(valores_aceleracao_y)):
            diferenca = abs(valores_aceleracao_y[i] - valores_aceleracao_y[i - 1])
            if diferenca > limiar or diferenca < -limiar:
                contador_acel2 += 1
        
        #Conta quantidade de vezes que o sensor de aceleração (eixo z) detectou uma movimentação "brusca"
        for i in range(1, len(valores_aceleracao_z)):
            diferenca = abs(valores_aceleracao_z[i] - valores_aceleracao_z[i - 1])
            if diferenca > limiar or diferenca < -limiar:
                contador_acel3 += 1

        #Conta quantidade de vezes que o sensor de luminosidade detectou uma iluminação "alta"
        for valor in valores_iluminacao:
            if valor > 20:
                contador_ilum += 1
        
        print(f"Contador de movimentações 'abruptas' pelo sensor de rotação: {contador_rotacao}/{len(valores_rotacoes)}")
        print(f"Contador de movimentações 'abruptas' pelo sensor de aceleração (eixo x): {contador_acel1}/{len(valores_aceleracao_x)}")
        print(f"Contador de movimentações 'abruptas' pelo sensor de aceleração (eixo y): {contador_acel2}/{len(valores_aceleracao_y)}")
        print(f"Contador de movimentações 'abruptas' pelo sensor de aceleração (eixo z): {contador_acel3}/{len(valores_aceleracao_z)}")
        print(f"Contador de altas mudanças na luminosidade : {contador_ilum}/{len(valores_iluminacao)}")

        if contador_rotacao <= 5 and contador_acel3 <= 5 and contador_acel1 <= 5 and contador_acel3 <= 5:
            print("Resultado: Não se mexeu muito durante a noite, teve um boa noite sono!")

        elif contador_rotacao <= 7 and contador_acel3 <= 7 and contador_acel1 <= 7 and contador_acel3 <= 7:
            print("Resultado: Se mexeu algumas vezes, Teve uma noite de sono pouco conturbada!")
            print("É recomendado que medidas sejam tomadas para melhorar o sono")

        else:
            print("Resultado: Péssima noite de sono! RECOMENDA-SE QUE ISSO SEJA VERIFICADO URGENTEMENTE!")


        if contador_ilum <= 20:
            print("Reusltado Iluminação: Boa iluminação para uma boa noite de sono")
        elif contador_ilum > 20 and contador_ilum <= 50:
            print("Reusltado Iluminação: Iluminaçaõ OK, mas pode ter atrapalhado um pouco no sono")
        else:
            print("Reusltado Iluminação: Iluminação muito clara, recomenda-se desligar as luzes ao redor!")

    option = int(input("\n1- Deseja voltar ao menu principal?\n2- Deseja ver recomendações para melhorar o sono?\n3- Deseja fazer Log-out?\n"))
    
    return option

