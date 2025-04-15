import numpy as np

nome_estados = ["Lady Gaga", "Olivia Rodrigo", "Taylor Swift"]

matriz = np.array([
    [0.6, 0.3, 0.1],
    [0.2, 0.5, 0.3],
    [0.3, 0.3, 0.4]
])

estado_inicial = np.array([0.0, 1.0, 0.0])

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
    print(f"\nDias {i}: ")
    for j, probabilidade in enumerate(estado):
        print(f"  {nome_estados[j]}: {probabilidade *100 :.2f} ")
print()

#após alguns dias a mídia se distribuí para Lady Gaga: 35% / Olivia Rodrigo: 38% / Taylor Swift: 27%

#a partir do dia 5 a mídia se equiliba em Lady Gaga: 37% / Olivia Rodrigo: 38% / Taylor Swift: 25%