#agressivo = 60%
#mdefensivo = 40%

#defensivo = 30%
#magressivo = 70%

#finalizar = 70% - 10

agressivo = 0.6
mdefensivo = 0.4

defensivo = 0.3
magressivo = 0.7

import numpy as np

nome_estados = ["agressivo", "defensivo"]

matriz = np.array([
    [0.6, 0.4],
    [0.3, 0.7]
])

estado_inicial = np.array([0.0, 1.0])

def cadeia_markov(matriz, estado_inicial, periodos):
    estados = [estado_inicial]  # Armazena os estados ao longo do tempo
    
    for i in range(periodos):
        # Multiplicar o estado atual pela matriz de transição
        novo_estado = np.dot(estados[-1], matriz)
        estados.append(novo_estado)  # Adiciona o novo estado à lista
    
    estados = np.array(estados).round(2)  # Converte para array para facilitar a manipulação
    return estados

# Solicita ao usuário o número de períodos
periodos = int(input("Por favor, informe o número de períodos: "))

# Calcula a cadeia de Markov
response = cadeia_markov(matriz, estado_inicial, periodos)

# Exibe os resultados
for i, estado in enumerate(response):
    print(f"\nIntervalo {i}: ")
    for j, probabilidade in enumerate(estado):
        print(f"  {nome_estados[j]}: {probabilidade *100 :.2f} ")
print()

finalizar = 0.7

#===========================================================================#

p_agressivo = 0.5
p_defensivo = 0.5
p_fagressivo = 0.9
p_fdefensivo = 0.2
p_pagressivo = 0.7
p_pdefensivo = 0.4

p_total = (p_fagressivo * p_pagressivo * p_agressivo) + (p_defensivo * p_fdefensivo * p_pdefensivo)
print(f"{p_total * 100:.2f}")

p_agressiva = (p_agressivo * p_fagressivo * p_pagressivo) / p_total
print(f"{p_agressiva * 100:.2f}")

#a cadeia de markov é mais útil para calcular a probabildade de que na terceira partida ele jogue de forma agressiva pois a cadeia irá trabalhar com périodos de tempo que estimam a mudança de comportamento do jogador conforme o tempo passa.

#a rede bayesiana é mais útil para calcular a probabilidade dele estar jogando de forma agressiva conforme a posse de bola e as finalizações pois com essa rede poderemos calcular utilizando os dados de posse e de finalizações calculando a probabilidade total e divindo esse valor pelas variaveis agressivas do jogador então recebendo a porcentagem dele estar jogando agressivamente