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
                # Escrever os dados no arquivo JSON
            json.dump(info, f, indent=4, ensure_ascii=False )
        
        count += 1


            # print(f"\nMonitoramento {count}")

            # print("\n---Dados dos sensores: ---\n")

            # #Não se mexeu
            # if rotacao == rotacao2:
            #     print("Sensor de rotação: Não se mexeu\n")
            # else:
            #     print("Sensor de rotação: Se mexeu\n")
            
            # #Não acelerou
            # if aceleracao_x == aceleracao_x2 and aceleracao_y == aceleracao_y2 and aceleracao_z == aceleracao_z2:
            #     print("Sensor de aceleração: Não se mexeu\n")
            # else:
            #     print("Sensor de aceleração: Se mexeu\n")
            

            # if iluminacao <= 20:
            #     print("Iluminação escura\n")

            # elif iluminacao > 20 and iluminacao <= 50:
            #     print("iluminação clara\n")
            
            # else:
            #     print("Iluminação muito clara\n")


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

    valores_rotacoes = dados[0]['Dia 1']['dados dos sensores']["rotacoes"]

    contador_rotacao = 0

    valores_rotacoes = [float(valor) for valor in valores_rotacoes]

    for i in range(1, len(valores_rotacoes)):
        diferenca_percentual = (valores_rotacoes[i] - valores_rotacoes[i - 1]) / valores_rotacoes[i - 1] * 100
        if diferenca_percentual > 40 or diferenca_percentual < -40:
            contador_rotacao += 1
    
    print(f"Contador de movimentações 'abruptas': {contador_rotacao}/{len(valores_rotacoes)}")
    

MonitoramentoSono(3)