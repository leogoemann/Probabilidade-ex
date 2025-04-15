import numpy as np

#F = focado
#E = eufórico
#P = perigoso

nome_estados = ["focado", "euforico", "perigoso"]

matriz = np.array([
    [0.6, 0.3, 0.1],
    [0.4, 0.4, 0.2],
    [0., 0.5, 0.3]
])

estado_inicial = np.array([1.0, 0.0, 0.0])

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

#Após 2 intervalos a distribuição de probabilidade focado:48% / euforico:35% / perigoso:15%

#Após o terceiro a probabilidade dele estar no estado perigoso é: 16%

#Existe uma contribuição estacionária para eddie a distribuição estacionária é:
#Focado: 46%, Eufórico: 37%, Perigoso: 17%

#Eddie se mantem focado porém frequentemente fica eufórico e no estado perigoso