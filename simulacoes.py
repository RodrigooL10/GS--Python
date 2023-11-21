import random

def simulador_rotacao():

    rotacao = random.uniform(0, 360)  # Valores de rotação entre 0 e 360 graus
    #print(f"Rotação: {rotacao:.2f} graus")

    return rotacao

# Exemplo de uso:


def simulador_aceleracao():

    aceleracao_x = random.uniform(-10, 10)  # Valores de aceleração ao longo do eixo x
    aceleracao_y = random.uniform(-10, 10)  # Valores de aceleração ao longo do eixo y
    aceleracao_z = random.uniform(-10, 10)  # Valores de aceleração ao longo do eixo z
    #print(f"Aceleração: X={aceleracao_x:.2f}, Y={aceleracao_y:.2f}, Z={aceleracao_z:.2f}")
    
    return aceleracao_x, aceleracao_y, aceleracao_z

# Exemplo de uso:


def simulador_iluminacao():

    iluminacao = random.uniform(0, 20)  # Valores de iluminação entre 0 e 20 % simulando um quarto escuro
    #print(f"Iluminação: {iluminacao:.2f}%")
    
    return iluminacao

# Exemplo de uso:
