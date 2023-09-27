import statistics

amostras = input("Digite as amostras: ")

# Separa as amostras em uma lista
amostras_array = [float(numero) for numero in amostras.split(' ')]

# Calcula a média
media = sum(amostras_array) / len(amostras_array)

# Calcula o desvio
desvios = [abs(x - media) for x in amostras_array]

# Calcula a variância
variancia = sum([x ** 2 for x in desvios]) / len(desvios)

# Calcula o desvio padrão
desvio_padrao = variancia ** 0.5

# Calcula a moda
moda = statistics.mode(amostras_array)

# Calcula a moda
mediana = statistics.median(amostras_array)

print("Amostras: ", amostras_array)
print("Média: ", media)
print("Desvio: ", desvios)
print("Variância: ", variancia)
print("Desvio padrão: ", desvio_padrao)
print("Moda: ", moda)
print("Mediana: ", mediana)
